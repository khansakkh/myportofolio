from django.contrib.auth.models import Group, User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Education

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution_name="Sekolah Khusus Atlantis",
            degree="S1 Sistem Informasi",
            start_year=2023,
        )
        self.admin = User.objects.create_superuser(
            "owner", "owner@example.com", "password123"
        )
        self.editor = User.objects.create_user("editor", password="password123")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.reader = User.objects.create_user("reader", password="password123")

    def test_page_is_shell_and_modal_is_owner_only(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education_list.html")
        self.assertContains(response, 'id="education-grid"')
        self.assertNotContains(response, self.education.institution_name)
        self.assertNotContains(response, 'id="education-form"')

        self.client.force_login(self.admin)
        response = self.client.get(reverse("main:show_education"))
        self.assertContains(response, 'id="education-form"')

    def test_json_search_and_star_metadata(self):
        self.education.starred_by.add(self.reader)
        url = reverse("main:get_education_json")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        item = response.json()[0]
        self.assertEqual(item["fields"]["institution_name"], "Sekolah Khusus Atlantis")
        self.assertEqual(item["fields"]["star_count"], 1)
        self.assertFalse(item["fields"]["is_starred"])
        self.assertEqual(item["fields"]["starred_by_names"], "reader")
        self.assertEqual(self.client.get(url, {"search": "tidak ada"}).json(), [])
        self.assertEqual(len(self.client.get(url, {"search": "atlAntis"}).json()), 1)

        self.client.force_login(self.reader)
        self.assertTrue(self.client.get(url).json()[0]["fields"]["is_starred"])

    def test_ajax_create_permissions_validation_and_sanitization(self):
        url = reverse("main:create_education_ajax")
        data = {
            "institution_name": "<b>Universitas Indonesia</b>",
            "degree": "S1 <i>Sistem Informasi</i>",
            "start_year": "2023",
            "end_year": "",
        }
        self.assertEqual(self.client.post(url, data).status_code, 403)
        self.client.force_login(self.editor)
        self.assertEqual(self.client.post(url, data).status_code, 403)
        self.client.force_login(self.admin)

        invalid = {**data, "institution_name": '<img src="x" onerror="alert(1)">'}
        response = self.client.post(url, invalid)
        self.assertEqual(response.status_code, 400)
        self.assertIn("institution_name", response.json()["errors"])

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        created = Education.objects.get(pk=response.json()["pk"])
        self.assertEqual(created.institution_name, "Universitas Indonesia")
        self.assertEqual(created.degree, "S1 Sistem Informasi")

    def test_ajax_create_requires_csrf(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.admin)
        url = reverse("main:create_education_ajax")
        data = {
            "institution_name": "Universitas Indonesia",
            "degree": "S1 Sistem Informasi",
            "start_year": "2023",
        }
        self.assertEqual(client.post(url, data).status_code, 403)
        client.get(reverse("main:show_education"))
        token = client.cookies["csrftoken"].value
        self.assertEqual(
            client.post(url, data, HTTP_X_CSRFTOKEN=token).status_code, 201
        )

from django.core.exceptions import ValidationError
from django.forms import ModelForm, NumberInput, Textarea, TextInput, URLInput
from django.utils.html import strip_tags

from main.models import Education, Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/username/project",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()

        if not title:
            raise ValidationError(
                "Nama proyek tidak boleh hanya berisi tag HTML."
            )

        return title

    def clean_tech_stack(self):
        return strip_tags(
            self.cleaned_data["tech_stack"]
        ).strip()

    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution_name", "degree", "start_year", "end_year"]
        labels = {
            "institution_name": "Nama Institusi",
            "degree": "Gelar / Jenjang",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai",
        }
        widgets = {
            "institution_name": TextInput(
                attrs={"placeholder": "Universitas Indonesia"}
            ),
            "degree": TextInput(
                attrs={"placeholder": "S1 Sistem Informasi"}
            ),
            "start_year": NumberInput(
                attrs={"placeholder": "2023"}
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2027 (kosongkan jika masih berlangsung)"
                }
            ),
        }
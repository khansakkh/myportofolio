from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput
from main.models import Project, Education


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
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }


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
            "institution_name": TextInput(attrs={"placeholder": "Universitas Indonesia"}),
            "degree": TextInput(attrs={"placeholder": "S1 Sistem Informasi"}),
            "start_year": NumberInput(attrs={"placeholder": "2023"}),
            "end_year": NumberInput(attrs={"placeholder": "2027 (kosongkan jika masih berlangsung)"}),
        }
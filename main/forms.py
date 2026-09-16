from django.forms import ModelForm, TextInput, NumberInput
from main.models import Education

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
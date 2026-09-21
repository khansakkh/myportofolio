from django.contrib import messages
from django.shortcuts import render, redirect
from main.forms import EducationForm
from main.models import Experience, Education
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def show_main(request):
    context = {
        "name": "Khansa",
        "npm": "2506536465",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Undergraduate student of information systems that has interest in "
            "technology, business, and risk management."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Khansa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all()
    context = {
        'education_list': education_list,
    }
    return render(request, "education_list.html", context)


def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {"name": "Khansa", "form": form}
    return render(request, "education_form.html", context)

def get_education_json(request):
    search_query = request.GET.get("search", "").strip()
    education = Education.objects.all()

    if search_query:
        education = education.filter(institution_name__icontains=search_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {"name": "Khansa", "form": form}
    return render(request, "education_form.html", context)
from django.shortcuts import render

from main.models import Experience

from main.models import Education



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
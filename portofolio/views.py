from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def landing_page(request):
    return render(request, "index.html")

def get_education_json(request):
    search_query = request.GET.get("search", "").strip()
    education = Education.objects.all()

    if search_query:
        education = education.filter(institution_name__icontains=search_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")
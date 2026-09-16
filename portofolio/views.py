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

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")
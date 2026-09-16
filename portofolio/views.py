from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def landing_page(request):
    return render(request, "index.html")
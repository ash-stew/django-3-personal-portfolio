from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # grabs all objects from DB that are project objects
    return render(request, 'portfolio/home.html', {'projects':projects}) # puts inside of list

def about(request):
    return render(request, 'portfolio/about.html') 
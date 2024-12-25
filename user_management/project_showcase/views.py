
from django.shortcuts import render
from .models import Project

def project_showcase(request):
    projects = Project.objects.all()
    return render(request, 'project_showcase/project_showcase.html', {'projects': projects})


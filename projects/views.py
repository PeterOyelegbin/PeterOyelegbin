from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project


# Create your views here.
def home(request):
    return render(request, 'home.html')


def webProject(request):
    web_projects = Project.objects.filter(category="Web")
    return render(request, "web_projects.html", {"web_obj": web_projects})


def cloudProject(request):
    cloud_projects = Project.objects.filter(category="Cloud")
    return render(request, "cloud_projects.html", {"cloud_obj": cloud_projects})

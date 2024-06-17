from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Project


# Create your views here.
def home(request):
    return render(request, 'home.html')


def webProject(request):
    try:
        web_projects = Project.objects.filter(category="Web")
        return render(request, "web_projects.html", {"web_obj": web_projects})
    except ObjectDoesNotExist:
        return render(request, "home.html", {"error_message": "⚠️ Error fetching web projects."})
    except Exception as e:
        return render(request, "home.html", {"error_message": f"⚠️ An unexpected error occurred: {str(e)}"})


def cloudProject(request):
    try:
        cloud_projects = Project.objects.filter(category="Cloud")
        return render(request, "cloud_projects.html", {"cloud_obj": cloud_projects})
    except ObjectDoesNotExist:
        return render(request, "home.html", {"error_message": "⚠️ Error fetching cloud projects."})
    except Exception as e:
        return render(request, "home.html", {"error_message": f"⚠️ An unexpected error occurred: {str(e)}"})
    
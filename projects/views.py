from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from .forms import ContactRequestForm
from .models import Project
from .notifications import notify_admin_of_project_request
from reviews.models import Review
from reviews.forms import ReviewForm
from reviews.notifications import notify_admin_of_review_submission


# Create your views here.
# def home(request):
#     return render(request, 'home.html')


# def webProject(request):
#     try:
#         web_projects = Project.objects.filter(category="Web")
#         return render(request, "web_projects.html", {"web_obj": web_projects})
#     except ObjectDoesNotExist:
#         return render(request, "home.html", {"error_message": "⚠️ Error fetching web projects."})
#     except Exception as e:
#         return render(request, "home.html", {"error_message": f"⚠️ An unexpected error occurred: {str(e)}"})


# def cloudProject(request):
#     try:
#         cloud_projects = Project.objects.filter(category="Cloud")
#         return render(request, "cloud_projects.html", {"cloud_obj": cloud_projects})
#     except ObjectDoesNotExist:
#         return render(request, "home.html", {"error_message": "⚠️ Error fetching cloud projects."})
#     except Exception as e:
#         return render(request, "home.html", {"error_message": f"⚠️ An unexpected error occurred: {str(e)}"})


def home(request):
    try:
        is_review_submission = request.POST.get("form_type") == "review"
        is_contact_submission = request.POST.get("form_type") == "contact"
        review_form = ReviewForm(
            request.POST if request.method == "POST" and is_review_submission else None
        )
        contact_form = ContactRequestForm(
            request.POST if request.method == "POST" and is_contact_submission else None
        )
        if request.method == "POST":
            if is_review_submission and review_form.is_valid():
                review_form.save()
                notify_admin_of_review_submission()
                messages.success(
                    request,
                    "Your review has been submitted and is awaiting approval.",
                    extra_tags="review",
                )
                return redirect("home")
            if is_contact_submission and contact_form.is_valid():
                notify_admin_of_project_request(**contact_form.cleaned_data)
                messages.success(
                    request,
                    "Your message has been sent. I'll be in touch soon.",
                    extra_tags="contact",
                )
                return redirect("home")

        project_pages = Paginator(Project.objects.all(), 2)
        review_pages = Paginator(Review.objects.filter(verify=True), 1)
        return render(request, "index.html", {
            "project_pages": project_pages,
            "review_pages": review_pages,
            "review_form": review_form,
            "contact_form": contact_form,
        })
    except ObjectDoesNotExist:
        return render(request, "index.html", {"error_message": "⚠️ Error fetching projects."})
    except Exception as e:
        return render(request, "index.html", {"error_message": f"⚠️ An unexpected error occurred: {str(e)}"})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import ReviewForm
from .models import Review
from .notifications import notify_admin_of_review_submission
from utils import get_gravatar_url


# Create your views here.
def addReviews(request):
    formset = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            notify_admin_of_review_submission()
            messages.success(request, 'Review submitted successfully')
            return redirect('contact')
        else:
            messages.error(request, formset.errors)
    try:
        reviews = Review.objects.filter(verify=True).select_related()  # Optimize DB access
        for review in reviews:
            review.gravatar_url = get_gravatar_url(review.email)
        return render(request, 'contact.html', {'formset': formset, 'reviews': reviews})
    except ObjectDoesNotExist:
        error_message = "⚠️ Error fetching reviews."
    except Exception as e:
        error_message = f"⚠️ An unexpected error occurred: {str(e)}"
    # Handle any errors by rendering the home page with an error message
    return render(request, "home.html", {"formset": formset, "error_message": error_message})

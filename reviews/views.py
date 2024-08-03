from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .forms import ReviewForm
from .models import Review
from utils import get_gravatar_url, send_async_email
import threading


# Create your views here.
def addReviews(request):
    formset = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if formset.is_valid():
            # Asynchronously handle send mail
            threading.Thread(target=send_async_email, args=(
                'Portfolio: New Review Uploaded',
                f"""Dear Peter,\n\nA new review has been submitted for approval on your portfolio,
                kindly attend to the review as it awaits your approval.\n\nBest regards,
                \nhttps://peteroyelegbin.onrender.com/admin""",
                settings.EMAIL_HOST_USER,
                ['peteroyelegbin@gmail.com']
            )).start()
            formset.save()
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

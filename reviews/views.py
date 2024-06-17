from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import ReviewForm
from .models import Review
import hashlib


# Create your views here.
def get_gravatar_url(email, size=100):
    email_hash = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"


def addReviews(request):
    formset = ReviewForm(request.POST or None)
    if formset.is_valid():
        formset.save()
        messages.success(request, 'Review submitted successfully')
        return redirect('contact')
    else:
        try:
            reviews = Review.objects.filter(verify=True)
            for review in reviews:
                review.gravatar_url = get_gravatar_url(review.email)
            return render(request, 'contact.html', {'formset': formset, 'reviews': reviews,})
        except ObjectDoesNotExist:
            return render(request, "home.html", {"error_message": "⚠️ Error fetching reviews."})
        except Exception as e:
            return render(request, "home.html", {"error_message": f"⚠️ An unexpected error occurred: {str(e)}"})

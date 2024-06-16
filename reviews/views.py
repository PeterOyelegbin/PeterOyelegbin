from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
import hashlib


# Create your views here.
def get_gravatar_url(email, size=100):
    email_hash = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"


def addReviews(request):
    formset = ReviewForm(request.POST or None)
    reviews = Review.objects.filter(verify=True)
    if formset.is_valid():
        formset.save()
        messages.success(request, 'Review submitted successfully')
        return redirect('home')
    else:
        for review in reviews:
            review.gravatar_url = get_gravatar_url(review.email)
        return render(request, 'contact.html', {'formset': formset, 'reviews': reviews,})

from django.shortcuts import render, redirect
from django.views import generic
from .models import Review
from .forms import ReviewForm


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by("-created")
    template_name = 'reviews.html'


# New review
def review(request):

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.username = request.user
            review.save()
            return redirect('reviews')
    else:
        review = ReviewForm()

    return render(request, 'new-review.html', {'review_form': review})

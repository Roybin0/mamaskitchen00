from django.shortcuts import render
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by("-created")
    template_name = 'reviews.html'

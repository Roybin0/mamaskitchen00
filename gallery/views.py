from django.shortcuts import render
from django.views import generic
from .models import Image


class ImageList(generic.ListView):
    model = Image
    queryset = Image.objects.filter(published=True).order_by("type")
    template_name = 'gallery.html'
    paginate_by = 9

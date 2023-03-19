from django import forms
from .models import Review
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'stars', 'review', 'image']
        widgets = {'username': forms.HiddenInput()}

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'first_name', 'stars', 'review', 'image', 'created',
                  'reply',]
        widgets = {'created': forms.HiddenInput(),
                   'reply': forms.HiddenInput(),
                   }

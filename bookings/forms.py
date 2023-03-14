from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'party_size', 'date', 'time',
                  'special_occasion', 'special_requirements', 'booking_ref',]
        widgets = {'booking_ref': forms.HiddenInput(),
                   'date': forms.DateInput(
                    format=('%d/%m/%Y'),
                    attrs={'class': 'form-control',
                           'placeholder': 'Select a date',
                           'type': 'date'}
                    )}

from django import forms
from .models import Booking
from allauth.account.forms import SignupForm


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


class SignupForm(SignupForm):
    name = forms.CharField(max_length=50, label='Name:')
    phone = forms.IntegerField(label='Phone No.:')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Email:')

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user


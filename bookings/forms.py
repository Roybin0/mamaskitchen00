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
    first_name = forms.CharField(max_length=50, label='First name:')
    last_name = forms.CharField(max_length=50, label='Last name:')
    phone = forms.IntegerField(label='Phone No.:')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Email:')

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user

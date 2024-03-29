from django.shortcuts import render
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact-success.html')
    form = ContactForm()

    return render(request, 'contact.html', {'contact_form': form})


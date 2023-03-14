from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def home(request):
    return render(request, 'index.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def booking(request):

    if request.method == 'POST':
        booking = BookingForm(request.POST)
        if booking.is_valid():
            if int(request.POST.get('party_size')) > isSpaceAvailable(
                    request.POST.get('date'), request.POST.get('time')):
                messages.add_message(
                    request, messages.ERROR, 'There are no tables available at\
                        this time. Choose another time or date.')
            else:
                booking.save()
                return HttpResponseRedirect('/thanks/')
    else:
        booking = BookingForm()

    return render(request, 'booking.html', {'booking_form': booking})


# Check for available seats - 40 seats available per hour
def isSpaceAvailable(date, time):

    maxSeats = 40
    seatsTaken = 0
    bookings_by_date = Booking.objects.filter(date=date)
    bookings_by_time = bookings_by_date.filter(time=time)
    for booking in bookings_by_time:
        seatsTaken = seatsTaken + booking.party_size
    availableSeats = maxSeats - seatsTaken
    return availableSeats

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


# Home page
def home(request):
    return render(request, 'index.html')


# Thank you page - Shows after successful booking 
def thankyou(request):
    return render(request, 'thankyou.html')


# Cancellation page - Shows afer booking is successfully cancelled
def cancelled(request):
    return render(request, 'cancelled.html')


# Menu page
def menu(request):
    return render(request, 'menu.html')


# Privacy policy page
def privacy(request):
    return render(request, 'privacy.html')


# New booking page
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


# Page to enter reference number to edit booking
def enter_ref_edit(request):
    return render(request, 'edit-booking-ref.html')


# Edit booking page
def edit_booking(request, booking_ref):
    booking = get_object_or_404(Booking, booking_ref=booking_ref)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit-booking.html', {'edit_form': form})


# Page to enter reference number to delete booking
def enter_ref_delete(request):
    return render(request, 'delete-booking-ref.html')


# Delete booking page
def delete_booking(request, booking_ref):
    booking = get_object_or_404(Booking, booking_ref=booking_ref)

    if request.method == 'POST':
        booking.delete()
        return redirect('cancelled')

    return render(request, 'cancel-confirmation.html', {'booking': booking})

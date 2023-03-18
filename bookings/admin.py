from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_filter = ('date', 'name')
    list_display = ('name', 'booking_ref', 'date', 'time', 'party_size',
                    'confirmed', 'special_occasion', 'special_requirements')
    search_fields = ('name', 'booking_ref', 'email', 'date')
    actions = ['approve_selected_bookings']

    def approve_selected_bookings(self, request, queryset):
        queryset.update(confirmed=True)

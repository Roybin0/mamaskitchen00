from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_filter = ('date', 'name')
    list_display = ('name', 'date', 'time', 'party_size', 'confirmed')
    search_fields = ('name', 'email', 'date')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(confirmed=True)

from django.test import TestCase
from .models import Booking
from django.contrib import messages


class TestViews(TestCase):

    def test_load_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_load_booking_page(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_load_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_load_privacy_page(self):
        response = self.client.get('/privacy-policy')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy.html')
    
    def test_can_book_table(self):
        response = self.client.post('/booking/', {'phone': 12345})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_booking_fails_if_overbooked(self):
        seats_taken = 30
        booking = Booking.objects.create(booking_ref=2245114, party_size=5,
                                         phone=12345)
        response = self.client.post(
            f'/edit-booking/{booking.booking_ref}', {'phone': 5544545})
        if (seats_taken + booking.party_size > 40):
            self.assertIsNotNone(messages.ERROR)
        else:
            self.assertRedirects(response, 'thankyou')

    def test_booking_ref_gets_booking(self):
        booking = Booking.objects.create(booking_ref=2245114, phone=12345)
        response = self.client.get(f'/edit-booking/{booking.booking_ref}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-booking.html')

    def test_can_edit_booking(self):
        booking = Booking.objects.create(booking_ref=2245114, phone=12345,
                                         party_size=5)
        response = self.client.post(
            f'/edit-booking/{booking.booking_ref}', {'party_size': 2})
        self.assertRedirects(response, 'thankyou')
        updated_booking = Booking.objects.get(booking_ref=2245114)
        self.assertEqual(updated_booking.party_size, 2)

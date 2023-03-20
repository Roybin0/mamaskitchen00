from django.test import TestCase
from .models import Booking
from datetime import datetime


class TestModel(TestCase):

    def test_name_is_a_string(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        self.assertEqual(str(booking.name), 'Test')

    def test_email_is_a_string(self):
        booking = Booking.objects.create(
            name='Test', phone=12345, email="123@123.com")
        self.assertEqual(str(booking.email), '123@123.com')

    def test_phone_is_integer(self):
        booking = Booking.objects.create(
            name='Test', phone=12345, email="123@123.com")
        self.assertEqual(int(booking.phone), 12345)

    def test_party_size_1_to_10(self):
        booking = Booking.objects.create(
            name='Test', phone=12345, party_size=7)
        self.assertGreaterEqual(booking.party_size, 1)
        self.assertLessEqual(booking.party_size, 10)

    def test_date_is_not_past(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        today = datetime.now()
        self.assertGreaterEqual(today, booking.date)

    def test_special_occasion_defaults_to_no(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        self.assertEqual(booking.special_occasion, 'No')

    def test_special_requirements_defaults_to_none(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        self.assertEqual(booking.special_requirements, 'None')

    def test_booking_ref_generated(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        self.assertIsNotNone(booking.booking_ref)

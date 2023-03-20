from django.test import TestCase
from .forms import BookingForm


blank_form = BookingForm({'name': ''},
                         {'email': ''},
                         {'phone': ''},
                         {'party_size': ''},
                         {'date': ''},
                         {'time': ''},
                         {'special_occasion': ''},
                         {'special_requirements': ''})

test_form = BookingForm({'name': 'test'},
                        {'email': 'test@test.com'},
                        {'phone': '12345'},
                        {'party_size': '4'},
                        {'date': '2023-03-22'},
                        {'time': '4PM'},
                        {'special_occasion': 'No'},
                        {'special_requirements': 'None'},
                        {'booking_ref': '5547854'})


class TestBookingForm(TestCase):

    def test_all_fields_are_required(self):
        form = blank_form
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertIn('phone', form.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'This field is required.')
        self.assertIn('party_size', form.errors.keys())
        self.assertEqual(
            form.errors['party_size'][0], 'This field is required.')
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_booking_ref_is_generated(self):
        form = test_form
        self.assertIsNotNone(form.booking_ref)

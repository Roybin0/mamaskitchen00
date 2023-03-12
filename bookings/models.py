from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, date
import random


TIME_CHOICES = (
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
)


def create_booking_ref():
    unique_ref = random.randint(10000000, 99999999)
    booking_ref = Booking.objects.values_list('booking_ref')
    for ref in booking_ref:
        if unique_ref == ref:
            unique_ref = random.randint(10000000, 99999999)
    return unique_ref


class Booking(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    party_size = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    date = models.DateField(
        default=datetime.now,
        validators=[
            MinValueValidator(date.today())
        ])
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    special_occasion = models.TextField(default="No")
    special_requirements = models.TextField(default="None")
    booking_ref = models.CharField(
        max_length=8,
        blank=True,
        unique=True,
        primary_key=True,
        default=create_booking_ref
        )
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Booking request from {self.name} for {self.party_size} people"

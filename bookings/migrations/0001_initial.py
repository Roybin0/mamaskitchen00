# Generated by Django 3.2.18 on 2023-03-12 19:33

import bookings.models
import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('party_size', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('date', models.DateField(default=datetime.datetime.now, validators=[django.core.validators.MinValueValidator(datetime.date(2023, 3, 12))])),
                ('time', models.CharField(choices=[('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM')], max_length=10)),
                ('special_occasion', models.BooleanField(default=False)),
                ('special_requirements', models.BooleanField(default=False)),
                ('booking_ref', models.CharField(blank=True, default=bookings.models.create_booking_ref, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

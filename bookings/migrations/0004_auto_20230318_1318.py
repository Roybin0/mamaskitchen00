# Generated by Django 3.2.18 on 2023-03-18 13:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime.now, validators=[django.core.validators.MinValueValidator(datetime.date(2023, 3, 18))]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='special_occasion',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='special_requirements',
            field=models.CharField(default='None', max_length=50),
        ),
    ]

# Generated by Django 3.2.18 on 2023-03-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.IntegerField(choices=[(0, 'Starters'), (1, 'Mains'), (2, 'Dessert')], default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

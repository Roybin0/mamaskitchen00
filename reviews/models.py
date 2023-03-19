from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    review = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

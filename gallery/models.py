from django.db import models
from cloudinary.models import CloudinaryField


TYPE = ((0, 'Starters'), (1, 'Mains'), (2, 'Dessert'))


class Image(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    type = models.IntegerField(choices=TYPE, blank=False, default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

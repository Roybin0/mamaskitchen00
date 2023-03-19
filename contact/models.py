from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.email

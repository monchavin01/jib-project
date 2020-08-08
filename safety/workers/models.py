from django.db import models

# Create your models here.

class Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    image_profile = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField()
    primary_phone = models.CharField(max_length=10)
    secondary_phone = models.CharField(max_length=10)
    address = models.TextField()
from django.db import models

# Create your models here.


# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length=30)
    issued_by = models.CharField(max_length=40)
   
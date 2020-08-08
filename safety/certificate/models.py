from django.db import models
from workers.models import Worker
# Create your models here.


# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length=30)
    issued_by = models.CharField(max_length=40)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
   
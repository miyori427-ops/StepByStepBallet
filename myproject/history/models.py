from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

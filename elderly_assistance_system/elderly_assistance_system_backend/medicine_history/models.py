from django.db import models

# Create your models here.
class MedicineHistory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField() 
    time = models.TimeField()
    consumed = models.BooleanField()
    time_of_consumption = models.TimeField()

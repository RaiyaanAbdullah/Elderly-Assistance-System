from django.db import models

# Create your models here.
class medicine(models.Model):
	name				=models.CharField(max_length=120)
	start_date 			= models.CharField(max_length=120)
	consumption_counter = models.CharField(max_length=120)
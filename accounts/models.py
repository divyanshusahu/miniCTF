from django.db import models

# Create your models here.

class teams(models.Model) :
	teamname = models.CharField(max_length=250, primary_key=True)
	email = models.EmailField(max_length=250, unique=True)
	password = models.CharField(max_length=250)
	job = models.CharField(max_length=100)
	company = models.CharField(max_length=250)
from django.db import models

# Create your models here.

class Teams(models.Model) :
	teamname = models.CharField(max_length=250, primary_key=True)
	email = models.EmailField(max_length=250, unique=True)
	job = models.CharField(max_length=100, null=True, default="")
	company = models.CharField(max_length=250, null=True, default="")
	points = models.IntegerField(default=0)
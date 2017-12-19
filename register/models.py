from django.db import models

# Create your models here.

class Users(models.Model) :
	teamname = models.CharField(max_length=200, primary_key=True)
	email = models.EmailField(max_length=200, unique=True)
	password = models.CharField(max_length=250)
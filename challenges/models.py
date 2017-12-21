from django.db import models

# Create your models here.

class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True)
	category = models.CharField(max_length=100)
	description = models.CharField(max_length=1000, null=True)
	points = models.IntegerField()
	#files = models.FileField(null=True, upload_to='uploads/')
	flag = models.CharField(max_length=500)
	author = models.CharField(max_length=250)
	#solved_by = models.CharField(max_length=null=True)
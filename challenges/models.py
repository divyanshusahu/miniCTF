from django.db import models

# Create your models here.
class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True)
	points = models.IntegerField()
	category = models.CharField(max_length=100)
	description = models.CharField(max_length=1000, null=True)
	files = models.FileField(null=True)
	flag = models.CharField(max_length=500)
	author = models.CharField(max_length=250)
	#solved_by = models.IntegerField(null=True)
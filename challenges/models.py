from django.db import models

# Create your models here.

def get_upload_path(instance, filename) :
	return 'uploads/challenges_{0}/{1}'.format(instance.name, filename)

class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True, null=True)
	category = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=1000, blank=True, default="", null=True)
	points = models.IntegerField(null=True)
	files = models.FileField(null=True, blank=True, upload_to=get_upload_path)
	flag = models.CharField(max_length=500, null=True)
	author = models.CharField(max_length=250, null=True)
	#solved_by = models.CharField()
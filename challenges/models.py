from django.db import models
import hashlib

# Create your models here.

def get_upload_path(instance, filename) :
	return 'uploads/'+instance.category+'/challenges_{0}/{1}'.format(hashlib.md5(instance.name.encode('utf-8')).hexdigest(), filename)

class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True, null=True)
	category = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=1000, blank=True, default="", null=True)
	points = models.IntegerField(null=True)
	file = models.FileField(null=True, blank=True, upload_to=get_upload_path)
	flag = models.CharField(max_length=500, null=True)
	author = models.CharField(max_length=250, null=True)
	#solved_by = models.CharField()
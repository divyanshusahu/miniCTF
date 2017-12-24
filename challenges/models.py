from django.db import models
import hashlib

# Create your models here.

def get_upload_path(instance, filename) :
	return instance.category+'/challenges_{0}/{1}'.format(hashlib.md5(instance.name.encode('utf-8')).hexdigest(), filename)

class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True)
	challenge_id = models.CharField(max_length=300, primary_key=True)
	category = models.CharField(max_length=100)
	description = models.CharField(max_length=1000, blank=True, default="")
	points = models.IntegerField()
	file = models.FileField(null=True, blank=True, upload_to=get_upload_path)
	flag = models.CharField(max_length=500)
	author = models.CharField(max_length=250)

class ChallengesSolvedBy(models.Model) :
	challenge_id =  models.CharField(max_length=250)
	user_name = models.CharField(max_length=250)
	points = models.IntegerField()
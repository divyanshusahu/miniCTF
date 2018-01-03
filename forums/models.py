from django.db import models

# Create your models here.

def get_upload_path_question(instance, filename) :
	return 'forums/'+instance.topic+'/question/'

def get_upload_path_answer(instance, filename) :
	return 'forums/'+instance.answer_on+'/answers/'

class Threads(models.Model) :
	topic = models.CharField(max_length=500, unique=True)
	posted_on = models.DateTimeField()
	posted_by = models.ForeignKey('accounts.Teams', on_delete=models.CASCADE)
	description = models.TextField()
	files = models.FileField(upload_to=get_upload_path_question, blank=True, null=True)
	score = models.IntegerField(default=0)

class Answers(models.Model) :
	answer_on = models.ForeignKey('Threads', on_delete=models.CASCADE)
	answer_by = models.ForeignKey('accounts.Teams', on_delete=models.CASCADE)
	answer_date = models.DateTimeField()
	answer = models.TextField(default="")
	answer_files = models.FileField(upload_to=get_upload_path_answer, blank=True, null=True)
	score = models.IntegerField(default=0)
from django import forms
from . import models

class AddThreadForm(forms.ModelForm) :
	topic = forms.CharField(max_length=500, label="Topic")
	description = forms.CharField(label="Description")
	files = forms.FileField(required=False, label="Files(if any)")

	class Meta :
		model = models.Threads
		fields = ["topic", "description", "files"]

class AddAnswerForm(forms.ModelForm) :
	answer = forms.CharField(label="Answer")
	answer_files = forms.FileField(required=False, label="Files(if any)")

	class Meta :
		model = models.Answers
		fields = ["answer", "answer_files"]
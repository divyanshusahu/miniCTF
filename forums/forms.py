from django import forms
from . import models

class AddThreadForm(forms.ModelForm) :
	topic = forms.CharField(max_length=500, label="Topic")
	description = forms.CharField(label="Description")
	files = forms.FileField(required=False, label="Files(if any)")

	class Meta :
		model = models.Threads
		fields = ["topic", "description", "files"]
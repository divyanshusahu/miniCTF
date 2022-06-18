from django import forms
from . import models

category_list = [
	('Cryptography','Cryptography'),
	('Forensics','Forensics'),
	('Pwning','Pwning'),
	('Reverse Engineering','Reverse Engineering'),
	('Stegnography','Stegnography'),
	('Web','Web')
]

class AddChallengeForm(forms.ModelForm) :
	name = forms.CharField(max_length=250, label="Challenge Name *", widget=forms.TextInput(attrs={'placeholder':'Challenge Name','class':'form-control'}))
	category = forms.CharField(widget=forms.Select(choices=category_list, attrs={'class':'form-control'}), label="Challenge Category *")
	description = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder':'Challenge Description', 'class':'form-control','required':'false'}), label="Challenge Description *", required=False)
	points = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Challenge Points *")
	file = forms.FileField(label="Challenge Files (if any)", required=False)
	flag = forms.CharField(max_length=500, label="Challenge Flag *", widget=forms.TextInput(attrs={'placeholder':'Challenge Flag','class':'form-control'}))
	author = forms.CharField(max_length=250, label="Challenge Author *", widget=forms.TextInput(attrs={'placeholder':'Challenge Author','class':'form-control'}))
	#solved_by = forms.CharField(max_length=250)

	class Meta :
		model = models.Challenges
		fields = ["name","category","description","points","file","flag","author"]
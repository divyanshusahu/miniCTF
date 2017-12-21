from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models
from django.http import HttpResponseRedirect

class RegisterForm(forms.ModelForm) :
	teamname = forms.CharField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Name','class':'form-control'}))
	email = forms.EmailField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Email','class':'form-control', 'type':'email'}))
	password = forms.CharField(max_length=250, min_length=8, label="", widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control','type':'password'}))

	class Meta :
		model = models.Teams
		fields = ["teamname","email"]

class LoginForm(AuthenticationForm) :
	username = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'placeholder':'Team Name','class':'form-control'}))
	password = forms.CharField(max_length=250, min_length=8, label="", widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control','type':'password'}))

class UpdateTeamDetails(forms.ModelForm) :
	#teamname = forms.CharField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Name','class':'form-control'}))
	#email = forms.EmailField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Email','class':'form-control', 'type':'email'}))
	job = forms.CharField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Job','class':'form-control'}))
	company = forms.CharField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Company','class':'form-control'}))

	class Meta :
		model = models.Teams
		fields = ["job","company"]
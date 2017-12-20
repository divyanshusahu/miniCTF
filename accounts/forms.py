from django import forms

class RegisterForm(forms.Form) :
	teamname = forms.CharField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Name','class':'form-control'}))
	email = forms.EmailField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Email','class':'form-control', 'type':'email'}))
	password = forms.CharField(max_length=250, min_length=8, label="", widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control','type':'password'}))

class LoginForm(forms.Form) :
	teamname = forms.CharField(max_length=250, label="", widget=forms.TextInput(attrs={'placeholder':'Team Name','class':'form-control'}))
	password = forms.CharField(max_length=250, min_length=8, label="", widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control','type':'password'}))
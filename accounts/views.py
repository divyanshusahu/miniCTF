from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from . import models

# Create your views here.

def redirect(request) :
	return HttpResponseRedirect("login/")

def login(request) :

	if request.method == 'POST' :
		form = forms.LoginForm(request.POST)
		if form.is_valid() :
			return HttpResponseRedirect('/challenges/')
	else :
		form = forms.LoginForm()
	
	return render(request, 'login/login.html', {'form':form})

def register(request) :
	
	if request.method == 'POST' :
		form = forms.RegisterForm(request.POST)
		if form.is_valid() :
			teamname = request.POST['teamname']
			email = request.POST['email']
			password = request.POST['password']
			print(teamname, email, password)
			return HttpResponseRedirect('/challenges/')
	else :
		form = forms.RegisterForm()
	
	return render(request, 'register/register.html', {'form':form})
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from . import models
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def redirect(request) :
	return HttpResponseRedirect("login/")

def register(request) :

	if request.user.is_authenticated :
		return HttpResponseRedirect("/accounts/profile")

	if request.method == 'POST' :
		form = forms.RegisterForm(request.POST)
		if form.is_valid() :
			form.save()
			teamname = form.cleaned_data.get("teamname")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			try :
				user = User.objects.get(username=uservalue)
				error = {'form':form, 'error':'Team name already taken'}
				return render(request, 'register/register.html', error)
			except :
				user = User.objects.create_user(username=teamname, password=password, email=email)
				user.save()
				login(request, user)
				return HttpResponseRedirect('/challenges/')
	else :
		form = forms.RegisterForm()
	
	return render(request, 'register/register.html', {'form':form})

@login_required(login_url="/accounts/login/")
def profile(request) :

	if request.method == 'POST' :
		form = forms.UpdateTeamDetails(request.POST)
		#if form.is_valid() :
	else :
		form = forms.UpdateTeamDetails()
		
	return render(request, 'profile/profile.html', {'form':form})
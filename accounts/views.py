from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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
	if request.user.is_superuser :
		return HttpResponseRedirect("/teams/")
	#print(models.Teams.objects.filter(teamname=request.user))
	j = models.Teams.objects.get(teamname=request.user).job
	c = models.Teams.objects.get(teamname=request.user).company
	form_data = {'job':j, 'company':c}
	if request.method == 'POST' :
		form = forms.UpdateTeamDetails(request.POST)
		success = 0
		if form.is_valid() :
			job = form.cleaned_data.get("job")
			company = form.cleaned_data.get("company")
			team = request.user
			models.Teams.objects.filter(teamname=team).update(job=job, company=company)
			success = 1
			return render(request, 'profile/profile.html', {'form':form, 'success':success})
	else :
		form = forms.UpdateTeamDetails(initial=form_data)
		
	return render(request, 'profile/profile.html', {'form':form})

@login_required(login_url="/accounts/login/")
def team_view(request) :
	if request.user.is_superuser :
		return HttpResponseRedirect("/teams/")
	team_details = models.Teams.objects.get(teamname=request.user)
	return render(request, 'team/team.html',{'team_details':team_details})
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from . import models
from django.contrib.auth import authenticate, login , update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from challenges.models import ChallengesSolvedBy
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

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
	solved_challenges = ChallengesSolvedBy.objects.filter(user_name=request.user)
	return render(request, 'team/team.html',{'team_details':team_details,'solved_challenges':solved_challenges})

@login_required(login_url="/accounts/login/")
def update_password(request) :
	if request.method == 'POST' :
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid() :
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated!')
			return HttpResponseRedirect("/challenges/")
		else :
			messages.error(request, 'Please correct the error below.')
	else :
		form = PasswordChangeForm(request.user)
	
	return render(request, 'profile/change-password.html',{'form':form})

@login_required(login_url="/accounts/login/")
def every_team(request, pk) :
	requested_team = pk
	try :
		requested_team_details = models.Teams.objects.get(teamname=requested_team)
		solved_team_challenges = ChallengesSolvedBy.objects.filter(user_name=requested_team)
		return render(request, 'team/team.html', {'team_details':requested_team_details,'solved_challenges':solved_team_challenges})
	except :
		return HttpResponseRedirect("/accounts/team/")
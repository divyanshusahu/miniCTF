from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required(login_url="/accounts/login")
def index(request) :
	return render(request, 'challenges.html')

@login_required(login_url="/accounts/login")
def addchallenges(request) :
	
	if request.user.is_superuser :
		if request.method == 'POST' :
			form = forms.AddChallengeForm(request.POST)
		else :
			form = forms.AddChallengeForm()

		return render(request, 'addchallenges.html', {'form':form})
	
	else :
		return redirect("/")
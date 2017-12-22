from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse
from . import models

# Create your views here.

@login_required(login_url="/accounts/login")
def index(request) :
	return render(request, 'challenges.html')

@login_required(login_url="/accounts/login")
def addchallenges(request) :
	
	if request.user.is_superuser :
		if request.method == 'POST' :
			form = forms.AddChallengeForm(request.POST, request.FILES)
			if form.is_valid() :
				i = models.Challenges(files=request.FILES['file'], name=request.POST['name'], category=request.POST['category'], description=request.POST['description'], points=request.POST['points'], flag=request.POST['flag'], author=request.POST['author'])
				i.save()
				return HttpResponse("Challenge added<br><a href='/challenges/'>challenges</a>")
		else :
			form = forms.AddChallengeForm()

		return render(request, 'addchallenges.html', {'form':form})
	
	else :
		return redirect("/")
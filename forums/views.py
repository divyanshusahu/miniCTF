from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms, models
from accounts.models import Teams
import datetime

# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request) :
	success = 0
	if request.method == 'POST' :
		form = forms.AddThreadForm(request.POST, request.FILES)
		if form.is_valid() :
			success = 1
			if request.FILES :
				i = models.Threads(topic=request.POST['topic'],
					posted_on=datetime.datetime.now(),
					description=request.POST['description'],
					posted_by=Teams.objects.get(teamname=request.user),
					files=request.FILES['files'])
				i.save()
			else :
				i = models.Threads(topic=request.POST['topic'],
					posted_on=datetime.datetime.now(),
					posted_by=Teams.objects.get(teamname=request.user),
					description=request.POST['description'])
				i.save()
	else :
		form = forms.AddThreadForm()

	all_threads = models.Threads.objects.order_by("-posted_on")
	print(all_threads)
	return render(request, 'index.html', {'form':form,'success':success,'all_threads':all_threads})

@login_required(login_url="/accounts/login/")
def thread(request, pk) :
	return render(request, 'index.html')
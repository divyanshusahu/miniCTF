from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms, models
from accounts.models import Teams
import datetime

# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request) :
	if request.method == 'POST' :
		form = forms.AddThreadForm(request.POST, request.FILES)
		if form.is_valid() :
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
	return render(request, 'index.html', {'form':form, 'all_threads':all_threads})

@login_required(login_url="/accounts/login/")
def thread(request, pk) :
	thread = models.Threads.objects.get(id=pk)

	if request.method == 'POST' :
		form = forms.AddAnswerForm(request.POST, request.FILES)
		if form.is_valid() :
			if request.FILES :
				i = models.Answers(answer_on=thread,
					answer_by=Teams.objects.get(teamname=request.user),
					answer=request.POST['answer'],
					answer_files=request.FILES['answer_files'],
					answer_date=datetime.datetime.now())
				i.save()
			else :
				i = models.Answers(answer_on=thread,
					answer_by=Teams.objects.get(teamname=request.user),
					answer=request.POST['answer'],
					answer_date=datetime.datetime.now()
					)
				i.save()
	else :
		form = forms.AddAnswerForm()

	answers = models.Answers.objects.filter(answer_on_id=pk)

	return render(request, 'thread.html',{'form':form, 'answers':answers, 'thread': thread})
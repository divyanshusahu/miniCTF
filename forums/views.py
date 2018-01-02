from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request) :
	if request.method == 'POST' :
		form = forms.AddThreadForm(request.POST, request.FILES)
	else :
		form = forms.AddThreadForm()
	return render(request, 'index.html', {'form':form})
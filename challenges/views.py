from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login")
def index(request) :
	return render(request, 'challenges.html')
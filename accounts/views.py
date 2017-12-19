from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def redirect(request) :
	return HttpResponseRedirect("login/")

def login(request) :
	return render(request, 'login/login.html')

def register(request) :
	return render(request, 'register/register.html')
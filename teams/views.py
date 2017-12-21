from django.shortcuts import render
from accounts.models import Teams

# Create your views here.

def teams(request) :
	obj = Teams.objects.all()
	return render(request, 'teams.html', {'obj':obj})
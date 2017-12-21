from django.shortcuts import render
from accounts.models import Teams

# Create your views here.

def score(request) :
	obj = Teams.objects.all()
	return render(request, 'scoreboard.html', {'obj':obj})
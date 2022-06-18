from django.shortcuts import render
from accounts.models import Teams

# Create your views here.

def teams(request) :
	teams_list = Teams.objects.all()
	return render(request, 'teams.html', {'teams_list':teams_list})
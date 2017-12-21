from django.shortcuts import render
from accounts.models import Teams

# Create your views here.

def score(request) :
	teams_list = Teams.objects.order_by("-points")
	return render(request, 'scoreboard.html', {'teams_list':teams_list})
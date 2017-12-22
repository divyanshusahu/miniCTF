from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse
from . import models

# Create your views here.

class PassInsideView() :
	name = ''
	category = ''
	description = ''
	points = ''
	file = ''
	author = ''
	def __init__(self, name, category, description, points, file, author) :
		self.name = name
		self.category = category
		self.description = description
		self.points = points
		self.file = file
		self.author = author

@login_required(login_url="/accounts/login")
def index(request) :
	challenge = models.Challenges.objects.order_by("points")
	challenge_info_stego_object = []
	challenge_info_for_object = []
	challenge_info_re_object = []
	challenge_info_pwn_object = []
	challenge_info_web_object = []
	challenge_info_crypto_object = []
	for c in challenge :
		if c.category == 'Stegnography' :
			s = PassInsideView(c.name, c.category, c.description, c.points, c.file, c.author)
			challenge_info_stego_object.append(s)
		elif c.category == 'Reverse Engineering' :
			re = PassInsideView(c.name, c.category, c.description, c.points, c.file, c.author)
			challenge_info_re_object.append(re)
		elif c.category == 'Forensics' :
			f = PassInsideView(c.name, c.category, c.description, c.points, c.file, c.author)
			challenge_info_for_object.append(f)
		elif c.category == 'Pwning' :
			p = PassInsideView(c.name, c.category, c.description, c.points, c.file, c.author)
			challenge_info_pwn_object.append(p)
		elif c.category == 'Web' :
			w = PassInsideView(c.name, c.category, c.description, c.points, c.file, c.author)
			challenge_info_web_object.append(w)
		elif c.category == 'Cryptography' :
			cy = PassInsideView(c.name, c.category, c.description, c.points, c.file, c.author)
			challenge_info_crypto_object.append(cy)

	return render(request, 'challenges.html',{'data_stego':challenge_info_stego_object,'data_for':challenge_info_for_object,'data_re':challenge_info_re_object,'data_pwn':challenge_info_pwn_object,'data_web':challenge_info_web_object,'data_crypto':challenge_info_crypto_object})

@login_required(login_url="/accounts/login")
def addchallenges(request) :
	
	if request.user.is_superuser :
		if request.method == 'POST' :
			form = forms.AddChallengeForm(request.POST, request.FILES)
			if form.is_valid() :
				if request.FILES :
					i = models.Challenges(file=request.FILES['file'], name=request.POST['name'], category=request.POST['category'], description=request.POST['description'], points=request.POST['points'], flag=request.POST['flag'], author=request.POST['author'])
					i.save()
				else :
					form.save()
				return HttpResponse("Challenge added<br><a href='/challenges/'>challenges</a>")
		else :
			form = forms.AddChallengeForm()

		return render(request, 'addchallenges.html', {'form':form})
	
	else :
		return redirect("/")
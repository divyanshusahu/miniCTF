from django.urls import path, include, re_path
from . import views as manual_views
from django.contrib.auth import views
from . import forms

urlpatterns = [
	path('', manual_views.redirect, name="redirect"),
	path('login/', views.login, {'template_name':'login/login.html','authentication_form':forms.LoginForm}),
	path('logout/', views.logout, {'next_page':'/'}, name="logout"),
	path('register/', manual_views.register, name="register"),
	path('profile/', manual_views.profile, name="profile"),
	path('team/', manual_views.team_view, name="team_view"),
	re_path('team/(?P<pk>.+)', manual_views.every_team, name="every_team"),
	path('profile/changepassword/', manual_views.update_password, name="update_password")
]
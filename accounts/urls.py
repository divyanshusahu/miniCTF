from django.urls import path, include
from . import views as manual_views
from django.contrib.auth import views
from . import forms

urlpatterns = [
	path('', manual_views.redirect, name="redirect"),
	path('login/', views.login, {'template_name':'login/login.html','authentication_form':forms.LoginForm}),
	path('logout', views.logout, {'next_page':'/'}, name="logout"),
	path('register/', manual_views.register, name="register"),
]
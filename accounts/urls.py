from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.redirect, name="redirect"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register")
]
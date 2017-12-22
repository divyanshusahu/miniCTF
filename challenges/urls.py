from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('admin/add', views.addchallenges, name="add")
]
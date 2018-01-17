from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('post/<slug:the_slug>', views.read, name="single")
]

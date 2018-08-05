from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('post/<slug:the_slug>', views.read, name="single"),
	path('post/category/<str:the_category>', views.category, name="category"),
	path('post/<int:the_year>', views.year_archive, name="year"),
	path('post/<int:the_year>/<str:the_month>', views.month_archive, name="month")
] 

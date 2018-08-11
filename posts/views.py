from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
# Create your views here.

five = Post.objects.filter(published=True).order_by("-date_published").all()[:3]

def index(request):
	posts = Post.objects.filter(published=True).order_by("-date_published").all()[:5]
	context = {'posts' : posts, 'five' : five}
	return render(request, 'posts/index.html', context)

def read(request, the_slug):
	post = Post.objects.filter(published=True, slug=the_slug).first()
	context = {'post' : post, 'five' : five}
	return render(request, 'posts/single.html', context)
	
def category(request, the_category):
	posts = Post.objects.filter(published=True, category=Category.objects.get(name=the_category)).all()
	context = {'posts' : posts}
	return render(request, 'posts/category.html', context)
	
def month_archive(request, the_month, the_year):
	post = Post.objects.filter(date_published__month=the_month).filter(date_published__year=the_year).all()
	context = {'post' : post}
	return render(request, 'posts/date.html', context)	
	
def year_archive(request, the_year):
	post = Post.objects.filter(date_published__year=the_year).all()
	context = {'post' : post}
	return render(request, 'posts/date.html', context)



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
	posts = Post.objects.filter(published=True).order_by("-date_published").all()
	
	context = {'posts' : posts}
	return render(request, 'posts/index.html', context)

def read(request, the_slug):
	post = Post.objects.filter(published=True, slug=the_slug).first()
	context = {'post' : post}
	return render(request, 'posts/single.html', context)
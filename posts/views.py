from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
	posts = Post.objects.order_by("-date_published").all()
	
	context = {'posts' : posts}
	return render(request, 'posts/index.html', context)

def post(request):
	return HttpResponse("This is the posts")
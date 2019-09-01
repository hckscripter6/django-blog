from django.shortcuts import render
from posts.views import Post


def about(request):
	return render(request, 'blog/about.html')
	
def contact(request):
	return render(request, 'blog/contact.html')
	
def posts(request):
	post = Post.objects.all()[:5]
	return render(request, 'blog/base.html')
	
def listPosts(request):
	posts = Post.objects.filter(published=True).order_by("-date_published").all()
	context = {'posts' : posts}
	return render(request, 'blog/posts.html')
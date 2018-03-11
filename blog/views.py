from django.shortcuts import render
from posts.views import Post

five = Post.objects.filter(published=True).order_by("-date_published").all()[:5]

def about(request):
	context = {'five' : five}
	return render(request, 'blog/about.html', context)
	
def contact(request):
	context = {'five' : five}
	return render(request, 'blog/contact.html', context)
	
def posts(request):
	post = Post.objects.all()[:5]
	context = {'post' : post, 'five' : five}
	return render(request, 'blog/base.html', context)
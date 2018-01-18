from django.shortcuts import render

def about(request):
	return render(request, 'blog/about.html')
	
def contact(request):
	return render(request, 'blog/contact.html')
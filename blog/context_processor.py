from posts.models import Post

def sidebar_posts(request):
    return {
        'sidebar_posts': Post.objects.filter(published=True).order_by("-date_published").all()[:3]
    }

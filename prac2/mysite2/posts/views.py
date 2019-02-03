from django.shortcuts import render, get_object_or_404
from .models import Post

def posts_list(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts':all_posts
    }
    return render(request, "posts/posts_list.html", context)

def posts_detail(request, slug):
    unique_post = get_object_or_404(Post, slug=slug) # Here if slug=post then the url pattern would have been slug:post instead of slug:slug
    context = {
        'post' : unique_post
    }
    return render(request, "posts/posts_detail.html", context)
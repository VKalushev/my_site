from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Post,Author,Tag

# Create your views here.
def starting_page(request):
    latests_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=lambda post: post['date'])
    # latests_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "all_posts": latests_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_details(request,slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    print("Post:",post)
    return render(request, "blog/post-detail.html",{
        "post" : post,
        "tags" : post.captions.all()
    })
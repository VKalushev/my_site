from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse

from django.http import HttpResponseRedirect


from .forms import CommentForm
from .models import Comment

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "all_posts"

    def get_queryset(self):
        return super().get_queryset().order_by("-date")[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        later_list = self.request.session.get('later_list')
        all_later_posts = []

        for slug in later_list:
            all_later_posts.append(Post.objects.get(slug=slug))

        context["all_later_posts"] = all_later_posts
        return context


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"

    def get_queryset(self):
        return super().get_queryset().order_by("-date")


class SinglePost(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        later_list = request.session.get('later_list')

        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.captions.all(),
            "form": CommentForm(),
            'later_list': later_list,
            'comments': post.comments.all()[::-1]
        })

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            url = reverse('post_detail_page', kwargs={'slug': post.slug})
            return HttpResponseRedirect(url)

        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.captions.all(),
            "form": form,
            'comments': post.comments.all()[::-1]
        })


class ReadLaterView(View):
    def post(self, request, slug):
        post_slug = request.POST['post_slug']

        if "later_list" not in request.session:
            request.session['later_list'] = []

        later_list = request.session['later_list']

        if post_slug not in later_list:
            later_list.append(post_slug)
        else:
            later_list.remove(post_slug)

        request.session['later_list'] = later_list

        return HttpResponseRedirect("/posts/"+post_slug)

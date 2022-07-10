from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Category, Post


class MainpageView(ListView):
    template_name = "main-page/mainpage.html"

    def get_context(self):
        posts= Post.objects.all()
        context = {
            'posts':posts,
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        context = {'post': post}
        return render(request, 'post-page/post-page.html', context)


class AboutView(ListView):
    template_name = "about-page/about.html"

    def get_context(self):
        categories=Category.objects.all()
        latest_posts=Post.objects.all()[:2]
        context = {
            'categories': categories,
            'latest_posts': latest_posts
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from core.models import Category, Post


def contact_view(request):
    form = ContactForm()
    categories = Category.objects.all()
    latest_posts = Post.objects.all()[:2]
    context = {
        'form': form,
        'categories': categories,
        'latest_posts': latest_posts,

    }
    return render(request, 'contact/contact.html', context)

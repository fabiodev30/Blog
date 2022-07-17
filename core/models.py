from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(published=True)


class Post(models.Model):
    objects=PostManager()
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(blank=True, null=True,)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


def get_latest_posts():
    return Post.objects.published().order_by("-created_on")[:10]


def get_popular_posts() -> list[Post]:
    return Post.objects.published().order_by("-views")[:10]

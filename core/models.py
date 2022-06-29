from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Nopublish"),
    (1,"Publish")
)

class Category(models.Model):
    name=models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
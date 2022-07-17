from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Category,Post


class StaticHomeSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return ['blog:home']

    def location(self, item):
        return reverse(item)


class StaticSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return [
            'blog:about',
        ]

    def location(self, item):
        return reverse(item)


class PostSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def location(self, item):
        return reverse('blog:post-detail', args=[item.slug])


class CategorySiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def location(self,obj):
        return '/category/%s' % (obj.name)



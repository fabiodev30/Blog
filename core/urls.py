from django.urls import path,include
from .views import AboutView, MainpageView,PostDetailView, SearchResultsView
from django.conf.urls.static import static
from django.conf import settings
from .sitemaps import StaticHomeSiteMap,StaticSiteMap,PostSiteMap,CategorySiteMap
from django.contrib.sitemaps.views import sitemap

app_name = 'blog'


sitemaps = {
    'home':StaticHomeSiteMap,
    'static_pages':StaticSiteMap,
    'post_detail':PostSiteMap,
    'category':CategorySiteMap

}



urlpatterns = [
     path('', MainpageView.as_view(), name='home'),
     path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
     path('about', AboutView.as_view(), name='about'),
     path("search/", SearchResultsView.as_view(), name="search_results"),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
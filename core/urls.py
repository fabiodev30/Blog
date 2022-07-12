from django.urls import path,include
from .views import AboutView, MainpageView,PostDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
     path('', MainpageView.as_view(), name='home'),
     path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
     path('about', AboutView.as_view(), name='about'),
     path("search/", SearchResultsView.as_view(), name="search_results"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.urls import path,include
from .views import MainpageView,PostDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
     path('', MainpageView.as_view(), name='home'),
     path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
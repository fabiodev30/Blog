from django.urls import path,include
from .views import MainpageView,PostDetailView

app_name = 'blog'
urlpatterns = [
     path('', MainpageView.as_view(), name='home'),
     path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
]
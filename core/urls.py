from django.urls import path,include
from .views import MainpageView

urlpatterns = [
     path('', MainpageView.as_view(), name='home'),
]
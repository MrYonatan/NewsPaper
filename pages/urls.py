from django.urls import path
from .views import HomePageVIew

urlpatterns = [
    path('',HomePageVIew.as_view(), name="home")
]

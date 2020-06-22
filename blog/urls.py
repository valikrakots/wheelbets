from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
    path('help', views.help, name='blog-help'),
    path('contacts', views.contacts, name='blog-contacts'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/index', views.contactForm, name='index'),
]

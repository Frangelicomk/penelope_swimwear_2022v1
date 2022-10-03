from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('message_sent/', views.contactForm, name='message_sent'),
]

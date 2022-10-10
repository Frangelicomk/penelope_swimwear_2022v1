from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_subscriber, name='new_subscriber'),
    path('confirm_subscriber/', views.confirm_subscriber, name='confirm'),
    path('delete_subscriber/', views.delete_subscriber, name='delete_subscriber'),
]

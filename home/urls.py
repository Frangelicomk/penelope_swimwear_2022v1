from django.urls import path
from . import views
from .views import contactView, successView

urlpatterns = [
    path('', views.index, name='home'),
    path("", contactView, name="contact"),
    path("", successView, name="success"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contactForm_submit',
         views.contactForm_submit,
         name='contactForm_submit'),
]

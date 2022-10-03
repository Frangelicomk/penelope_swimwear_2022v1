from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import ContactFormEmails
from .forms import ContactForm
# Create your views here.


def index(request):
    """ A view to render/return the index page """

    return render(request, 'home/index.html')

# function to send the form to back-end


def contact(request):
    if request.method == 'POST':
        contactFormEmail = ContactFormEmails(name=request.POST.get('name'), email=request.POST.get(
            'email'), subject=request.POST.get(
            'subject'), message=request.POST.get('message'))
        contactFormEmail.save()

        messages.success(
            request, "Your message has been successfully send! Thank you")
        return HttpResponseRedirect('/')


def contactForm(request):
    """ send email with contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'home/index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'home/index.html', context)

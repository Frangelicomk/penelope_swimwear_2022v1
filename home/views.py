from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import render, redirect
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


def contactForm(request, product_id):
    """ send email with contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            subject = "Contact form message"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'no-reply@penelope_c.com',
                          ['frangelicomk87@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("main:index")

        form = ContactForm()
        return render(request, "/", {'form': form})

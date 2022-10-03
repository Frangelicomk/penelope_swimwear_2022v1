from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def index(request):
    """ A view to render/return the index page """

    return render(request, 'home/index.html')

# function to send the form to back-end


def contactForm(request):
    """ send email with contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, '/')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'home/index.html', context)

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


def index(request):
    """ A view to render/return the index page """

    return render(request, 'home/index.html')

# function to send the form to back-end


def contactform_submit(request):
    """ send email with contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["name"]}: \
                 {form.cleaned_data["subject"]}'
            email_message = f'Message: {form.cleaned_data["message"]}, \
                 Email: {form.cleaned_data["email"]}'
            send_mail(email_subject, email_message,
                      settings.CONTACT_EMAIL, settings.ADMIN_EMAILS,)
            messages.success(request, 'Thank you for your message')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Failed to send message. \
                    Please ensure the form is valid.')
    else:
        form = ContactForm()
        return render(request, 'home/index.html')


def error_page_404(request, exception):
    """ render a 404 custom template in the browser """
    return render(request, '404.html')

import random
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm


# Create your views here.


def random_digits():
    """
    generate random degits for subscriber confirmation number
    """
    return "%0.12d" % random.randint(0, 999999999999)


@csrf_exempt
def new_subscriber(request):
    """
    New subscriber confirmation email and view
    """
    if request.method == "POST":
        email = request.POST.get('email')
        confirmation_number = random_digits()
        Subscriber.objects.create(
            email=email, confirmation_number=confirmation_number)
        email_subject = 'Newsletter Confirmation'
        email_message = (
            'Thank you for signing up for my email newsletter! Please complete \
                 the process by \
                    <a href="{}/confirm_subscriber/?email={}&confirmation_number={}"> \
                        clicking here to confirm your registration.'.format(
                            request.build_absolute_uri(
                                '/confirm_subscriber/'), email, confirmation_number))
        send_mail(
            email_subject,
            email_message,
            settings.CONTACT_EMAIL,
            [email, ]
            )
        messages.success(
            request, f'A confirmation emai has been send to {email}')
        return render(request, 'home/index.html', {
            'email': email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'home/index.html', {'form': SubscriberForm()})


def confirm_subscriber(request):
    """
    confirmation email send with a link
    """
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.confirmation_number == request.GET['confirmation_number']:
        sub.confirmed = True
        sub.save()
        return render(request, 'home/index.html', {
            'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'home/index.html', {
            'email': sub.email, 'action': 'denied'})


def delete_subscriber(request):
    """
    Unsubscribe
    """
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.confirmation_number == request.GET['confirmation_number']:
        sub.delete()
        return render(request, 'home/index.html', {
            'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'home/index.html', {
            'email': sub.email, 'action': 'denied'})

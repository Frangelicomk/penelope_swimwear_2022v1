from django.conf import settings
from django.db import models
from django.core.mail import send_mail

# Create your models here.


class Subscriber(models.Model):
    """
    subscirber details model.
    """
    email = models.EmailField(unique=True)
    confirmation_number = models.CharField(max_length=45)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + "(" + (
            "not" if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    """
    Newsletter Model to handle newsletter content
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='uploaded_newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")


    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        for sub in subscribers:
            email_subject = 'Newsletter Confirmation'
            email_message = contents + (
                        '<br><a href="{}/delete/?email={}&confirmation_number={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.confirmation_number)
            send_mail(
                email_subject,
                email_message,
                settings.CONTACT_EMAIL,
                [sub.email, ]
                )

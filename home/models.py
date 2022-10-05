from django.db import models

# Create your models here.


class ContactFormEmails(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Form Emails'
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

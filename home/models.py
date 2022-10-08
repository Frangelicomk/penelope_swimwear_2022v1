from django.db import models

# Create your models here.


class ContactFormEmails(models.Model):
    """
    This Model displays the arguments we want to retrieve from the user
    """
    class Meta:
        """
        Meta Class so I can change the name of the initial class in admin panel
        """
        verbose_name_plural = 'Contact Form Emails'
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)

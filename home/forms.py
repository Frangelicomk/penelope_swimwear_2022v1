from django import forms
from .models import ContactFormEmails


class ContactForm(forms.ModelForm):
    """ A custom contact form """
    class Meta:
        """ fields to render for our form """
        model = ContactFormEmails
        fields = '__all__'

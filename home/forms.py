from django import forms
from .models import ContactFormEmails


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormEmails
        fields = '__all__'


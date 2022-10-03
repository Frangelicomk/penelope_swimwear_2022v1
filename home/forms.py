from django import forms
from .models import ContactFormEmails


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormEmails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

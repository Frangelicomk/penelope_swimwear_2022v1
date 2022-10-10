from django import forms


class SubscriberForm(forms.Form):
    """
    News letter form located in the landing page
    """
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(
                                attrs={'class': 'form-control'}))

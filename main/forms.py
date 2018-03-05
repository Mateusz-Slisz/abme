from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

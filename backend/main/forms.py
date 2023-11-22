from django import forms
from .models import Page, ContactUs
from django.utils.translation import gettext_lazy as _


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        required=True, label="Your Name", widget=forms.TextInput(
            attrs={
                "class": "form-control border-dark border-opacity-25",
                "id": "name",
                "placeholder": "enter your name"
            }
        )
    )
    email = forms.CharField(
        required=True, label="Email", widget=forms.EmailInput(
            attrs={
                "class": "form-control border-dark border-opacity-25",
                "id": "email",
                "placeholder": "example@gmail.com"
            }
        )
    )
    message = forms.CharField(
        required=True, label="Message", max_length=600, widget=forms.Textarea(
            attrs={
                "class": "form-control border-dark border-opacity-25",
                "id": "message",
                "placeholder": "enter your message..."
            }
        )
    )

    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]

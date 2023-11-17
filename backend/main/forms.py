from django import forms
from .models import Page
from django.utils.translation import gettext_lazy as _


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

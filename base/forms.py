from .models import Subscribe
from django.forms import ModelForm
from django import forms

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
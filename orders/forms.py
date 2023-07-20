from cProfile import label

from django import forms
from django.core.validators import RegexValidator

from .models import Order


class OrderCreateForm(forms.ModelForm):
    phone = forms.CharField(
        label='Телефон (+375XX XXX-XX-XX)',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'city', 'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderCreateAuthUser(forms.Form):
    phoneNumberRegex = RegexValidator(regex=r'^\+375\d{2}\s\d{3}-\d{2}-\d{2}$')
    phone = forms.CharField(
        max_length=16, widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        label='Телефон (+375XX XXX-XX-XX)',
        validators=[phoneNumberRegex]
    )
    city = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        label='Город'
    )
    address = forms.CharField(
        max_length=250, widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        label='Адрес'
    )

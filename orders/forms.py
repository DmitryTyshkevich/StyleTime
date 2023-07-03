from cProfile import label

from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'city', 'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderCreateAuthUser(forms.Form):
    phone = forms.CharField(
        max_length=13, widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        label='Телефон'
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

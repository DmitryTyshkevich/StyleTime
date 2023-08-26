from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Форма для изменения изображения в личном кабинете"""

    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': '',
        }


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        ]
        labels = {
            'username': 'Логин',
        }

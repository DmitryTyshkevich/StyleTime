from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True, verbose_name="Аватар"
    )

    def __str__(self):
        return f"{self.user} Profile"
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

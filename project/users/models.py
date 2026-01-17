from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Дополнительные поля
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


    def __str__(self):
        return self.username


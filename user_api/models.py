# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """CustomUserModel."""
    user_profile = models.ImageField(null=True, blank=True, upload_to='profile_pic/')
    address = models.TextField(null=True, blank=True)
    contact_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

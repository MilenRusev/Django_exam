from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(unique=True, default='', max_length=10)
    email = models.EmailField(max_length=50, default='', blank=False, unique=True)
    first_name = models.CharField(max_length=30, default='', blank=False)
    last_name = models.CharField(max_length=30, default='', blank=False)
    phone = models.CharField(max_length=10, default='')
    age = models.PositiveIntegerField(default=0, blank=True)
    password = models.CharField(max_length=15, default='')

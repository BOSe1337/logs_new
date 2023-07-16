from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    hostname = models.CharField(max_length=255, verbose_name="hostname")
    ipaddress = models.CharField(max_length=255, verbose_name="ipaddress")
    type_of_login = models.CharField(max_length=255, verbose_name="type")
    time_login = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')


class BadUser(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="hostname")
    ipaddress = models.CharField(max_length=255, verbose_name="ipaddress")
    type_of_login = models.CharField(max_length=255, verbose_name="type")
    time_login = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    username = models.CharField(max_length=255, verbose_name="username")

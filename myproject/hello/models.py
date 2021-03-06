from django.db import models
from django.contrib.auth.models import AbstractUser


class Greeting(models.Model):
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date = models.DateTimeField()
    owner = models.ForeignKey('User', null=True)

    class Meta:
        db_table = 'Greeting'


class User(AbstractUser):
    class Meta:
        db_table = 'User'
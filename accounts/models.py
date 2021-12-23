from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(primary_key=True)
    username = models.CharField(blank=True, null=True, max_length=50)
    password = models.CharField(blank=True, null=True, max_length=50)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True

    def __str__(self):
        return self.email

class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=40)


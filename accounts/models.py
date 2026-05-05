from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150,blank=True, null=True)
    last_name = models.CharField(max_length=150,blank=True, null=True)
    role_choice = [
        ('admin','Admin'),
        ('agent', 'Agent')
    ]

    role = models.CharField(max_length=20, choices=role_choice, default='agent')

    def __str__(self):
        return self.email
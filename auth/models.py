from django.db import models
from django.core.validators import EmailValidator

class User(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

from random import randint
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    birthday = models.DateField(default=False)
    random_number = models.IntegerField(randint(1,100))

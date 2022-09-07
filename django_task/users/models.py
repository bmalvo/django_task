from random import randint
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# CustomUser = get_user_model()
# queryset = get_user_model().objects.all()

# Create your models here.
class CustomUser(AbstractUser):
    birthday = models.DateField(default=False)
    random_number = models.IntegerField(randint(1,100))

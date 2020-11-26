from django.db import models

# to create a custom user:
from django.contrib.auth.models import AbstractUser

# create a custom user as recommended by django doc class


class CustomUser(AbstractUser):
    pass

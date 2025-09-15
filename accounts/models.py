from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
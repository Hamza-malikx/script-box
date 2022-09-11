from datetime import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager

# Importing from user App
from User.models import User

# Create your models here ---------------------------

class ModeratorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MODERATOR)

class Moderator(User):
    base_role = User.Role.MODERATOR
    moderator = ModeratorManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "Only for moderators"

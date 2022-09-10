from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# from django.conf import settings
# User = settings.AUTH_USER_MODEL

# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your models here.

Type = (
    ('Paid', 'Paid'),
    ('Free', 'Free'),
)
Privacy = (
    ('Public', 'Public'),
    ('Unlisted', 'Unlisted'),
    ('Private', 'Private'),
)


# ---------------- Tayyab --------------------------------------------


# User Model
# class User(User):
#     is_user = models.BooleanField('Is user', default=False)
#     is_moderator = models.BooleanField('Is moderator', default=False)
#     is_admin = models.BooleanField('Is admin', default=False)


# class User(User):
#     DOCTOR = 1
#     NURSE = 2
#     SURGEN = 3

#     ROLE_CHOICES = (
#         (DOCTOR, 'Doctor'),
#         (NURSE, 'Nurse'),
#         (SURGEN, 'Surgen'),
#     )
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MODERATOR = "MODERATOR", "Moderator"
        USER = "USER", "User"

    # base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
    #         return super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['id']


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


class NormalUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.USER)

class NormalUser(User):
    base_role = User.Role.MODERATOR
    normalUser = NormalUserManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "Only for normal users"
# ---------------- Shahab --------------------------------------------

class Content(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default=datetime.now().strftime("%Y%m%d%H%M%S"))
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=600)
    thumbnail = models.ImageField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_universal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    tag = models.TextField(null=True, blank=True)
    type = models.CharField(choices=Type, max_length=50, null=True)
    privacy = models.CharField(choices=Privacy, max_length=50, null=True)
    views = models.IntegerField(blank=True, default=0)
    num_reviews = models.IntegerField(null=True, blank=True, default=0)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
<<<<<<< HEAD
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> 16c7c6c1780dcd19ba156e3176ec8f20b3d9c4f8

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['id']


class Script(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default=datetime.now().strftime("%Y%m%d%H%M%S"))
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    script = models.CharField(max_length=500, null=False)
    is_encrypted = models.BooleanField(default=False)
    is_patched = models.BooleanField(default=False)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


def contact_default():
    return {"email": "to1@example.com"}


class PrivateKey(models.Model):
<<<<<<< HEAD
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    script_id = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    privateKey = models.CharField(null=False, max_length=2000)
    #privateKey = models.JSONField()
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    script_id = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    privateKey = models.CharField(null=False, max_length=2000)
>>>>>>> 16c7c6c1780dcd19ba156e3176ec8f20b3d9c4f8

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']

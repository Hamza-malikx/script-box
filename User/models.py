from datetime import datetime
from django.contrib.auth.models import User, AbstractUser
from django.db import models

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
    

class User(User):
      DOCTOR = 1
      NURSE = 2
      SURGEN =3
      
      ROLE_CHOICES = (
          (DOCTOR, 'Doctor'),
          (NURSE, 'Nurse'),
          (SURGEN, 'Surgen'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['id']


class Script(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default=datetime.now().strftime("%Y%m%d%H%M%S"))
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    script = models.CharField(max_length=500,null=False)
    is_patched = models.BooleanField(default=False)


    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


def contact_default():
    return {"email": "to1@example.com"}

class PrivateKey(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    privateKey = models.TextField(null=False)
    # privateKey = models.JSONField("privateKey", default=contact_default)


    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
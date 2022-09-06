from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

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


# User Model
class User(User):
    is_user = models.BooleanField('Is user', default=False)
    is_moderator = models.BooleanField('Is moderator', default=False)
    is_admin = models.BooleanField('Is admin', default=False)

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
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    script = models.TextField(null=False)
    is_patched = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']

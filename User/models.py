import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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


# ---------------- Tayyab ------------------------------------------------
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MODERATOR = "MODERATOR", "Moderator"
        USER = "USER", "User"

    role = models.CharField(max_length=50, choices=Role.choices)
    old_username = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
        
    class Meta:
        ordering = ['id']


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200,unique=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    script_id = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    privateKey = models.CharField(null=False, max_length=2000)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']




class Badge(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return str(self.name)

    class Meta:
        ordering = ['id']



class BadgeContent (models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


class DraftContent (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.ForeignKey(Content, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


class FavContent (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    likes = models.IntegerField(blank=True,default=0)
    dislikes = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


class LikeCommentCheck (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
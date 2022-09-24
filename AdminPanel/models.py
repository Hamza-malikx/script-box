from django.db import models

# Create your models here.
from User.models import Badge


class ApplyBadgeCriteria(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    num_script = models.IntegerField(null=True,default=0)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


class Notification(models.Model):
    user = models.ForeignKey(Badge, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.id)

    class Meta:
        ordering = ['id']

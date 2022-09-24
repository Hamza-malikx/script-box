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
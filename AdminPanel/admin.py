from django.contrib import admin

from AdminPanel.models import ApplyBadgeCriteria
from User.models import User
# Register your models here.

admin.site.register(User)
admin.site.register(ApplyBadgeCriteria)

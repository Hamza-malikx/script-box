from django.contrib import admin

from AdminPanel.models import *
from .models import *
# Register your models here

admin.site.register(NormalUser)
admin.site.register(Content)
admin.site.register(Badge)
admin.site.register(BadgeContent)
admin.site.register(ApplyBadgeCriteria)
admin.site.register(Script)
admin.site.register(PrivateKey)
admin.site.register(Comment)
admin.site.register(FavContent)

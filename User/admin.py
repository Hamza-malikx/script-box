from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(NormalUser)
admin.site.register(Content)
admin.site.register(Script)
admin.site.register(PrivateKey)
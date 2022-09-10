from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('User.urls')),
    path('api/moderators/', include('Moderator.urls')),
    path('api/adminPanel/', include('AdminPanel.urls')),
]

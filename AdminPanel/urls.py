"""Abdullah URL Configuration
"""

from django.contrib import admin
from django.urls import path
from .import views
# from User import views


urlpatterns = [    
    path('', views.mainPage, name="mainPage"),
    path('users/', views.getUsers, name="users"),
    path('get-statistics/', views.getStatistics, name="statistics"),
    path('setBadge/', views.set_badge, name='set-badge'),
    path('getBadges/', views.get_badges, name='get-badges'),
    path('createBadge/', views.create_badge, name='create-badge'),
    path('imageUploadBadge/', views.upload_badge_image, name='image-badge'),
]

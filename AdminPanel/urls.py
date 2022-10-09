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
    path('getContentBadges/', views.get_content_badges, name='get-content-badges'),
    path('createBadge/', views.create_badge, name='create-badge'),
    path('deleteBadge/<str:pk>/', views.delete_badge, name='delete-badge'),
    path('imageUploadBadge/', views.upload_badge_image, name='image-badge'),

    path('suspendContent/', views.suspend_content, name='suspend-content'),
    path('getSuspendContent/', views.get_suspend_content, name='get_suspend_content'),
    path('unSuspendContent/<str:pk>/', views.un_suspend_content, name='un_suspend_content')
]

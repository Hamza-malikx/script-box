"""Abdullah URL Configuration
"""

from django.contrib import admin
from django.urls import path
from .import views
# from User import views


urlpatterns = [    
    path('', views.mainPage, name="mainPage"),
    path('users/', views.getUsers, name="users"),
    path('contents/', views.getContents, name="contents"),
    
    
]

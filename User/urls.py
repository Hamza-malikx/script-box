"""Abdullah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
# from User import views


urlpatterns = [
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # User..
    path('user/profile/', views.getUserProfile, name="user-profile"),
    path('user/register/', views.registerUser, name="register"),
    
    path('', views.getRoutes, name="routes"),
    path('user/uploadContent/', views.upload_content, name='upload-content'),
    path('user/content/<str:pk>/', views.get_content, name='get-content'),
    path('user/userContents/<str:pk>/', views.get_user_content, name='get-user-content'),
    path('user/allContent/', views.get_all_content, name='get-all-content'),
    path('user/updateContent/<str:pk>', views.update_content, name='update-content'),

]

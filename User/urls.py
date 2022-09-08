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
    path('', views.getRoutes, name="routes"),
    path('moderators/', views.getModerators, name="moderators"),
    path('normalUsers/', views.getNormalUsers, name="normal-users"),
    
    # User..
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name="user-profile"),
    path('register/', views.registerUser, name="register"),
    
    path('uploadContent/', views.upload_content, name='upload-content'),
    path('content/<str:pk>/', views.get_content, name='get-content'),
    path('userContents/<str:pk>/', views.get_user_content, name='get-user-content'),
    path('allContent/', views.get_all_content, name='get-all-content'),
    path('updateContent/<str:pk>/', views.update_content, name='update-content'),
    path('getDecryptedScript/<str:pk>/', views.decrypted_script, name='decrypted-script'),
    path('encryptScript/<str:pk>/', views.encrypt_script, name='encrypt-script'),


]

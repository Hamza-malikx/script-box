from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('normalUsers/', views.getNormalUsers, name="normal-users"),
    
    # User..
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name="user-profile"),
    path('register/', views.registerUser, name="register"),
    path('uploadContent/', views.upload_content, name='upload-content'),
    path('uploadContentImage/', views.upload_content_image, name='upload-image'),
    path('content/<str:pk>/', views.get_content, name='get-content'),
    path('userContents/<str:pk>/', views.get_user_content, name='get-user-content'),
    path('allContent/', views.get_all_content, name='get-all-content'),
    path('updateContent/<str:pk>/', views.update_content, name='update-content'),
    path('getDecryptedScript/<str:pk>/', views.decrypted_script, name='decrypted-script'),
    path('encryptScript/<str:pk>/', views.encrypt_script, name='encrypt-script'),


]

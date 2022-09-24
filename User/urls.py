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
    path('update/<str:pk>/', views.updateUser, name='user-update'),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
    
    path('uploadContent/', views.upload_content, name='upload-content'),
    path('uploadContentImage/', views.upload_content_image, name='upload-image'),
    path('uploadScript/', views.upload_content_script, name='upload-script'),
    path('content/<str:pk>/', views.get_content, name='get-content'),

    path('userContents/<str:pk>/', views.get_user_content, name='get-user-content'),
    path('allContent/', views.get_all_content, name='get-all-content'),
    path('updateContent/<str:pk>/', views.update_content, name='update-content'),
    path('getDecryptedScript/<str:pk>/', views.decrypted_script, name='decrypted-script'),
    path('encryptScript/<str:pk>/', views.encrypt_script, name='encrypt-script'),

    # badge
    path('badges/', views.get_badges, name='get-badges'),

    # comments
    path('publishComment/', views.publish_comment, name='publish_comment'),
    path('getComment/<str:pk>/', views.get_comment, name='get-comment'),
    path('deleteComment/<str:pk>/', views.delete_comment, name='delete-comment'),
    path('disLikeComment/<str:pk>/', views.disLike_comment, name='disLike-comment'),
    path('likeComment/<str:pk>/', views.like_comment, name='like-comment'),
    path('getRecentComments/', views.get_recent_comment, name='get-recent-comment'),

    # fav Content
    path('addFavContent/', views.add_fav_content, name='add_fav_content'),
    path('getFavContent/<str:pk>/', views.get_fav_content, name='get_fav_content'),
    path('deleteFavContent/<str:pk>/', views.delete_fav_content, name='delete_fav_content'),

]

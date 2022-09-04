from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
   path('', views.getRoutes, name="routes"),
]

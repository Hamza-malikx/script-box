from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

# JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from User.models import *

# Models
from . models import Moderator

# Serializers
from . serializers import ModeratorSerializer
from User.serializers import *

# Create your views here ---------------------------------------------------------

@api_view(['GET'])
def getModerators(request):
    studentUser = Moderator.moderator.all()
    serializer = ModeratorSerializer(studentUser, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def add_content_hashtags(request, pk):
    content = Content.objects.all(id=pk)
    data = request.data
    content.tag = data['hashtags']
    content.save()
    serializer = ContentSerializer(content, many=False)
    return Response(serializer.data)


from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from requests import Response
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

# JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Models
from AdminPanel.models import ApplyBadgeCriteria
from User.models import Script, Content, User, Badge

# Serializers
from User.serializers import ContentSerializer, UserSerializer, UserSerializerWithToken, BadgeSerializer


# Create your views here.

@api_view(['GET'])
def mainPage(request):
    return Response('AdminPanel')


# Get a user profile
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def set_badge(request):
    try:
        data = request.data
        badge_name = request.data['name']
        badge_num = request.data['scriptNumber']
        badge = Badge.objects.get(name=badge_name)

        bg = ApplyBadgeCriteria.objects.create(
            badge=badge,
            num_script=badge_num,
        )

        return Response("Uploaded badge criteria")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_badge(request):
    try:
        data = request.data

        bg = Badge.objects.create(
            name=data['name'],
            description=data['description'],
        )

        return Response("Uploaded badge")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_badges(request):
    try:
        bg = Badge.objects.all()
        serializer = BadgeSerializer(bg, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload_badge_image(request):
    try:

        bgId = request.data['name']
        bg = Badge.objects.get(name=bgId)
        bg.image = request.FILES.get('image')
        bg.save()

        return Response("Uploaded Image")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
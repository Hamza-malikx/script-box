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
from User.models import Script, Content, User

# Serializers
from User.serializers import ContentSerializer, UserSerializer, UserSerializerWithToken

# --------------------------------------------------------------------------

# User Authentication
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# ------------------------------------------------------

@api_view(['GET'])
def getRoutes(request):
    return Response('')

# ------------------------------------------------------
# Register a user:
@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------

# Get a user profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# ------------------------------------------------------

@api_view(['POST'])
def upload_content(request):
    data = request.data
    return None

@api_view(['POST'])
def register_shop(request):
    try:
        data = request.data
        # user = User.objects.get(username=data['user'])  user id sent from the frontend getting object
        content = Content.objects.create(
            #user=user,
            title=data['title'],
            link=data['link'],
            is_varfied=data['is_varfied'],
            is_universal=data['is_universal'],
            description=data['description'],
            features=data['features'],
            tag=data['tag'],
            type=data['type'],
            privacy=data['privacy'],

        )

        script = Script.objects.create(
            script= data['script'],
            content = content,
        )

        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        print(message)
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
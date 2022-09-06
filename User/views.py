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
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------------------------------------

# Get a user profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# -------------------Content-----------------------------------

@api_view(['POST'])
def upload_content(request):
    try:
        data = request.data
        user = User.objects.get(new_username=data['user'])
        content = Content.objects.create(
            user=user,
            title=data['title'],
            link=data['link'],
            is_varfied=data['is_varfied'],
            is_universal=data['is_universal'],
            description=data['description'],
            features=data['features'],
            tag=data['tag'],
            type=data['type'],
            privacy=data['privacy'],
            thumbnail= request.FILE.get('image')
        )

        script = Script.objects.create(
            script= data['script'],
            content = content,
        )

        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_content(self, pk):
    try:
        con = Content.objects.get(id=pk)
        Content.objects.get(id=pk).update(vew=con.views +1)
        serializer = ContentSerializer(con, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_content(self):
    try:
        con = Content.objects.all()
        serializer = ContentSerializer(con, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_content(self,pk):
    try:
        con = Content.objects.filter(user=User.objects.get(new_username=pk))
        serializer = ContentSerializer(con, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)\

@api_view(['PUT'])
def update_content(request,pk):
    try:
        data = request.data
        content = Content.object.get(id=pk).update(
            title=data['title'],
            link=data['link'],
            is_varfied=data['is_varfied'],
            is_universal=data['is_universal'],
            description=data['description'],
            features=data['features'],
            tag=data['tag'],
            type=data['type'],
            privacy=data['privacy'],
            thumbnail= request.FILE.get('image')
        )

        script = Script.object.get(content=content).update(
            script= data['script'],
            is_patched=data['patched'],
        )
        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
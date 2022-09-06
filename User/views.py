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
from User.models import Script, Content, User,PrivateKey

# Serializers
from User.serializers import ContentSerializer, UserSerializer, UserSerializerWithToken
import rsa

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
        user = User.objects.get(username=data['user'])
        content = Content.objects.create(
            user=user,
            title=data['title'],
            link=data['link'],
            is_verified=data['is_varfied'],
            is_universal=data['is_universal'],
            description=data['description'],
            features=data['features'],
            tag=data['tag'],
            type=data['type'],
            privacy=data['privacy'],
            thumbnail= data['image']
        )

        publicKey, privateKey = rsa.newkeys(512)
        encScript = rsa.encrypt(data['script'].encode(),
                                publicKey)

        sc = Script.objects.create(
            script= encScript,
            content = content,
        )

        key = PrivateKey.objects.create(
            user=user,
            script=sc,
            privateKey= privateKey,
        )

        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_content(self, pk):
    try:
        print(pk)
        con = Content.objects.get(id=pk)
        Content.objects.filter(id=pk).update(views=con.views +1)
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
def get_user_content(request,pk):
    try:
        con = Content.objects.filter(user=User.objects.get(username=pk))
        serializer = ContentSerializer(con, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_content(request,pk):
    try:
        print(pk)
        data = request.data
        content = Content.objects.filter(id=pk).update(
            title=data['title'],
            link=data['link'],
            is_verified=data['is_varfied'],
            is_universal=data['is_universal'],
            description=data['description'],
            features=data['features'],
            tag=data['tag'],
            type=data['type'],
            privacy=data['privacy'],
            thumbnail= data['image']
        )

        script = Script.objects.filter(content=content).update(
            script= data['script'],
            is_patched=data['patched'],
        )
        return Response("Updated")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def decrypted_script(self,pk):
    dy_sci ={}
    con = Content.objects.get(id=pk)
    scri = Script.objects.filter(content=con)
    for s in scri:
        p = PrivateKey.objects.get(script=s)
        dy_sci[s.id] = rsa.decrypt(s.script, rsa.importKey(p.privateKey)).decode()

    return Response({'data': dy_sci})


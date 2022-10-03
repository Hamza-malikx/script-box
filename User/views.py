from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# encryption
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# from requests import Response
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

# JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Models
from AdminPanel.models import ApplyBadgeCriteria
from User.models import *

# Serializers
from User.serializers import *


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

@api_view(['GET'])
def getNormalUsers(request):
    normalUser = NormalUser.normalUser.all()
    serializer = NormalUserSerializer(normalUser, many=True)
    return Response(serializer.data)


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

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    data = request.data

    user.username = data['username']
    # user.email = data['email']
    user.bio = data['bio']
    user.password = make_password(data['password'])
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')

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
            thumbnail=data['image']
        )

        print(data['script'])

        sc = Script.objects.create(
            script=data['script'],
            content=content,
        )
        script_count = len(Script.objects.filter(content=content))

        apply_badge = ApplyBadgeCriteria.objects.filter(num_script=script_count).first()

        if apply_badge:
                bc = BadgeContent.objects.create(
                    badge= apply_badge.badge,
                    content=content
                )


        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        print(message)
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload_content_image(request):
    try:
        contentID = request.data['id']
        content = Content.objects.get(id=contentID)
        content.thumbnail = request.FILES.get('image')
        content.save()
         
        return Response("Uploaded Image")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload_content_script(request):
    try:
        data = request.data
        contentID = request.data['id']
        content = Content.objects.get(id=contentID)

        sc = Script.objects.create(
            script=data['script'],
            content=content,
        )

        script_count = len(Script.objects.filter(content=content))

        apply_badge = ApplyBadgeCriteria.objects.filter(num_script=script_count).first()
        if apply_badge:
            bc = BadgeContent.objects.create(
                badge= apply_badge.badge,
                content=content
            )


        return Response("Uploaded Script")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_content(self, pk):
    try:
        con = Content.objects.get(id=pk)
        Content.objects.filter(id=pk).update(views=con.views + 1)
        serializer = ContentSerializer(con, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_badges(self):
    try:
        bg = BadgeContent.objects.all()
        serializer = BadgeContentSerializer(bg, many=True)
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
def get_user_content(request, pk):
    try:
        con = Content.objects.filter(user=User.objects.get(username=pk))
        serializer = ContentSerializer(con, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_content(request, pk):
    try:
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
            # thumbnail=data['image']
        )

        script = Script.objects.filter(content=content).update(
            script=data['script'],
            is_patched=data['patched'],
        )
        return Response("Updated")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def decrypted_script(self, pk):
    try:
        scri = Script.objects.get(id=pk)
        if scri.is_encrypted:
            key = PrivateKey.objects.get(script_id=scri.id)

            Pkey = key.privateKey[2:-1]
            PScri = scri.script[2:-1]
            decoded_text = decrypt(scri.id, PScri, Pkey)

            scri.is_encrypted = False
            scri.script = str(decoded_text)[2:-1]
            scri.save()
            key.delete()

            serializer = ScriptSerializer(scri, many=False)
            return Response(serializer.data)

        else:
            return Response("Already Decrypted")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def encrypt_script(request, pk):
    try:
        scri = Script.objects.get(id=pk)
        if not scri.is_encrypted:

            user = User.objects.get(username=scri.content.user.username)
            # Generate a salt for use in the PBKDF2 hash
            Pkey = base64.b64encode(os.urandom(12))  # Recommended method from cryptography.io
            encoded_text = encrypt(scri.id, scri.script, Pkey)

            scri.is_encrypted = True
            scri.script = encoded_text
            scri.save()

            priv = PrivateKey.objects.create(
                user=user,
                script_id=scri.id,
                privateKey=Pkey,
            )

            serializer = ScriptSerializer(scri, many=False)
            return Response(serializer.data)
        else:
            return Response("Encrypted Already")
    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


def encrypt(scri_id, script, salt):
    # Set up the hashing algo
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # This stretches the hash against brute forcing
        backend=default_backend(),  # Typically this is OpenSSL
    )
    # Derive a binary hash and encode it with base 64 encoding
    hashed_pwd = base64.b64encode(kdf.derive(scri_id.encode()))

    # Set up AES in CBC mode using the hash as the key
    f = Fernet(hashed_pwd)
    encrypted_secret = f.encrypt(script.encode())
    return encrypted_secret


def decrypt(scri_id, script, salt):
    # Set up the hashing algo
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,  # This stretches the hash against brute forcing
        backend=default_backend(),  # Typically this is OpenSSL
    )
    # Derive a binary hash and encode it with base 64 encoding
    hashed_pwd = base64.b64encode(kdf.derive(scri_id.encode()))

    # Set up AES in CBC mode using the hash as the key
    f = Fernet(hashed_pwd)

    secret = f.decrypt(script.encode())
    return secret


@api_view(['POST'])
def publish_comment(request):
    try:
        data = request.data
        user = User.objects.get(username=data['user'])
        content = Content.objects.get(title=data['content'])

        if not Comment.objects.filter(content=content,user=user).exists():
            comment = Comment.objects.create(
                user=user,
                content=content,
                comment= data['comment']
            )

            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data)
        else:
            return Response("Commented Already")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_comment(request,pk):
    try:
        data = request.data
        content = Content.objects.get(title=pk)
        comment = Comment.objects.filter(content=content)
        serializer = CommentSerializer(comment, many=True)
        print(serializer.data)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_recent_comment(request):
    try:
        data = request.data
        comment = Comment.objects.all().order_by('-id')[:10]

        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_comment(request,pk):
    try:
        comment = Comment.objects.get(id=pk).delete()
        return Response("Deleted")
    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def like_comment(request):
    try:
        data = request.data
        user = User.objects.get(username=data['user'])
        comment = Comment.objects.get(id=data['id'])
        if not LikeCommentCheck.objects.filter(comment=comment,user=user).exists():
            like = comment.likes
            comment = Comment.objects.filter(id=data['id']).update(likes=like+1)
            LikeCommentCheck.objects.create(comment=comment,user=user)
            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data)
        else:
            return Response("Liked Already")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def disLike_comment(request):
    try:
        data = request.data
        user = User.objects.get(username=data['user'])
        comment = Comment.objects.get(id=data['id'])
        if LikeCommentCheck.objects.filter(comment=comment,user=user).exists():
            like = comment.likes
            comment = Comment.objects.filter(id=data['id']).update(likes=like-1)
            LikeCommentCheck.objects.filter(comment=comment,user=user).delete()
            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data)
        else:
            return Response("Disliked")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_fav_content(request):
    try:
        data = request.data
        co = Content.objects.get(title=data['content'])
        user = User.objects.get(username=data['user'])
        if not FavContent.objects.filter(content=co).exists():
            fav = FavContent.objects.create(
                user= user,
                content= co
            )

            serializer = FavSerializer(fav, many=False)
            return Response("Added to Favorites")
        else:
            return Response("Already Added")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def check_fav_content(request, pk):
    try:
        data = request.data
        co = Content.objects.get(title=pk)
        return Response(FavContent.objects.filter(content=co).exists())

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_fav_content(request,pk):
    try:
        data = request.data
        user = User.objects.get(username=pk)

        fav = FavContent.objects.filter(
            user= user
        )

        serializer = FavSerializer(fav, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_fav_content(request,pk):
    try:
        fav = FavContent.objects.get(id=pk).delete()
        return Response("Deleted")
    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

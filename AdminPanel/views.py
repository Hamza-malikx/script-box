from multiprocessing import AuthenticationError
from django.http import JsonResponse
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
from User.models import Script, Content, User, Badge, SuspendContent
# Serializers
from User.serializers import ContentSerializer, UserSerializer, UserSerializerWithToken, BadgeSerializer, \
    ContentIDSerializer
from .serializers import ScriptSerializer, StatSerializer, BadgeConentSerializer


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


@api_view(['GET'])
def getStatistics(request):
    users = User.objects.all()
    contents = Content.objects.all()
    scripts = Script.objects.all()
    badges = Badge.objects.all()
    return JsonResponse(
        {
            'users': len(users),
            'contents': len(contents),
            'scripts': len(scripts),
            'badges': len(badges),
        }
    )


@api_view(['PUT'])
def patch_user_script(request, pk):
    script = Script.objects.all(id=pk)
    data = request.data
    script.is_patched = data['isPatched']
    script.save()
    serializer = ScriptSerializer(script, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def delet_or_suspend_user(request, pk):
    user = User.objects.all(id=pk)
    data = request.data
    if data['delete'] == 'delete':
        user.delete()
    else:    
        user.is_active = data['isActive']
        user.save()
    serializer = ScriptSerializer(User, many=False)
    return Response(serializer.data)


# Shahab Section Below ----------------------------------------------

@api_view(['POST'])
def set_badge(request):
    try:
        data = request.data
        id = request.data['Badgeid']
        badge_num = request.data['scriptNumber']
        badge = Badge.objects.get(id=id)

        if not ApplyBadgeCriteria.objects.filter(badge=badge).exists():
            bg = ApplyBadgeCriteria.objects.create(
                badge=badge,
                num_script=badge_num,
            )
            return Response("Uploaded badge criteria")
        else:
            ApplyBadgeCriteria.objects.filter(badge=badge).update(
                num_script=badge_num,
            )
            return Response("Updated")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_badge(request):
    try:
        data = request.data

        bg = Badge.objects.create(
            name=data['title'],
            description=data['desc'],
        )

        serializer = BadgeSerializer(bg, many=False)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_badge(request,pk):
    try:
        bg = ApplyBadgeCriteria.objects.get(id=pk).delete()
        return Response("Deleted")
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

@api_view(['GET'])
def get_content_badges(request):
    try:
        bg = ApplyBadgeCriteria.objects.all()
        serializer = BadgeConentSerializer(bg, many=True)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        print(message)
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload_badge_image(request):
    try:
        bgId = request.data['id']
        bg = Badge.objects.get(id=bgId)
        bg.image = request.FILES.get('image')
        bg.save()
        return Response("Uploaded Image")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def suspend_content(request):
    try:
        data = request.data
        pk = data['id']
        print(pk)
        con = Content.objects.get(id=pk)
        if not SuspendContent.objects.filter(content=con).exists():
            sus = SuspendContent.objects.create(
                content=con
            )
            co = Content.objects.filter(id=pk).update(is_suspend=True)
            return Response("Suspended")
        else:
            return Response("Already Suspended")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_suspend_content(request):
    try:
        data = request.data
        suspend = SuspendContent.objects.all()
        serializer = ContentIDSerializer(suspend, many=True)
        print(serializer.data)
        return Response(serializer.data)

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def un_suspend_content(request,pk):
    try:
        data = request.data
        con = Content.objects.get(id=pk)

        if SuspendContent.objects.filter(id=pk).exists():
            SuspendContent.objects.filter(id=pk).delete()
            co = Content.objects.filter(id=data['content']).update(is_suspend=False)
            return Response("UnSuspended")
        else:
            return Response("Already UnSuspended")

    except Exception as ex:
        message = {'detail': f'....{type(ex).__name__, ex.args}.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
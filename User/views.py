from django.shortcuts import render

# Create your views here.
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view

from User.models import Script, Content
from User.serializers import ContentSerializer


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
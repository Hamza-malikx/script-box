from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('Hello')

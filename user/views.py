from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers
from django.shortcuts import render
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import User
from .serializer import UserSerializer, UserCreateSerializer
from django.http import HttpResponse
import json
import uuid

class AnonymousUserView(APIView):
    '''
    사용자 Id를 받아 사용자의 정보를 돌려준다.
    '''
    @swagger_auto_schema(tags=['유저 API'])
    def get(self, request, id):
        obj = User.objects.get(id=id)
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, status = 200)

# 임시 유저를 생성함
class MakeAnonymousUserView(APIView):
    '''
    새로운 사용자를 생성하고, 사용자별로 고유한 임시 식별자를 발급한다.
    '''
    @swagger_auto_schema(tags=['유저 API'])
    def get(self, request):
        anonymousId = uuid.uuid4()
        user = User.objects.create(anonymous_id = anonymousId)
        serializer = UserCreateSerializer(user)
        return JsonResponse(serializer.data, status = 200)

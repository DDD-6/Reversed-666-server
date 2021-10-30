from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import render
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


    

class AnonymousUserView(APIView):
    @swagger_auto_schema(tags=['유저 API'])
    def get(self, request, anonymousId):
        return Response(f"{anonymousId}에 해당하는 사용자의 정보를 가져옵니다.")

class MakeAnonymousUserView(APIView):
    @swagger_auto_schema(tags=['유저 API'])
    def get(self, request):
        return Response("새로운 임시 사용자를 생성합니다.")
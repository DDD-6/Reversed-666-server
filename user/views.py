from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers
from django.shortcuts import render
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import User
from django.http import HttpResponse
import json
import uuid

class AnonymousUserView(APIView):
    @swagger_auto_schema(tags=['유저 API'])
    def get(self, request, anonymousId):
        return Response(f"{anonymousId}에 해당하는 사용자의 정보를 가져옵니다.")

# 임시 유저를 생성함
class MakeAnonymousUserView(APIView):
    @swagger_auto_schema(tags=['유저 API'])
    def get(self, request):
        anonymousId = uuid.uuid4()
        user = User.objects.create(anonymous_id = anonymousId)
        data = {
            "anonymousId" : f"{user.anonymous_id}"
        }
        return HttpResponse(json.dumps(data), content_type = "application/json", status = 200)
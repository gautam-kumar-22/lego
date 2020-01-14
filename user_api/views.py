# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSignUpSerializer, UserLoginSerializer

class SignUpApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = {}
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data['username'] = user.username
            data['email'] = user.email
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['error'] = "error"
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class LoginApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = {}
        serializer = UserLoginSerializer(data=request.data)
        import pdb;pdb.set_trace()
        if serializer.is_valid():
            authenticated_user = serializer.validated_data.get('authenticated_user')
            login(request, authenticated_user)
            data['id'] = authenticated_user.id
            data['username'] = authenticated_user.username
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['error'] = serializer.error
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class LogoutApiView(APIView):

    queryset = []
    def get(self, request):
        data = {
            'msg': "logged out successfully."
        }
        logout(request)
        return Response(data, status=status.HTTP_200_OK)

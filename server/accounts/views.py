from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response  
from .serializers import RegistrationSerializer,UsersSerializer
from rest_framework import permissions
from .models import Account
import requests
from rest_framework import status,generics

class AllUsers(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    queryset=Account.objects.all()
    serializer_class=UsersSerializer

class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)

class CreateAccount(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user=reg_serializer.save()
            if new_user:
                r=requests.post('http://127.0.0.1:8000/api-auth/token', data = {
                    'username':new_user.email,
                    'password':request.data['password'],
                    'client_id':'Your Client ID',
                    'client_secret':'Your Client Secret',
                    'grant_type':'password'
                })
                return Response(r.json(),status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
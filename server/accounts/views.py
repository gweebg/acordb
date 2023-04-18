from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response  
from .serializers import AccountSerializer,AdministratorSerializer,ConsumerSerializer,ConsumerRegistrationSerializer,AdministratorRegistrationSerializer
from rest_framework import permissions
from .models import Account
import requests
from rest_framework import status,generics

class AllUsers(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        serializer = AccountSerializer(self.request.user)
        return Response(serializer.data)

class CreateAdministrator(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=AdministratorRegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user=reg_serializer.save()
            if new_user:
                r=requests.post('http://127.0.0.1:8000/api-auth/token', data = {
                    'username':new_user.account.email,
                    'password':request.data['account']['password'],
                    'client_id':'45Wi64AqHgfs3Ehy8JGioH6wn1U1pGECfSzrCy5L',
                    'client_secret':'C67kEa9GwgVjAODaiXTbvHmlAbGFeRN2laaYzfv0LARGTjNrHeu4BQ8m9lIdBu32AfUGXlPjInzAeI66CruGLJFDlbOIc4RGp5n6SyNvxyuVwUmD9ZWKxC4MZznMDt8U',
                    'grant_type':'password'
                })
                return Response(r.json(),status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CreateConsumer(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=ConsumerRegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user=reg_serializer.save()
            if new_user:
                r=requests.post('http://127.0.0.1:8000/api-auth/token', data = {
                    'username':new_user.email,
                    'password':request.data['password'],
                    'client_id':'45Wi64AqHgfs3Ehy8JGioH6wn1U1pGECfSzrCy5L',
                    'client_secret':'C67kEa9GwgVjAODaiXTbvHmlAbGFeRN2laaYzfv0LARGTjNrHeu4BQ8m9lIdBu32AfUGXlPjInzAeI66CruGLJFDlbOIc4RGp5n6SyNvxyuVwUmD9ZWKxC4MZznMDt8U',
                    'grant_type':'password'
                })
                return Response(r.json(),status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
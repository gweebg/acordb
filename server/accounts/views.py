from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics,viewsets
from rest_framework.response import Response  
from .serializers import AccountSerializer,AdministratorSerializer,ConsumerSerializer,PasswordBasedLoginSerializer
from rest_framework import permissions
from .models import Account
import requests
from rest_framework import status,generics
from .permissions import IsAdministrator,IsConsumer
from django.conf import settings
from rest_framework import mixins
from .models import Administrator,Consumer

class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        serializer = AccountSerializer(self.request.user)
        return Response(serializer.data)
    
class PasswordBasedLogin(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=PasswordBasedLoginSerializer(data=request.data)
        if reg_serializer.is_valid():
            r=requests.post('http://127.0.0.1:8000/api-auth/token', data = {
                    'username':request.data['username'],
                    'password':request.data['password'],
                    'client_id':settings.DEFAULT_CLIENT_ID,
                    'client_secret':settings.DEFAULT_CLIENT_SECRET,
                    'grant_type':'password'
                })
            return Response(r.json(),status=status.HTTP_200_OK)
    

class CreateAdministrator(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=AdministratorRegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user=reg_serializer.save()
            if new_user:
                r=requests.post('http://127.0.0.1:8000/accounts/login/', data = {
                    'username':new_user.account.email,
                    'password':request.data['account']['password']
                })
                return Response(r.json(),status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AdministratorData(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    permission_classes=[IsAdministrator]
    serializer_class=AdministratorSerializer
    queryset = Administrator.objects.all()
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [AdministratorSerializer]
        return [permission() for permission in permission_classes]
    
    def perform_destroy(self, instance):
        instance.account.delete()
        instance.delete()
class ConsumerData(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    permission_classes=[IsConsumer]
    serializer_class=ConsumerSerializer()
    queryset = Consumer.objects.all()
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [AdministratorSerializer]
        return [permission() for permission in permission_classes]
    
    def perform_destroy(self, instance):
        instance.account.delete()
        instance.delete()
    
class CreateConsumer(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=ConsumerRegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user=reg_serializer.save()
            if new_user:
                r=requests.post('http://127.0.0.1:8000/accounts/login/', data = {
                    'username':new_user.email,
                    'password':request.data['password']
                })
                return Response(r.json(),status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
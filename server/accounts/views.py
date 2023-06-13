import requests
from django.conf import settings
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from .permissions import IsUser
from .serializers import (  AccountSerializer,
                            PasswordBasedLoginSerializer,
                            SocialMediaLoginSerializer)


class CurrentUser(mixins.ListModelMixin, 
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (IsUser,)
    serializer_class=AccountSerializer
    queryset = Account.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Check if the ListModelMixin is being used
        if 'list' in self.action:
            user = self.request.user
            queryset = queryset.filter(pk=user.pk)
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.first())  # Get the first item from the queryset
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
            return Response(r.json(),status=r.status_code)
        
class FacebookBasedLogin(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=SocialMediaLoginSerializer(data=request.data)
        if reg_serializer.is_valid():
            r=requests.post('http://127.0.0.1:8000/api-auth/convert-token', data = {
                    'token': request.data["token"],
                    'backend': "facebook",
                    'client_id':settings.DEFAULT_CLIENT_ID,
                    'client_secret':settings.DEFAULT_CLIENT_SECRET,
                    'grant_type':'convert_token'
                })
            return Response(r.json(),status=r.status_code)
class GoogleBasedLogin(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        reg_serializer=SocialMediaLoginSerializer(data=request.data)
        if reg_serializer.is_valid():
            r=requests.post('http://127.0.0.1:8000/api-auth/convert-token', data = {
                    'token': request.data["token"],
                    'backend': "google-oauth2",
                    'client_id':settings.DEFAULT_CLIENT_ID,
                    'client_secret':settings.DEFAULT_CLIENT_SECRET,
                    'grant_type':'convert_token'
                })
            return Response(r.json(),status=r.status_code)

        
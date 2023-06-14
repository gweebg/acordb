import requests
from django.conf import settings
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from records.models import Record,ChangeRequest
from favorites.models import Favorites
from django.shortcuts import get_object_or_404
from .permissions import IsUser,IsAdministrator
from .serializers import (  AccountSerializer,
                            PasswordBasedLoginSerializer,
                            SocialMediaLoginSerializer)
from django.db.models import Q,Value
from django.db.models.functions import Concat


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

class Search(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self,request,x):
        accounts = Account.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
        ).filter(
            Q(email__icontains=x) |
            Q(first_name__icontains=x) |
            Q(last_name__icontains=x) |
            Q(filiation__icontains=x) |
            Q(full_name__icontains=x)
        )
        return Response(AccountSerializer(accounts,many=True).data,status=status.HTTP_200_OK)
    
class Statistics(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        if request.user.is_administrator:
            return Response({
                "Processos":Record.objects.filter(added_by=request.user).count(),
                "Criação":request.user.created_at.strftime('%H:%M:%S %d/%m/%Y'),
                "Reviews":ChangeRequest.objects.filter(reviewer=request.user).count(),
                "Favoritos":Favorites.objects.filter(user=request.user).count()
                },status=status.HTTP_200_OK)
        else:
            return Response({
                "Changes":ChangeRequest.objects.filter(sujested_by=request.user).count(),
                "Criação":request.user.created_at.strftime('%H:%M:%S %d/%m/%Y'),
                "ChangesAccepted":ChangeRequest.objects.filter(sujested_by=request.user, status='accepted').count(),
                "ChangesDenied":ChangeRequest.objects.filter(sujested_by=request.user, status='denied').count(),
                "Favoritos":Favorites.objects.filter(user=request.user).count()
                },status=status.HTTP_200_OK)
            
         

class MakeConsumerAdmin(APIView):
    permission_classes=[IsAdministrator]
    
    def post(self, request,id):
        account = get_object_or_404(Account, id=id)
        if account.is_administrator:
            return Response(status=status.HTTP_403_FORBIDDEN)
        account.is_administrator=True
        account.save()
        return Response(AccountSerializer(account).data,status=status.HTTP_201_CREATED)
    
    
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

        
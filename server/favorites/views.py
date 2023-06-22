from django.shortcuts import render
from rest_framework import mixins,status,generics,permissions,viewsets
from rest_framework.response import Response
from .models import Favorites
from .serializers import FavoritesSerializer
from .permissions import FavoritesPermission
import uuid
# Create your views here.

class FavoritesData(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes=[FavoritesPermission]
    queryset=Favorites.objects.all()
    serializer_class=FavoritesSerializer
    
    def get_queryset(self, *args, **kwargs):
        return Favorites.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
    def create(self, request, *args, **kwargs):
        user = request.user
        acordao = request.data.get('acordao')

        # Check if a Favorites object with the same user and acordao already exists
        if Favorites.objects.filter(user=user, acordao=acordao).exists():
            return Response(
                {"error": "Favorites with this user and acordao already exists."},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            uuid.UUID(acordao)
        except ValueError:
            return Response(
                {"error": "Invalid UUID format for acordao."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        user = request.user
        acordao = request.data.get('acordao')
        instance = self.get_object()

        # Check if a Favorites object with the same user and acordao already exists
        if Favorites.objects.filter(user=user, acordao=acordao).exclude(pk=instance.pk).exists():
            return Response(
                {"error": "Favorites with this user and acordao already exists."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
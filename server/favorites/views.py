from django.shortcuts import render
from rest_framework import mixins,status,generics,permissions,viewsets
from rest_framework.response import Response
from .models import Favorites
from .serializers import FavoritesSerializer
from .permissions import FavoritesPermission
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
        processo = request.data.get('processo')

        # Check if a Favorites object with the same user and processo already exists
        if Favorites.objects.filter(user=user, processo=processo).exists():
            return Response(
                {"error": "Favorites with this user and processo already exists."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        user = request.user
        processo = request.data.get('processo')
        instance = self.get_object()

        # Check if a Favorites object with the same user and processo already exists
        if Favorites.objects.filter(user=user, processo=processo).exclude(pk=instance.pk).exists():
            return Response(
                {"error": "Favorites with this user and processo already exists."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
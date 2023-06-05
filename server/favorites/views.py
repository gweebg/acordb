from django.shortcuts import render
from rest_framework import mixins,status,generics,permissions,viewsets
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
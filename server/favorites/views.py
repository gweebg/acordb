from django.shortcuts import render
from rest_framework import mixins,status,generics,permissions,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Favorites
from records.models import Acordao
from .serializers import FavoritesSerializer
from .permissions import FavoritesPermission
import uuid
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class IsFavorite(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Check if the acordao is a favorite",
        manual_parameters=[
            openapi.Parameter(
                name="acordao",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="ID of the acordao",
                required=True,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Favorite found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "acordao": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                    },
                ),
            ),
            204: openapi.Response(description="Favorite not found"),
        },
    )
    def get(self, request,acordao):
        acordao = get_object_or_404(Acordao,pk=acordao)
        fav = Favorites.objects.filter(user=request.user, acordao=acordao).first()
        if fav is not None:
            return Response(FavoritesSerializer(fav).data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

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
        user = self.request.user
        if user.is_authenticated:
            return Favorites.objects.filter(user=user)
        return Favorites.objects.none()
    
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
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account,APIKey
from records.models import Record,ChangeRequest
from favorites.models import Favorites
from django.shortcuts import get_object_or_404
from .permissions import IsUser,IsAdministrator
from .serializers import (  AccountSerializer,
                            APIKeySerializer,
                            EmailSerializer)
from django.db.models import Q,Value
from django.db.models.functions import Concat
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.http import JsonResponse
import json
from google.oauth2 import id_token as google_id_token
from google.auth.transport import requests as google_requests
from django.conf import settings
from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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


class Requests(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Retrieves the changeRequest that need to be shown to the user",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_STRING),
                            'sujested_by': openapi.Schema(type=openapi.TYPE_STRING),
                            'acordao': openapi.Schema(type=openapi.TYPE_STRING),
                            'added_at': openapi.Schema(type=openapi.TYPE_STRING),
                            'status': openapi.Schema(type=openapi.TYPE_STRING),
                            'reviewer': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                            'merged': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                            'data': openapi.Schema(type=openapi.TYPE_OBJECT),
                        },
                    ),
                ),
            ),
        },
    )
    def get(self,request):
        """
        Retrieves the changeRequest that need to be shown to the user
        Returns a list of ChangeRequests
        In case the user is Administrator all ChangeRequests are returned
        If the user is Comsumer only the ChangeRequests he sujested will be returned
        """
        if not request.user.is_administrator:
            return Response(ChangeRequest.objects.sujested_by(request.user),status=status.HTTP_200_OK)
        else:
            return Response(ChangeRequest.objects.getAllRequests(),status=status.HTTP_200_OK)
        


class Search(APIView):
    permission_classes=[permissions.AllowAny]
    @swagger_auto_schema(
        operation_description="Free search for a user",
        manual_parameters=[
            openapi.Parameter(
                'x',
                openapi.IN_PATH,
                description="The term to search for",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'email': openapi.Schema(type=openapi.TYPE_STRING),
                            'password': openapi.Schema(type=openapi.TYPE_STRING),
                            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'filiation': openapi.Schema(type=openapi.TYPE_STRING),
                            'is_administrator': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        },
                    ),
                ),
            ),
        },
    )
    def get(self,request,x):
        """
        Free search for a user
        "x" is the term to search for
        Returns the data of all user that match the query
        """
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
    @swagger_auto_schema(
        operation_description="Retrieves the statistics of a user",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "Acordãos": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Criação": openapi.Schema(type=openapi.TYPE_STRING),
                        "Reviews": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Changes": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "ChangesAccepted": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "ChangesDenied": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Favoritos": openapi.Schema(type=openapi.TYPE_INTEGER),
                    },
                ),
            ),
        },
    )
    def get(self,request):
        """
        Retrieves the statistics of a user
        If the user is Comsumer:
            "Changes": The number of changes requested by the user
            "Criação": The Date and time the account was created at
            "ChangesAccepted": The number of changes that were aproved
            "ChangesDenied": The number of changes that were denied
            "Favoritos": The number of Favorites of the user
        If the user is Administrator:
            "Acordãos": Number of acordãos Created
            "Criação": The Date and time the account was created at
            "Reviews": Number of changes requested Created
            "Favoritos": The number of Favorites of the user
        """
        if request.user.is_administrator:
            return Response({
                "Acordãos":Record.objects.filter(added_by=request.user).count(),
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
    @swagger_auto_schema(
        operation_description="Changes the authorization level of a consumer to an admin",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["email"],
        ),
        responses={
            201: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_STRING),
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                        "password": openapi.Schema(type=openapi.TYPE_STRING),
                        "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "filiation": openapi.Schema(type=openapi.TYPE_STRING),
                        "is_administrator": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    },
                ),
            ),
            400: openapi.Response(
                description="Bad request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "errors": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
        },
    )
    def post(self, request):
        """
        Changes the authorization level of a consumer to an admin
        Returns the the data of the user.
        
        Recieves an "email" of the user to make admin
        """
        ser = EmailSerializer(data=request.data)
        if ser.is_valid():
            account = get_object_or_404(Account, email=request.data['email'])
            if account.is_administrator:
                return Response({'errors':'the account is already an administrator'},status=400)
            account.is_administrator=True
            account.save()
            return Response(AccountSerializer(account).data,status=status.HTTP_201_CREATED)
    

class GenerateApiKey(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Creates an API Key for the authenticated user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["name"],
        ),
        responses={
            201: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "key": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: openapi.Response(
                description="Bad request",
            ),
        },
    )
    def post(self,request):
        """
        Creates an API Key for the authenticated user
        Returns the api key generated in "key" field.
        
        Recieves a "name" to give to the APIKey.
        """
        ser = APIKeySerializer(data=request.data)
        if ser.is_valid():
            key = APIKey.objects.create_newkey(name=request.data['name'],user=request.user)
            return Response({'key':key[1]},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
@csrf_exempt
def google_auth_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            google_token = data.get('token')
            decoded_token = google_id_token.verify_oauth2_token(google_token.encode(),google_requests.Request(),settings.GOOGLE_CLIENT_ID)
            email = decoded_token['email']
            account = Account.objects.filter(email=email).first()
            if account is None:
                first_name = decoded_token['given_name']
                last_name = decoded_token['family_name']
                filiation = "google"
                account=Account.objects.create_consumer(email,first_name,last_name,"akdsklhnyauftbg121341",filiation)
                account.set_unusable_password()
                account.save()
            refresh = RefreshToken.for_user(account)
            return JsonResponse({ 'refresh': str(refresh),'access': str(refresh.access_token)}, status=200)
                    
        except (ValueError) as e:
            return JsonResponse({'error': 'Invalid token'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

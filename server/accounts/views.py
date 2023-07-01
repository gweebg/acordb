from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account,APIKey
from records.models import Record,ChangeRequest
from favorites.models import Favorites
from django.shortcuts import get_object_or_404
from .permissions import IsUser,IsAdministrator
from .serializers import (  AccountSerializer,
                            APIKeySerializer)
from django.db.models import Q,Value
from django.db.models.functions import Concat
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.http import JsonResponse
import json


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
    def get(self,request):
        if not request.user.is_administrator:
            return Response(ChangeRequest.objects.sujested_by(request.user),status=status.HTTP_200_OK)
        else:
            return Response(ChangeRequest.objects.getAllRequests(),status=status.HTTP_200_OK)
        


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
    

class GenerateApiKey(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self,request):
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
            decoded_token = jwt.decode(google_token.encode(), verify=False)
            email = decoded_token['email']
            account = Account.objects.filter(email=email).first()
            if account is None:
                if 'filiation' not in data:
                    return JsonResponse({'error': 'Missing filiation for new account'}, status=400)
                first_name = decoded_token['given_name']
                last_name = decoded_token['family_name']
                filiation = data.get('filiation')
                account=Account.objects.create_consumer(email,first_name,last_name,"akdsklhnyauftbg121341",filiation)
                account.set_unusable_password()
                account.save()
            refresh = RefreshToken.for_user(account)
            return JsonResponse({ 'refresh': str(refresh),'access': str(refresh.access_token)}, status=200)
                    
        except (jwt.DecodeError, jwt.ExpiredSignatureError) as e:
            return JsonResponse({'error': 'Invalid token'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

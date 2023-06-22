from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status,mixins,generics,viewsets
from .mongo import *
import uuid
import bson
from .models import Record,ChangeRequest,Tag,Field,Acordao
from .permissions import IsAdministrator,IsConsumer,BelongsToUser
# Create your views here.

from .serializers import TagSerializer,FieldSerializer
# Create your views here.

class Tags(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Tag.objects.all()
    serializer_class=TagSerializer
    
class Fields(mixins.ListModelMixin,
             viewsets.GenericViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Field.objects.all()
    serializer_class=FieldSerializer
    
class AcordaoView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        elif self.request.method == 'POST':
            return [IsAdministrator()]
        return super().get_permissions()

    def get(self, request, acordao=None):
            if acordao==None:
                d=request.GET.dict()
                return Response(Acordao.objects.getMany(d),status=status.HTTP_200_OK)
            else:
                #Retrieve
                r=Acordao.objects.getOne(acordao)
                if r is None:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response(r,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        r = Acordao.objects.create(request.data,request.user)
        if r is not None:
            return Response(r,status=status.HTTP_201_CREATED)
        return Response({},status=status.HTTP_400_BAD_REQUEST)

class RecordsView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        return super().get_permissions()
    
    def get(self, request, acordao):
        if Acordao.objects.filter(id=acordao).exists():
            return Response(Record.objects.getMany(acordao),status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
class RecordView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        return super().get_permissions()
    
    def get(self, request, id):
        r=Record.objects.getOne(id)
        if r is not None:
            return Response(r,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    



class ChangeRequestsView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
    
    def get(self, request,acordao):
        #list
        r=ChangeRequest.objects.getRequests(acordao)
        if r is not None:
            return Response(r,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND) 
            
    def post(self,request,acordao):
        if not Record.objects.filter(acordao=acordao).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        r = ChangeRequest.objects.create(acordao,request.data,request.user)
        if r is not None:
            return Response(r,status=status.HTTP_201_CREATED)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
         
        
class ChangeRequestView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        elif self.request.method == 'DELETE':
            return [BelongsToUser()]
        elif self.request.method == 'PATCH':
            return [IsAdministrator()]
        return super().get_permissions()
    
    def get(self, request,requestId=None):
        r=ChangeRequest.objects.getRequest(requestId)
        if r is not None:
            return Response(r,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request,requestId, format=None):
        r=ChangeRequest.objects.deleteRequest(requestId)
        if r is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif r is {}:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(r,status=status.HTTP_204_NO_CONTENT)
        
    def patch(self, request, requestId, format=None):
        request_status=request.data.pop('status',None)
        if request_status and (request_status=='accepted' or request_status=='denied'):
            if request_status=='accepted':
                r=ChangeRequest.objects.acceptRequest(requestId,request.user)
            else:
                r=ChangeRequest.objects.denyRequest(requestId,request.user)
            if r is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(r,status=status.HTTP_202_ACCEPTED)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
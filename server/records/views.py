from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status,mixins,generics,viewsets
from .mongo import *
import uuid
import bson
from .models import Record,ChangeRequest,Tag
from .permissions import IsAdministrator,IsConsumer,BelongsToUser
# Create your views here.

from .serializers import TagSerializer
# Create your views here.

class Tags(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

class Records(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        elif self.request.method == 'POST':
            return [IsAdministrator()]
        return super().get_permissions()
    
    def get(self, request, processo=None):
        if processo==None:
            d=request.GET.dict()
            idQ = d.pop('id',None)
            if idQ is not None:
                d['_id']=bson.Binary.from_uuid(uuid.UUID(idQ))
            return Response(Record.objects.getMany(d),status=status.HTTP_200_OK)
        else:
            #Retrieve
            r=Record.objects.getOne(processo)
            if r is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(r,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        if 'Processo' in request.data:
            if Record.objects.filter(processo=request.data['Processo']).exists():
                return Response(status=status.HTTP_403_FORBIDDEN)
            r = Record.objects.create(request.data,request.user)
            if r is not None:
                return Response(r,status=status.HTTP_201_CREATED)
        return Response({},status=status.HTTP_400_BAD_REQUEST)

class ChangeRequests(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [BelongsToUser()]
        elif self.request.method == 'PATCH':
            return [IsAdministrator()]
        return super().get_permissions()
    
    def get(self, request,processo, requestId=None):
        if requestId is None:
            #list
            r=ChangeRequest.objects.getRequests(processo)
            if r is not None:
                return Response(r,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND) 
        else:
            #retrieve
            r=ChangeRequest.objects.getRequest(requestId)
            if r is not None:
                return Response(r,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
    def post(self,request,processo):
        if not Record.objects.filter(processo=processo).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        r = ChangeRequest.objects.create(processo,request.data,request.user)
        if r is not None:
            return Response(r,status=status.HTTP_201_CREATED)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request,requestId,processo=None, format=None):
        r=ChangeRequest.objects.deleteRequest(requestId)
        if r is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif r is {}:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(r,status=status.HTTP_204_NO_CONTENT)
        
    def patch(self, request, requestId,processo=None, format=None):
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
        
            
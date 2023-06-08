from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from accounts.models import Administrator
from .mongo import *
from .models import Record
from .permissions import IsAdministrator
# Create your views here.

class ListRecords(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()] 
        elif self.request.method == 'POST':
            return [IsAdministrator()]
        elif self.request.method == 'PUT':
            return [IsAdministrator()]
        elif self.request.method == 'DELETE':
            return [IsAdministrator()]
        return super().get_permissions()
    
    def get(self, request, id=None):
        if id==None:
            query=request.GET.dict()
            records = getManyRecords(query)
            return Response([{"added_by":Record.objects.get(id=v["_id"]).added_by,"data":v} for v in records],status=status.HTTP_200_OK)
        else:
            #Retrieve
            if not Record.objects.filter(id=id).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            v = getOneRecord(id)
            return Response({"added_by":Record.objects.get(id=v["_id"]).added_by,"data":v},status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        if '_id' in request.data and not Record.objects.filter(id=request.data["_id"]).exists():
            r=createRecord(request.data)
            if r is not None:
                rec=Record(id=r['_id'],added_by=Administrator.objects.get(account=request.user))
                rec.save()
                return Response(r,status=status.HTTP_201_CREATED)
        return Response({},status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id, format=None):
        if not Record.objects.filter(id=id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        r=updateRecord(id,request.data)
        if r is not None:
            return Response(r,HTTP_202_ACCEPTED)
        else:
            return Response({},HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        if not Record.objects.filter(id=id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        r=getOneRecord(id)
        d=deleteRecord(id)
        if d:
            Record.objects.get(id=id).delete()
            return Response(r,status=HTTP_204_NO_CONTENT)
        else:
            return Response({},status=HTTP_400_BAD_REQUEST)
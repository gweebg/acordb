from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status,mixins,generics,viewsets
from .mongo import *
import uuid
import bson
from .models import Record,ChangeRequest,Tag,Field,Acordao
from .permissions import IsAdministrator,IsConsumer,BelongsToUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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
    
    @swagger_auto_schema(
        operation_description="Get Acordão",
        manual_parameters=[
            openapi.Parameter(
                "acordao",
                openapi.IN_QUERY,
                description="ID of the specific Acordão to retrieve or None to get all",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successful operation",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "data": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items= openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING),
        "sujested_by": openapi.Schema(type=openapi.TYPE_STRING),
        "acordao": openapi.Schema(type=openapi.TYPE_STRING),
        "added_at": openapi.Schema(type=openapi.TYPE_STRING),
        "status": openapi.Schema(type=openapi.TYPE_STRING),
        "reviewer": openapi.Schema(type=openapi.TYPE_STRING),
        "merged": openapi.Schema(type=openapi.TYPE_STRING),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_STRING),
            properties={
                "Processo": openapi.Schema(type=openapi.TYPE_STRING),
                "Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Data do Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Descritores": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                ),
            },
            required=["Processo", "Acordão", "Data do Acordão", "Descritores"],
        ),
    },
    required=[],
),
                        ),
                        "count": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Total count of Acordãos",
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Acordão not found",
            ),
        },
    )
    def get(self, request, acordao=None):
        """
        If acordãos is set then returns onlythe data of the acordão
        Otherwise returns the data of all acordãos that match the querystring
        """
        if acordao==None:
            d=request.GET.dict()
            data,count = Acordao.objects.getMany(d)
            return Response({'data':data,'count':count},status=status.HTTP_200_OK)
        else:
            #Retrieve
            r=Acordao.objects.getOne(acordao)
            if r is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(r,status=status.HTTP_200_OK)
            
    @swagger_auto_schema(
        operation_description="Create Acordão",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "added_by": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="ID of the user who added the Acordão",
                ),
                "added_at": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description="Date and time when the Acordão was added",
                ),
                "acordao": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="ID of the Acordão",
                ),
                "tags": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_STRING,
                    ),
                    description="List of tags associated with the Acordão",
                ),
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="Data of the Acordão",
                ),
            },
            required=["added_by", "added_at", "acordao", "tags", "data"],
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Acordão created successfully",
                items= openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_STRING),
            properties={
                "Processo": openapi.Schema(type=openapi.TYPE_STRING),
                "Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Data do Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Descritores": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                ),
            },
            required=["Processo", "Acordão", "Data do Acordão", "Descritores"],
        ),
    },
    required=[],
),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Bad request",
            ),
        },
    )
    def post(self, request, format=None):
        """
        Creates a new acordão with the data given
        Returns the created acordão
        """
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
        """
        Returns all the data version of the given acordão
        """
        if Acordao.objects.filter(id=acordao).exists():
            return Response(Record.objects.getMany(acordao),status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
class RecordView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()] 
        return super().get_permissions()
    @swagger_auto_schema(
        operation_description="Get Data Versions",
        manual_parameters=[
            openapi.Parameter(
                "acordao",
                openapi.IN_PATH,
                description="ID of the Acordão",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successful operation",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "data": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items= openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING),
        "sujested_by": openapi.Schema(type=openapi.TYPE_STRING),
        "acordao": openapi.Schema(type=openapi.TYPE_STRING),
        "added_at": openapi.Schema(type=openapi.TYPE_STRING),
        "status": openapi.Schema(type=openapi.TYPE_STRING),
        "reviewer": openapi.Schema(type=openapi.TYPE_STRING),
        "merged": openapi.Schema(type=openapi.TYPE_STRING),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_STRING),
            properties={
                "Processo": openapi.Schema(type=openapi.TYPE_STRING),
                "Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Data do Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Descritores": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                ),
            },
            required=["Processo", "Acordão", "Data do Acordão", "Descritores"],
        ),
    },
    required=[],
),
                        ),
                    },
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Acordão not found",
            ),
        },
    )
    def get(self, request, id):
        """
        Returns the data version of the given record
        """
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
    @swagger_auto_schema(
        operation_description="Get Change Requests",
        manual_parameters=[
            openapi.Parameter(
                "acordao",
                openapi.IN_PATH,
                description="ID of the Acordão",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successful operation",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                   items= openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING),
        "sujested_by": openapi.Schema(type=openapi.TYPE_STRING),
        "acordao": openapi.Schema(type=openapi.TYPE_STRING),
        "added_at": openapi.Schema(type=openapi.TYPE_STRING),
        "status": openapi.Schema(type=openapi.TYPE_STRING),
        "reviewer": openapi.Schema(type=openapi.TYPE_STRING),
        "merged": openapi.Schema(type=openapi.TYPE_STRING),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_STRING),
            properties={
                "Processo": openapi.Schema(type=openapi.TYPE_STRING),
                "Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Data do Acordão": openapi.Schema(type=openapi.TYPE_STRING),
                "Descritores": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                ),
            },
            required=["Processo", "Acordão", "Data do Acordão", "Descritores"],
        ),
    },
    required=[],
),
                ),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Acordão not found",
            ),
        },
    )
    def get(self, request,acordao):
        """
        Returns the data of all change requests sujested to the acordão
        """
        #list
        r=ChangeRequest.objects.getRequests(acordao)
        if r is not None:
            return Response(r,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        
    @swagger_auto_schema(
        operation_description="Create Change Request",
        manual_parameters=[
            openapi.Parameter(
                "acordao",
                openapi.IN_PATH,
                description="ID of the Acordão",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Data for the change request",
                ),
            },
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Change request created successfully",
                items=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_STRING),
        ),
    },
    required=["id", "sujested_by", "acordao", "added_at", "status"],
),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Bad request",
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Acordão not found",
            ),
        },
    )
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
    
    @swagger_auto_schema(
        operation_description="Get Change Request",
        manual_parameters=[
            openapi.Parameter(
                "requestId",
                openapi.IN_PATH,
                description="ID of the Change Request",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successful operation",
                 items=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING),
        "sujested_by": openapi.Schema(type=openapi.TYPE_STRING),
        "acordao": openapi.Schema(type=openapi.TYPE_STRING),
        "added_at": openapi.Schema(type=openapi.TYPE_STRING),
        "status": openapi.Schema(type=openapi.TYPE_STRING),
        "reviewer": openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
        "merged": openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_STRING),
        ),
    },
    required=["id", "sujested_by", "acordao", "added_at", "status"],
),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Change Request not found",
            ),
        },
    )
    def get(self, request,requestId=None):
        r=ChangeRequest.objects.getRequest(requestId)
        if r is not None:
            return Response(r,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        operation_description="Delete Change Request",
        manual_parameters=[
            openapi.Parameter(
                "requestId",
                openapi.IN_PATH,
                description="ID of the Change Request",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Change Request deleted successfully",
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Change Request not found",
            ),
        },
    )
    def delete(self, request,requestId, format=None):
        r=ChangeRequest.objects.deleteRequest(requestId)
        if r is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif r is {}:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(r,status=status.HTTP_204_NO_CONTENT)
        
    @swagger_auto_schema(
        operation_description="Update Change Request",
        manual_parameters=[
            openapi.Parameter(
                "requestId",
                openapi.IN_PATH,
                description="ID of the Change Request",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "status": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Status of the Change Request",
                ),
            },
        ),
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                description="Change Request updated successfully",
                 items=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=["id", "sujested_by", "acordao", "added_at", "status"],
),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Bad request",
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Change Request not found",
            ),
        },
    )
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
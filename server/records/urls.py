from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RecordsMostRecent,Records,ChangeRequests,Tags,Fields
app_name = 'records'

router = DefaultRouter()



urlpatterns = [
   path('tags/', Tags.as_view({'get': 'list'}), name='tag-list'),
   path('tags/<pk>/', Tags.as_view({'get': 'retrieve'}), name='tag-detail'),
   path('fields/',Fields.as_view({'get': 'list'}), name='field-list'),
   path('mostRecent/',RecordsMostRecent.as_view(),name='records-mostRecent-list'),
   path('<str:processo>/alteracoes/<uuid:requestId>/', ChangeRequests.as_view(), name='changeRequests-detail'),
   path('<str:processo>/alteracoes/', ChangeRequests.as_view(), name='changeRequests-list'),
   path('<str:processo>/', Records.as_view(), name='records-detail'),
   path('', Records.as_view(), name='records-list'),
   ]
urlpatterns+=router.urls
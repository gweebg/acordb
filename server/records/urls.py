from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RecordsView,RecordView,ChangeRequestsView,AcordaoView,ChangeRequestView,Tags,Fields
app_name = 'records'

router = DefaultRouter()



urlpatterns = [
   path('tags/', Tags.as_view({'get': 'list'}), name='tag-list'),
   path('tags/<pk>/', Tags.as_view({'get': 'retrieve'}), name='tag-detail'),
   path('fields/',Fields.as_view({'get': 'list'}), name='field-list'),
   path('changeRequest/<requestId>/',ChangeRequestView.as_view(),name='changeRequests-details'),
   path('changeRequests/<acordao>/',ChangeRequestsView.as_view(),name='changeRequests-list'),
   path('record/<id>/',RecordView.as_view(),name='records-details'),
   path('records/<acordao>/',RecordsView.as_view(),name='records-list'),
   path('<acordao>/',AcordaoView.as_view(),name='acordaos-details'),
   path('',AcordaoView.as_view(),name='acordaos-list'),
   ]
urlpatterns+=router.urls
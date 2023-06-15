from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Records,ChangeRequests,Tags
app_name = 'records'

router = DefaultRouter()



urlpatterns = [
   path('tags/', Tags.as_view({'get': 'list'}), name='tag-list'),
   path('tags/<pk>/', Tags.as_view({'get': 'retrieve'}), name='tag-detail'),
   path('<str:processo>/alteracoes/<uuid:requestId>/', ChangeRequests.as_view(), name='changeRequests-detail'),
   path('<str:processo>/alteracoes/', ChangeRequests.as_view(), name='changeRequests-list'),
   path('<str:processo>/', Records.as_view(), name='records-detail'),
   path('', Records.as_view(), name='records-list'),
   ]
urlpatterns+=router.urls
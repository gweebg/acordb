from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ListRecords
app_name = 'records'

router = DefaultRouter()



urlpatterns = [
   path('', ListRecords.as_view(), name='your-model-list'),
   path('<id>/', ListRecords.as_view(), name='your-model-detail'),
   ]
urlpatterns+=router.urls
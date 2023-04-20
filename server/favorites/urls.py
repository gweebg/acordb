from django.urls import path,include
from .views import FavoritesData
from rest_framework.routers import DefaultRouter
app_name = 'favorites'

router = DefaultRouter()
router.register(r'', FavoritesData, basename='favorites')


urlpatterns = [
   ]
urlpatterns+=router.urls
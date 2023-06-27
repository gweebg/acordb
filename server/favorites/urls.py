from django.urls import path,include
from .views import FavoritesData,IsFavorite
from rest_framework.routers import DefaultRouter
app_name = 'favorites'

router = DefaultRouter()
router.register(r'', FavoritesData, basename='favorites')


urlpatterns = [
   path('isFavorite/<acordao>/',IsFavorite.as_view(),name='is favorite'),
   ]
urlpatterns+=router.urls
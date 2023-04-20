from django.urls import path,include
from .views import CurrentUser,PasswordBasedLogin,AdministratorData,ConsumerData
from rest_framework.routers import DefaultRouter
app_name = 'users'

router = DefaultRouter()
router.register(r'administrator', AdministratorData, basename='administrator')
router.register(r'consumer', ConsumerData,basename='consumer')


urlpatterns = [
   path('login/',PasswordBasedLogin.as_view(),name="password_login"),
   path('personal/', CurrentUser.as_view(), name="current"),
   path('', include('social_django.urls', namespace='social'))
   ]
urlpatterns+=router.urls
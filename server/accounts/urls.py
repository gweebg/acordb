from django.urls import path,include
from .views import CurrentUser,CreateAdministrator,CreateConsumer,PasswordBasedLogin,AdministratorData
from rest_framework.routers import DefaultRouter
app_name = 'users'

router = DefaultRouter()
router.register(r'administrator', AdministratorData, basename='administrator')


urlpatterns = [
   path('login/',PasswordBasedLogin.as_view(),name="password_login"),
   path('create/administrator/', CreateAdministrator.as_view(), name="create_administrator"),
   path('create/consumer/', CreateAdministrator.as_view(), name="create_consumer"),
   path('personal/', CurrentUser.as_view(), name="current"),
   path('', include('social_django.urls', namespace='social'))
   ]
urlpatterns+=router.urls
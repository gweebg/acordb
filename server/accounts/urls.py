from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AdministratorData, ConsumerData, CurrentUser,
                    PasswordBasedLogin,FacebookBasedLogin,GoogleBasedLogin)

app_name = 'users'

router = DefaultRouter()
router.register(r'administrator', AdministratorData, basename='administrator')
router.register(r'consumer', ConsumerData, basename='consumer')


urlpatterns = [
   path('login/password/',PasswordBasedLogin.as_view(),name="password_login"),
   path('login/google/',GoogleBasedLogin.as_view(),name="google_login"),
   path('login/facebook/',FacebookBasedLogin.as_view(),name="facebook_login"),
   path('personal/', CurrentUser.as_view(), name="current"),
   path('', include('social_django.urls', namespace='social'))
]

urlpatterns+=router.urls
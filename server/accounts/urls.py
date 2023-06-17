from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CurrentUser,
                    Search,
                    Statistics,
                    GenerateApiKey,
                    PasswordBasedLogin,
                    FacebookBasedLogin,
                    GoogleBasedLogin,
                    MakeConsumerAdmin)

app_name = 'users'

router = DefaultRouter()
router.register(r'user', CurrentUser, basename='user')


urlpatterns = [
   path('login/password/',PasswordBasedLogin.as_view(),name="password_login"),
   path('login/google/',GoogleBasedLogin.as_view(),name="google_login"),
   path('login/facebook/',FacebookBasedLogin.as_view(),name="facebook_login"),
   path('user/<id>/makeadmin/',MakeConsumerAdmin.as_view(),name="makeadmin"),
   path('search/<x>/',Search.as_view(),name="search"),
   path('statistics/',Statistics.as_view(),name="user-statistics"),
   path('genAPIKey/',GenerateApiKey.as_view(),name="gen_apikey"),
   path('', include('social_django.urls', namespace='social'))
]

urlpatterns+=router.urls
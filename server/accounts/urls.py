from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (CurrentUser,
                    Search,
                    Statistics,
                    GenerateApiKey,
                    MakeConsumerAdmin,
                    Requests,
                    google_auth_token)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'users'

router = DefaultRouter()
router.register(r'user', CurrentUser, basename='user')


urlpatterns = [
   path('login/google/',google_auth_token,name="login_google"),
   path('login/password/', TokenObtainPairView.as_view(), name='login_password'),
   path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
   path('user/<id>/makeadmin/',MakeConsumerAdmin.as_view(),name="makeadmin"),
   path('search/<x>/',Search.as_view(),name="search"),
   path('statistics/',Statistics.as_view(),name="user-statistics"),
   path('requests/',Requests.as_view(),name="user-requests"),
   path('genAPIKey/',GenerateApiKey.as_view(),name="gen_apikey")
]

urlpatterns+=router.urls
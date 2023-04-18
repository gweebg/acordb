from django.urls import path
from .views import AllUsers,CurrentUser,CreateAdministrator,CreateConsumer

app_name = 'users'

urlpatterns = [
   path('create/administrator/', CreateAdministrator.as_view(), name="create_administrator"),
   path('create/consumer/', CreateAdministrator.as_view(), name="create_consumer"),
   path('all/', AllUsers.as_view(), name="all"),
   path('currentUser/', CurrentUser.as_view(), name="current"),
   ]
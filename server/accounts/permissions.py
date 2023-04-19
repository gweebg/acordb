from rest_framework import permissions
from .models import Consumer,Administrator

class IsConsumer(permissions.BasePermission):
    message = 'Must be a consumer to access this endpoint.'

    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return Consumer.objects.filter(account=user).exists()
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        if isinstance(obj,Consumer):
            return obj.account==user
                    
    
class IsAdministrator(permissions.BasePermission):
    message = 'Must be Administrator to access this endpoint.'

    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return Administrator.objects.filter(account=user).exists()
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user is None or not user.is_authenticated:
           return False
        if isinstance(obj,Administrator):
            return obj.account==user
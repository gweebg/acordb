from rest_framework import permissions
from accounts.models import Administrator
from .models import Record

class IsAdministrator(permissions.BasePermission):
    message = 'Must be Administrator to access this endpoint.'

    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        administrator = Administrator.objects.get(account=user)
        return Administrator.objects.filter(account=user).exists()
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user is None or not user.is_authenticated:
           return False
        administrator = Administrator.objects.get(account=user)
        if isinstance(obj,Record):
            return obj.added_by==administrator
        return False
        
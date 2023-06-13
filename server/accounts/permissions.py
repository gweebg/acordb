from rest_framework import permissions
from .models import Account

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method=='POST':
            return True
        if user is None or not user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:  # Allows GET, HEAD, OPTIONS requests
            return True
        if isinstance(obj,Account):
            return obj==user
        return False
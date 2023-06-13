from rest_framework import permissions
from accounts.models import Account
from .models import Record,ChangeRequest

class IsAdministrator(permissions.BasePermission):
    message = 'Must be Administrator to access this endpoint.'

    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return user.is_administrator
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request,view)

class IsConsumer(permissions.BasePermission):
    message = 'Must be Consumer to access this endpoint.'
    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return not user.is_administrator
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        elif not isinstance(ChangeRequest,obj): return False
        else: return obj.sujested_by==user
        
        
class BelongsToUser(permissions.BasePermission):
    message = 'Must the be the owner of this object'
    def has_permission(self,request,view):
        return True
    def has_object_permission(self,request,view,obj):
        print("ON")
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        elif not isinstance(ChangeRequest,obj): return False
        else: return obj.sujested_by==user
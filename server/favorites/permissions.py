from rest_framework import permissions
class FavoritesPermission(permissions.IsAuthenticated):
    message = 'Must be authenticated and have access to the favorite to access this endpoint.'

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not self.has_permission(request, view):
            return False
        if request.method == 'POST':
            return True
        return bool(obj.user==user)
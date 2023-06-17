from .models import APIKey
from rest_framework.authentication import BaseAuthentication

class APIKeyAuthenticationBackend(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')
        if api_key:
            try:
                key = APIKey.objects.get_from_key(api_key)
                return key.user, None
            except APIKey.DoesNotExist:
                pass
        return None
from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Favorites
from records.models import Record

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorites
        fields=('processo','description','id')
        extra_kwargs={'id':{'read_only':True}}

    def validate_processo(self, value):
        # Check if a Record with the given processo exists
        if not Record.objects.filter(processo=value).exists():
            raise serializers.ValidationError("A Record with this processo does not exist.")
        return value
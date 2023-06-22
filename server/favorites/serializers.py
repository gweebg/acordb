from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Favorites
import uuid
from records.models import Acordao

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorites
        fields=('acordao','description','id')
        extra_kwargs={'id':{'read_only':True}}

    def validate_acordao(self, value):
        # Check if a Record with the given processo exists
        if not Acordao.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("A Acordao with this value does not exist.")
        return value
from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Favorites

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorites
        fields=('user','record','description','id')
        extra_kwargs={'user':{'write_only':True},'id':{'read_only':True}}
from .models import Tag,Field
from rest_framework import serializers
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=('name',)
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model=Field
        fields=('name',)
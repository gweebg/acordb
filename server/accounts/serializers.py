from rest_framework import serializers
from .models import Account


class PasswordBasedLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('username','password')
        extra_kwargs={'password':{'write_only':True}} 
class SocialMediaLoginSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True,required=True)

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('id','email','password','first_name','last_name','filiation','is_administrator')
        extra_kwargs={'password':{'write_only':True},'id':{'read_only':True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
    
    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        if self.context['view'].action == 'update' or self.context['view'].action == 'partial_update':  # Check if the action is 'update'
            extra_kwargs['is_administrator'] = {'read_only': True}
        return extra_kwargs


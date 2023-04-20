from rest_framework import serializers
from .models import Administrator,Consumer,Account


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
        fields=('id','email','password','first_name','last_name','filiation')
        extra_kwargs={'password':{'write_only':True},'id':{'read_only':True}}  

class AdministratorSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model=Administrator
        fields=('account',)
    def create(self,validated_data):
        instance=self.Meta.model.objects.create_administrator(**validated_data["account"])
        return instance

class ConsumerSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model=Consumer
        fields=('account',)
    def create(self,validated_data):
        instance=self.Meta.model.objects.create_consumer(**validated_data["account"])
        return instance


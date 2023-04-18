from rest_framework import serializers
from .models import Administrator,Consumer,Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('email','first_name','last_name','filiation')

class AdministratorSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model=Administrator
        fields=('account',)

class ConsumerSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model=Consumer
        fields=('account',)

class AccountRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('email','password','first_name','last_name','filiation')
        extra_kwargs={'password':{'write_only':True}}  
class AdministratorRegistrationSerializer(serializers.ModelSerializer):
    account = AccountRegistrationSerializer()
    class Meta:
        model=Administrator
        fields=('account',)

    def create(self,validated_data):
        instance=self.Meta.model.objects.create_administrator(**validated_data["account"])
        return instance

class ConsumerRegistrationSerializer(serializers.ModelSerializer):
    account = AccountRegistrationSerializer()
    class Meta:
        model=Consumer
        fields=('account',)

    def create(self,validated_data):
        instance=self.Meta.model.objects.create_administrator(**validated_data["account"])
        return instance
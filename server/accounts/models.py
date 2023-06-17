from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from rest_framework_api_key.models import AbstractAPIKey,BaseAPIKeyManager
from django.utils.translation import gettext_lazy as _



class CustomAccountManager(BaseUserManager):
    def create_account(self,email,first_name,last_name,password,filiation):
        if not email:
            raise ValueError(_('Please provide an email address'))
        if not first_name:
            raise ValueError(_('Please provide a first name'))
        if not last_name:
            raise ValueError(_('Please provide a last name'))
        if not password:
            raise ValueError(_('Please provide a password'))
        if not filiation:
            filiation=""

        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,last_name=last_name,filiation=filiation,username=email)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,first_name,last_name,password,**kwargs):
        if not email:
            raise ValueError(_('Please provide an email address'))
        if not first_name:
            raise ValueError(_('Please provide a first name'))
        if not last_name:
            raise ValueError(_('Please provide a last name'))
        if not password:
            raise ValueError(_('Please provide a password'))

        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,last_name=last_name,filiation="",is_staff=True,is_superuser=True,username=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_administrator(self,email,first_name,last_name,password,filiation):
        account = self.create_account(email, first_name, last_name, password, filiation)
        account.is_administrator = True
        account.save()
        return account
    
    def create_consumer(self,email,first_name,last_name,password,filiation):
        account = Account.objects.create_account(email, first_name, last_name, password, filiation)
        account.is_administrator = False
        account.save()
        return account
    
class Account(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    username= models.CharField(_('User Name'),max_length=150)
    first_name = models.CharField(_('First Name'),max_length=150)
    last_name = models.CharField(_('Last Name'),max_length=150)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    filiation = models.CharField(max_length=150,blank=True)
    is_administrator =models.BooleanField(default=False)
    created_at = models.DateTimeField(_('Created At'), default=timezone.now)

    objects=CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    def __str__(self):
        return self.email
    
    
class APIKeyManager(BaseAPIKeyManager):
    def create_newkey(self,**data):
        user=data.get('user')
        currKey = self.filter(user=user).first()
        if currKey is not None:
            currKey.delete()
        return self.create_key(**data)
    
class APIKey(AbstractAPIKey):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    objects = APIKeyManager()
    
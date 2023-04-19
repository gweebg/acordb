from django.db import models
from ..accounts.models import Account
from ..records.models import Record

class CustomFavoritesManager(models.Manager):
    def create_favorite(self,username,record,description):
        if not username:
            raise ValueError(_('Please provide a username'))
        if not record:
            raise ValueError(_('Please provide a first name'))
        if not description:
            description=""
        user = Account.objects.get(username=username)
        if not user:
            raise ValueError(_('Please provide a existing username'))
        record = Record.objects.get(id=record)
        if not record:
            raise ValueError(_('Please provide a existing record'))
        favorite = self.model(user=user,record=record,description=description)
        favorite.save()
        return favorite



class Favorites(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,primary_key=True)
    record = models.ForeignKey(Record, on_delete=models.CASCADE,primary_key=True)
    description = models.CharField(max_length=150,blank=True) 
# Create your models here.

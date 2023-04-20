from django.db import models
from accounts.models import Account
from records.models import Record

class CustomFavoritesManager(models.Manager):
    def create_favorite(self,user,record,description):
        if not user:
            raise ValueError(_('Please provide a user'))
        if not record:
            raise ValueError(_('Please provide a record'))
        if not description:
            description=""
        user = Account.objects.get(pk=user)
        if not user:
            raise ValueError(_('Please provide a existing user'))
        record = Record.objects.get(pk=record)
        if not record:
            raise ValueError(_('Please provide a existing record'))
        favorite = self.model(user=user,record=record,description=description)
        favorite.save()
        return favorite



class Favorites(models.Model):
    #id will be the primary key
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    description = models.CharField(max_length=150,blank=True) 
    class Meta:
        unique_together = (("user", "record"),)
# Create your models here.

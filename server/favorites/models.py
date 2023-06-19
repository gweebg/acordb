from django.db import models
from accounts.models import Account
from records.models import Record
from rest_framework import serializers

class CustomFavoritesManager(models.Manager):
    def create_favorite(self,user,processo,description):
        if not user:
            raise ValueError(_('Please provide a user'))
        if not processo:
            raise ValueError(_('Please provide a processo'))
        if not description:
            description=""
        user = Account.objects.get(pk=user)
        if not user:
            raise ValueError(_('Please provide a existing user'))
        favorite = self.model(user=user,processo=processo,description=description)
        favorite.save()
        return favorite



class Favorites(models.Model):
    #id will be the primary key
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    processo = models.CharField(max_length=32)
    description = models.CharField(max_length=255,blank=True)
    class Meta:
        unique_together = (("user", "processo"),)

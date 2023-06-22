from django.db import models
from accounts.models import Account
from records.models import Acordao
from rest_framework import serializers

class CustomFavoritesManager(models.Manager):
    def create_favorite(self,user,acordao,description):
        if not user:
            raise ValueError(_('Please provide a user'))
        if not acordao:
            raise ValueError(_('Please provide a acordao'))
        if not description:
            description=""
        user = Account.objects.get(pk=user)
        if not user:
            raise ValueError(_('Please provide a existing user'))
        acordao = Acordao.objects.get(pk=acordao)
        favorite = self.model(user=user,acordao=acordao,description=description)
        favorite.save()
        return favorite



class Favorites(models.Model):
    #id will be the primary key
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    acordao = models.ForeignKey(Acordao, on_delete=models.CASCADE)
    description = models.CharField(max_length=255,blank=True)
    class Meta:
        unique_together = (("user", "acordao"),)

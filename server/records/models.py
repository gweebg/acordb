from django.db import models
from django.conf import settings
from accounts.models import Administrator,Consumer
import uuid 
from abc import ABCMeta, abstractmethod

# Create your models here.

class Record(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    added_by = models.ForeignKey(Administrator, on_delete=models.CASCADE,null=True,default=None,blank=True)
    
class ChangedRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ChangeRequest(models.Model):
    changedRecord = models.OneToOneField(ChangedRecord, on_delete=models.CASCADE,primary_key=True)
    sujested_by = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

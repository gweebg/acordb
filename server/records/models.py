from django.db import models
from django.conf import settings
from accounts.models import Administrator,Consumer
import uuid 
from abc import ABCMeta, abstractmethod

# Create your models here.

''' class RecordManager(models.Manager):
    db=settings.mongodb['records']
    
    def create(self,data,added_by=None):
        if not data:
            raise ValueError(_('Please provide data'))
        if not isinstance(data, dict):
            raise ValueError(_('The data must be a dictionary'))
        if 'Processo' not in data:
            raise ValueError(_('data must contain process'))
        if added_by is not None and not isinstance(added_by, Administrator):
            raise ValueError(_('Added by must be an Administrator'))
        data['_id']=data['Processo']
        del data['Processo']
        self.db.insert_one(data)
        if added_by is None:
            record=self.model(id=data['_id'])
        else:
            record=self.model(id=data['_id'],added_by=added_by)
        record.save()
        return record '''
    
    


class Record(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    added_by = models.ForeignKey(Administrator, on_delete=models.CASCADE,null=True,default=None,blank=True)
    
class ChangedRecord(models.Model):
    #id will be automaticly added
    pass

class ChangeRequest(models.Model):
    changedRecord = models.OneToOneField(ChangedRecord, on_delete=models.CASCADE,primary_key=True)
    sujested_by = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

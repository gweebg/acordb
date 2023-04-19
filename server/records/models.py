from django.db import models
from ..accounts.models import Administrator,Consumer
import uuid 

# Create your models here.


class Record(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    added_by = models.ForeignKey(Administrator, on_delete=models.CASCADE,null=True,default=None)
    
class ChangedRecord(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)

class ChangeRequest(models.Model):
    changedRecord = models.OneToOneField(ChangedRecord, on_delete=models.CASCADE,primary_key=True)
    sujested_by = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

from django.db import models
from django.conf import settings
from accounts.models import Account
import uuid
import bson
from django.utils import timezone
from abc import ABCMeta, abstractmethod
from .mongo import createRecord,getManyRecords,getOneRecord,updateRecord,deleteRecord
from .mongo import createchangeRequest,getOnechangeRequest,deletechangeRequest
from django.db.models import Max

# Create your models here.

class TagManager(models.Manager):
    def get_or_create(self,name):
        tag = self.filter(name=name).first()
        if tag is None:
            tag=self.model(name=name)
            tag.save()
        return tag

class Tag(models.Model):
    name = models.CharField(max_length=128,primary_key=True)
    objects = TagManager()
    

def recordSerializer(record,record_data):
    del record_data['_id']
    return {
                "id":str(record.id),
                "added_by":str(record.added_by),
                "added_at":record.added_at.strftime("%H:%M:%S %d/%m/%Y"),
                "tags":[i.name for i in record.tags.all()],
                "data":record_data            
            }
    



class RecordManager(models.Manager):
    def create(self,data,user):
        if 'Processo' in data and 'Descritores' in data:
            rec=self.model(processo=data['Processo'],added_by=user)
            descritores = data.pop("Descritores")
            tags = [Tag.objects.get_or_create(name=descritor) for descritor in descritores]
            data["_id"]=bson.Binary.from_uuid(rec.id)
            r=createRecord(data)
            if r is not None:
                rec.save()
                rec.tags.set(tags)
                rec.save()
                return recordSerializer(rec,r)
        return None
    
    def getMostRecentMany(self,query):
        records = getManyRecords(query)
        r=[]
        for record_data in records:
            record=self.get(id=uuid.UUID(bytes=record_data["_id"]))
            most_recent_added_at = Record.objects.filter(processo=record.processo).aggregate(Max("added_at"))["added_at__max"]
            if record.added_at==most_recent_added_at:
                r.append(recordSerializer(record,record_data))
        return r
    
    def getMany(self,query):
        records = getManyRecords(query)
        r=[]
        for record_data in records:
            record=self.get(id=uuid.UUID(bytes=record_data["_id"]))
            r.append(recordSerializer(record,record_data))
        return r
    
    def getOne(self,processo):
        records=self.filter(processo=processo).order_by('-added_at')
        if records is not None:
            r=[]
            for record in records:
                record_data = getOneRecord(bson.Binary.from_uuid(record.id))
                r.append(recordSerializer(record,record_data))
            return r
        return None

        
class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    processo = models.CharField(max_length=32)
    added_by = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,default=None,blank=True)
    added_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    objects = RecordManager()            

    

def changeRequestSerializer(changeRequest,request_data):
    del request_data['_id']
    return {
                'id':changeRequest.id,
                'sujested_by':str(changeRequest.sujested_by),
                'processo':changeRequest.processo,
                'added_at':changeRequest.added_at.strftime("%H:%M:%S %d/%m/%Y"),
                'status':changeRequest.status,
                'reviewer':str(changeRequest.reviewer) if changeRequest.reviewer else None,
                'data':request_data
                }



    
class ChangeRequestManager(models.Manager):
    
    def create(self,processo,data,user):
        if not Record.objects.filter(processo=processo).exists():
            return None
        changeRequest=self.model(processo=processo,sujested_by=user)
        data['_id']=bson.Binary.from_uuid(changeRequest.id)
        request_data=createchangeRequest(data)
        if request_data is None:
            return None
        else:
            changeRequest.save()
            return changeRequestSerializer(changeRequest,request_data)
    
    def getRequests(self,processo):
        requests=self.filter(processo=processo).order_by('-added_at')
        if requests is None:
            return None
        r=[]
        for request in requests:
            request_data=getOnechangeRequest(bson.Binary.from_uuid(request.id))
            r.append(changeRequestSerializer(request,request_data))
        return r
    
    def getRequest(self,request):
        changeRequest=self.get(id=request)
        if changeRequest is None:
            return None
        else:
            request_data=getOnechangeRequest(bson.Binary.from_uuid(changeRequest.id))
            return changeRequestSerializer(changeRequest,request_data)
    def acceptRequest(self,request,user):
        changeRequest=self.get(id=request)
        if changeRequest is None or changeRequest.status!='pending':
            return None
        else:
            changeRequest.status='accepted'
            changeRequest.reviewer=user
            changeRequest.save()
            request_data=getOnechangeRequest(bson.Binary.from_uuid(changeRequest.id))
            Record.objects.create(request_data,changeRequest.sujested_by)
            return changeRequestSerializer(changeRequest,request_data)
        
    def denyRequest(self,request,user):
        changeRequest=self.get(id=request)
        if changeRequest is None or changeRequest.status!='pending':
            return None
        else:
            changeRequest.status='denied'
            changeRequest.reviewer=user
            changeRequest.save()
            request_data=getOnechangeRequest(bson.Binary.from_uuid(changeRequest.id))
            return changeRequestSerializer(changeRequest,request_data)
        
    def deleteRequest(self,request):
        changeRequest=self.get(id=request)
        if changeRequest is not None:
            if changeRequest.status=='pending':
                request_data = getOnechangeRequest(bson.Binary.from_uuid(changeRequest.id))
                r=deletechangeRequest(bson.Binary.from_uuid(changeRequest.id))
                if not r :
                    return {}
                s=changeRequestSerializer(changeRequest,request_data)
                changeRequest.delete()
                return s
        return None
            
class ChangeRequest(models.Model):
    STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('pending', 'Pending'),
        ('denied', 'Denied'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sujested_by = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='sujested')
    processo = models.CharField(max_length=32)
    added_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default="pending")
    reviewer = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,default=None,related_name='reviewer')
    
    objects = ChangeRequestManager()


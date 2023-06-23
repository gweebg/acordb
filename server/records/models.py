from django.db import models
from django.conf import settings
from accounts.models import Account
import uuid
import bson
from django.utils import timezone
from abc import ABCMeta, abstractmethod
from .mongo import createRecord,getManyRecords,getOneRecord,updateRecord,deleteRecord,createManyRecord,getMostRecentRecords
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
    
    def createIfNotExists(self,data:set):
        existing_tags = self.filter(name__in=data)
        existing_names = set(tag.name for tag in existing_tags)
        c=[]
        for d in data:
            if d not in existing_names:
                c.append(self.model(name=d))
        self.bulk_create(c) 
            
    def get_or_createMany(self,data_list):
        data_list=set(data_list)
        existing_tags = self.filter(name__in=data_list)
        existing_names = set(tag.name for tag in existing_tags)

        objects_to_create = []
        for data in data_list:
            if data not in existing_names:
                objects_to_create.append(self.model(name=data))

        created_objects = self.bulk_create(objects_to_create)
        created_objects = self.filter(pk__in=[obj.pk for obj in created_objects])
        all_objects = existing_tags | created_objects
        return all_objects

class Tag(models.Model):
    name = models.CharField(max_length=512,primary_key=True)
    objects = TagManager()

class FieldManager(models.Manager):
    def get_or_create(self,name):
        field = self.filter(name=name).first()
        if field is None:
            field=self.model(name=name)
            field.save()
        return field
    
    def createIfNotExists(self,data:set):
        existing_fields = self.filter(name__in=data)
        existing_names = set(tag.name for tag in existing_fields)
        c=[]
        for d in data:
            if d not in existing_names:
                c.append(self.model(name=d))
        self.bulk_create(c) 
    
    def get_or_createMany(self,data_list):
        data_list=set(data_list)
        existing_fields = self.filter(name__in=data_list)
        existing_names = set(field.name for field in existing_fields)

        objects_to_create = []
        for data in data_list:
            if data not in existing_names:
                objects_to_create.append(self.model(name=data))

        created_objects = self.bulk_create(objects_to_create)
        created_objects = self.filter(pk__in=[obj.pk for obj in created_objects])
        all_objects = existing_fields | created_objects
        return all_objects

class Field(models.Model):
    name = models.CharField(max_length=265,primary_key=True)
    objects = FieldManager()
    


    
    
class Acordaomanager(models.Manager):
    def create(self,data,user):
        c=self.model()
        c.save()
        return Record.objects.create(c,data,user)
    def createMany(self,data,user):
        acordaos=[]
        pairs=[]
        for datat in data:
            c=self.model()
            acordaos.append(c)
            pairs.append((c,datat))
        Acordao.objects.bulk_create(acordaos)
        Record.objects.createMany(pairs,user)
        
        
    
    def getOne(self,id):
        try:
            acordao = self.get(id=id)
            most_recent_record = acordao.record_set.aggregate(max_added_at=Max('added_at'))
            return Record.objects.getOne(acordao.record_set.get(added_at=most_recent_record['max_added_at']).id)
        except Acordao.DoesNotExist:
            # Handle the case when Acordao with the given ID does not exist
            return None
        except Record.DoesNotExist:
            # Handle the case when there are no records for the given Acordao
            return None
        
    def getMany(self,query):
        return Record.objects.getMostRecentMany(query)
            
        
        
    
    
class Acordao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objects=Acordaomanager()
    

def recordSerializer(record,record_data):
    del record_data['_id']
    del record_data['id_acordao']
    del record_data['record_added_at']
    return {
                "id":str(record.id),
                "added_by":str(record.added_by),
                "added_at":record.added_at.strftime("%H:%M:%S %d/%m/%Y"),
                "acordao":str(record.acordao.id),
                "tags":[i.name for i in record.tags.all()],
                "data":record_data            
            }
    
class RecordManager(models.Manager):
    def create(self,acordao,data,user):
        try:
            data=data.dict()
        except:
            pass
        if 'Descritores' not in data:
            data['Descritores']=[]
        rec=self.model(acordao=acordao,added_by=user)
        descritores = data.pop("Descritores")
        fields = [Field.objects.get_or_create(name=key) for key in data.keys()]
        tags = [Tag.objects.get_or_create(name=descritor) for descritor in descritores]
        data["_id"]=bson.Binary.from_uuid(rec.id)
        data["id_acordao"]=bson.Binary.from_uuid(acordao.id)
        data["record_added_at"]=rec.added_at
        r=createRecord(data)
        if r is not None:
            rec.save()
            rec.tags.set(tags)
            rec.fields.set(fields)
            rec.save()
            return recordSerializer(rec,r)
        return None
        
    
    def createMany(self,acordaoData,user):
        mongoData=[]
        records=[]
        fields=[]
        tags=[]
        stags=set()
        sfields=set()

        for (acordao,data) in acordaoData:
            try:
                data=data.dict()
            except:
                pass
            if 'Descritores' not in data:
                data['Descritores']=[]
            rec=self.model(acordao=acordao,added_by=user)
            records.append(rec)
            descritores = data.pop("Descritores")
            fields.append(list(data.keys()))
            for field in data.keys():
                sfields.add(field)
            tags.append(descritores)
            for tag in descritores:
                stags.add(tag)
            data["_id"]=bson.Binary.from_uuid(rec.id)
            data["id_acordao"]=bson.Binary.from_uuid(acordao.id)
            data["record_added_at"]=rec.added_at
            mongoData.append(data)
        print("Creating Records")
        Record.objects.bulk_create(records)
        print("Creating Tags")
        Tag.objects.createIfNotExists(stags)
        print("Creating Fields")
        Field.objects.createIfNotExists(sfields)
        print("Atributing Tags and Fields")
        for p,rec in enumerate(records):
            rec.tags.set(Tag.objects.filter(name__in=tags[p]))
            rec.fields.set(Field.objects.filter(name__in=fields[p]))
        print("starting MongoInsertion")
        createManyRecord(mongoData)
            
    
    def getMostRecentMany(self,query):
        records = getMostRecentRecords(query)
        r=[]
        for record in records:
            r.append(recordSerializer(self.filter(id=uuid.UUID(bytes=record['_id'])).first(),record))
        return r
    
    def getMany(self,acordao):
        records=self.filter(acordao=acordao)
        r=[]
        for record in records:
            r.append(recordSerializer(record,getOneRecord(bson.Binary.from_uuid(record.id))))
        return r
    
    def getOne(self,id):
        record=self.filter(id=id).first()
        if record is not None:
            record_data = getOneRecord(bson.Binary.from_uuid(record.id))
            return recordSerializer(record,record_data)
        return None

        
class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    acordao = models.ForeignKey(Acordao,on_delete=models.CASCADE)
    added_by = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,default=None,blank=True)
    added_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    fields = models.ManyToManyField(Field)
    objects = RecordManager()

    

def changeRequestSerializer(changeRequest,request_data):
    del request_data['_id']
    return {
                'id':changeRequest.id,
                'sujested_by':str(changeRequest.sujested_by),
                'acordao':str(changeRequest.acordao.id),
                'added_at':changeRequest.added_at.strftime("%H:%M:%S %d/%m/%Y"),
                'status':changeRequest.status,
                'reviewer':str(changeRequest.reviewer) if changeRequest.reviewer else None,
                'merged':str(changeRequest.merged.id) if changeRequest.merged else None,
                'data':request_data
                }



    
class ChangeRequestManager(models.Manager):
    
    def create(self,acordao,data,user):
        ac=Acordao.objects.filter(id=acordao).first()
        if ac is None:
            return None
        changeRequest=self.model(acordao=ac,sujested_by=user)
        data['_id']=bson.Binary.from_uuid(changeRequest.id)
        request_data=createchangeRequest(data)
        if request_data is None:
            return None
        else:
            changeRequest.save()
            return changeRequestSerializer(changeRequest,request_data)
    
    def sujested_by(self,consumer):
        requests=self.filter(sujested_by=consumer).order_by('-added_at')
        r=[]
        for request in requests:
            request_data=getOnechangeRequest(bson.Binary.from_uuid(request.id))
            r.append(changeRequestSerializer(request,request_data))
        return r
    
    def getAllRequests(self):
        requests=self.all().order_by('-added_at')
        r=[]
        for request in requests:
            request_data=getOnechangeRequest(bson.Binary.from_uuid(request.id))
            r.append(changeRequestSerializer(request,request_data))
        return r
    
    def getRequests(self,acordao):
        requests=self.filter(acordao=acordao).order_by('-added_at')
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
            r=Record.objects.create(changeRequest.acordao,request_data,changeRequest.sujested_by)
            rec=Record.objects.get(id=r['id'])
            changeRequest.merged=rec
            changeRequest.save()
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
    acordao = models.ForeignKey(Acordao,on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default="pending")
    reviewer = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,default=None,related_name='reviewer')
    merged = models.ForeignKey(Record,on_delete=models.CASCADE,null=True,default=None)
    
    objects = ChangeRequestManager()


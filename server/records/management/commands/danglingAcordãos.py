from django.core.management.base import BaseCommand
from records.models import Acordao,Field,Tag,Record
from accounts.models import Account
from django.contrib.admin.models import LogEntry
from django.conf import settings
import os
import bson


class Command(BaseCommand):
    help = 'delete acordaos that are not used'
    
    def handle(self, *args, **options):
        user = Account.objects.filter(email="jtrl@min-just.pt").first()
        records = Record.objects.filter(added_by=user)
        records.delete()
        self.stdout.write("deleted records")
        
        
        acordaos_without_records = Acordao.objects.exclude(record__isnull=False)
        lista=list(map(lambda x:bson.Binary.from_uuid(x.id),acordaos_without_records))
        self.stdout.write("deleting mongo")
        for i in lista:
            settings.MONGO_DB['records'].delete_one({"id_acordao":i},max_time_ms=500000)
        self.stdout.write("deleted mongo")
        acordaos_without_records.delete()
        user.delete()
        
        self.stdout.write("deleted")
                        
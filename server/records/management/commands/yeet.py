from django.core.management.base import BaseCommand
from records.models import Acordao,Field,Tag
from accounts.models import Account
from django.contrib.admin.models import LogEntry
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'delete acordaos'
    
    def handle(self, *args, **options):
        LogEntry.objects.all().delete()
        Acordao.objects.all().delete()
        Field.objects.all().delete()
        Tag.objects.all().delete()
        Account.objects.filter(email__contains='@min-just.pt').delete()
        settings.MONGO_DB['records'].drop()
        settings.MONGO_DB['changeRequests'].drop()
        self.stdout.write("deleted")
                        
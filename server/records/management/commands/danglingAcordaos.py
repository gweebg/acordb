from django.core.management.base import BaseCommand
from records.models import Acordao,Field,Tag
from django.contrib.admin.models import LogEntry

import os


class Command(BaseCommand):
    help = 'delete acordaos'
    
    def handle(self, *args, **options):
        Field.objects.all().delete()
        Tag.objects.all().delete()
        LogEntry.objects.all().delete()
        Acordao.objects.all().delete()
        self.stdout.write("deleted")
                        
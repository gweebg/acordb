from django.core.management.base import BaseCommand
from accounts.models import Account
from records.models import Acordao
import json
import os



def process_file(file_path,file_name,stdout):
    administrator=Account.objects.create_administrator(f"{getName(file_name)}@min-just.pt","Tribunal",getName(file_name),"password","Tribunal")
    with open(file_path) as file:
        data = json.load(file)
        stdout.write(f"Started {file_name}")
        Acordao.objects.createMany(data,administrator)
        stdout.write(f"Ended {file_name}")

def getName(filename):
    return filename.replace("_acordaos.json","")

class Command(BaseCommand):
    help = 'creates records'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        if os.path.isfile(file_path):
            process_file(file_path, os.path.basename(file_path),self.stdout)

                        
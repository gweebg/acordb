from django.core.management.base import BaseCommand
from accounts.models import Account
from records.models import Acordao
import json
import os


#def process_file(file_path, file_name,stdout):
#    administrator=Account.objects.create_administrator(f"{getName(file_name)}@min-just.pt","Tribunal",getName(file_name),"password","Tribunal")
#    with open(file_path) as file:
#        data = json.load(file)
#        stdout.write(f"Started {file_name}")
#        for item in data:
#            Acordao.objects.create(item,administrator)
#        stdout.write(f"Ended {file_name}")

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
        parser.add_argument('folder_path', type=str, help='Path to the folder')

    def handle(self, *args, **options):
        folder_path = options['folder_path']
        
        if not os.path.isdir(folder_path):
            self.stdout.write(self.style.ERROR(f"The provided path '{folder_path}' is not a valid folder."))
            return

        files = os.listdir(folder_path)
        
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                process_file(file_path, file_name,self.stdout)

                        
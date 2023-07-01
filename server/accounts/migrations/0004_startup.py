from django.db import migrations
from django.conf import settings
from ..models import Account

class Migration(migrations.Migration):
    dependencies = [
      ('accounts','0003_remove_account_apikey_apikey')
    ] # can also be emtpy if it's your first migration

    def generate_superuser(apps, schema_editor):
        Account.objects.create_superuser('admin@admin.pt','admin','admin','admin')
        
    operations = [
        migrations.RunPython(generate_superuser),
    ]
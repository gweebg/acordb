from django.db import migrations
from django.conf import settings
from ..models import Account

class Migration(migrations.Migration):
    dependencies = [
      ('accounts','0003_remove_account_apikey_apikey'),
      ('oauth2_provider','0006_alter_application_client_secret'),
    ] # can also be emtpy if it's your first migration

    def generate_superuser(apps, schema_editor):
        Application = apps.get_model('oauth2_provider', 'Application')
        Account.objects.create_superuser('admin@admin.pt','admin','admin','admin')
        Application.objects.create(
            name='App',
            client_id=settings.DEFAULT_CLIENT_ID,
            client_secret=settings.DEFAULT_CLIENT_SECRET,
            authorization_grant_type='password'
        )
        
    operations = [
        migrations.RunPython(generate_superuser),
    ]
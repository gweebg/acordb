from django.contrib import admin
from accounts.models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Account,AccountAdmin)
    

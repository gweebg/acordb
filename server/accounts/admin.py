from django.contrib import admin
from accounts.models import Account,Administrator,Consumer

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    
    pass
admin.site.register(Account,AccountAdmin)

class AdministratorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Administrator,AdministratorAdmin)

class ConsumerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consumer,ConsumerAdmin)


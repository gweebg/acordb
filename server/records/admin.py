from django.contrib import admin
from .models import Record,ChangeRequest

# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record,RecordAdmin)

class ChangeRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChangeRequest,ChangeRequestAdmin)
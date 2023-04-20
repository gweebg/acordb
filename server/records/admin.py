from django.contrib import admin
from .models import Record,ChangedRecord,ChangeRequest

# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    
    pass
admin.site.register(Record,RecordAdmin)
class ChangedRecordAdmin(admin.ModelAdmin):
    
    pass
admin.site.register(ChangedRecord,ChangedRecordAdmin)
class ChangeRequestAdmin(admin.ModelAdmin):
    
    pass
admin.site.register(ChangeRequest,ChangeRequestAdmin)
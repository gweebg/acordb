from django.contrib import admin
from .models import Record,ChangeRequest,Tag

# Register your models here.

class TagManager(admin.ModelAdmin):
    pass
admin.site.register(Tag,TagManager)

class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record,RecordAdmin)

class ChangeRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChangeRequest,ChangeRequestAdmin)
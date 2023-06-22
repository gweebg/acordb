from django.contrib import admin
from .models import Record,ChangeRequest,Tag,Field,Acordao

# Register your models here.

class TagManager(admin.ModelAdmin):
    pass
admin.site.register(Tag,TagManager)
class FieldManager(admin.ModelAdmin):
    pass
admin.site.register(Field,FieldManager)

class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record,RecordAdmin)

class AcordaoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Acordao,AcordaoAdmin)

class ChangeRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChangeRequest,ChangeRequestAdmin)
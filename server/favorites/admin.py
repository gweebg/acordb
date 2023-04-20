from django.contrib import admin
from .models import Favorites

# Register your models here.
class FavoriteAdmin(admin.ModelAdmin):
    
    pass
admin.site.register(Favorites,FavoriteAdmin)
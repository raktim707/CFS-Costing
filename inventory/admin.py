from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(StandardPart)
class StandardPartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StandardPart._meta.get_fields()]
    search_fields = ['dwg_no', 'model_no', 'Manufacturer']
    list_filter = ['dwg_no', 'model_no', 'Manufacturer']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'Formula']


admin.site.register(PrimaryProcess)
admin.site.register(SecondaryProcess)

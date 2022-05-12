from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

# Register your models here.


@admin.register(StandardPart)
class StandardPartAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['dwg_no', 'model_no', 'Manufacturer',
                    'quantity', 'price_per_unit', 'total_price_sgd']
    search_fields = ['dwg_no', 'model_no', 'Manufacturer']
    list_filter = ['dwg_no', 'model_no', 'Manufacturer']


@admin.register(MaterialConfiguration)
class MaterialAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'price', 'Formula']


admin.site.register(PrimaryProcess)
admin.site.register(Material)
admin.site.register(SecondaryProcess)
admin.site.register(RFQEntry)
admin.site.register(MaterialCost)

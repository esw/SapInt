from django.contrib import admin
from sapcat.models import *

class CentroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cod_sap')

class TipoMaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    
class ParamsMaterialAdmin(admin.ModelAdmin):
    list_display = ('tipo_mat','indt_sect','base_uom','matl_grp','division')

#class RefLegacyAdmin(admin.ModelAdmin):
#    list_display = ('sistema','ref_legacy','referencia')
#    search_fields = ('ref_legacy',)
#    list_filter = ['sistema']

admin.site.register(Centro, CentroAdmin)
admin.site.register(TipoMaterial, TipoMaterialAdmin)
admin.site.register(ParamsMaterial, ParamsMaterialAdmin)

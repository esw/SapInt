from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from aluminio.models import *

class TipoAcabadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cons_calc', 'primer','d_clear','prod_scheduler','texto_lista')
    list_filter = ('primer',)

class GrupoValoracionAdmin(admin.ModelAdmin):
    list_display = ('codigo','valor_total','peso_total_kg')

class AcabadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo','prod_alutions','prod_scheduler','grupo_mat','cod_sap_mat')
    list_filter = ('tipo','prod_alutions')
    search_fields = ['nombre']
    
class AleacionAdmin(admin.ModelAdmin):
    list_display = ('codigo','especial')

class TempleAdmin(admin.ModelAdmin):
    list_display = ('codigo',)

class UbicacionSapAdmin(admin.ModelAdmin):
    list_display = ('codigo','area',)

class ReferenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre','aleacion_std','temple_std','peso_lineal','perim_exp','perim_total','unbw')
    search_fields = ['nombre']
    list_filter = ('unbw','aleacion_std','temple_std')

class ReferenciaSAntAdmin(admin.ModelAdmin):
    list_display = ('sistema','ref_ant','peso_lineal','referencia')
    list_filter = ('sistema',)
    search_fields = ['ref_ant']

class AcabadoSAntAdmin(admin.ModelAdmin):
    list_display = ('sistema','acab_ant','acabado')
    list_filter = ('sistema',)
    search_fields = ['acab_ant']
    
class TochoAdmin(admin.ModelAdmin):
    list_display = ('tipo','aleacion','cod_sap')
    list_filter = ('tipo','aleacion',)
    search_fields = ['cod_sap']
    
class UbicacionSAntAdmin(admin.ModelAdmin):
    list_display = ('sistema','ubicacion_ant','ubicacion_sap')
    list_filter = ('sistema',)
    search_fields = ['ubicacion_ant']

def make_sin_cargar(modeladmin, request, queryset):
    queryset.update(cargado=False, cod_sap=None)
make_sin_cargar.short_description = "Cambiar estado a Sin Cargar los seleccionados"

def make_cargado(modeladmin, request, queryset):
    queryset.update(cargado=True)
make_cargado.short_description = "Cambiar estado de Cargado a los seleccionados"

class SapAluminioAdmin(admin.ModelAdmin):
    list_display = ('id','cod_sap','referencia','aleacion','temple','acabado','largo_mm','peso_lineal','peso_kg','tipo_mat','cargado')
    list_filter = ('cargado','tipo_mat','aleacion','temple','acabado')
    search_fields = ['cod_sap']
    exclude = ('cargado','cod_sap')
    actions = [make_sin_cargar]

class SaldoWmsAdmin(admin.ModelAdmin):
    list_display = ('id','codigo','referencia','acabado','largo_mm','ubicacion','cant','peso_lineal','peso_kg','peso_total_kg','tipo_mat','grupo_val')
    list_filter = ('tipo_mat','aleacion','temple','grupo_val','acabado',)
    

admin.site.register(TipoAcabado,TipoAcabadoAdmin)
admin.site.register(GrupoValoracion,GrupoValoracionAdmin)
admin.site.register(Acabado, AcabadoAdmin)
admin.site.register(Aleacion, AleacionAdmin)
admin.site.register(Temple, TempleAdmin)
admin.site.register(Referencia, ReferenciaAdmin)
admin.site.register(Tocho, TochoAdmin)
admin.site.register(UbicacionSap,UbicacionSapAdmin)
admin.site.register(ReferenciaSAnt, ReferenciaSAntAdmin)
admin.site.register(AcabadoSAnt, AcabadoSAntAdmin)
admin.site.register(UbicacionSAnt,UbicacionSAntAdmin)
admin.site.register(SapAluminio, SapAluminioAdmin)
admin.site.register(SaldoWms, SaldoWmsAdmin)
#admin.site.register(, )



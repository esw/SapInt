from django.contrib import admin
from aluminio.models import *

class AcabadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    
class ReferenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre','aleacion_std','temple_std','peso_lineal')
    list_filter = ['aleacion_std','temple_std']
    search_fields = ('nombre',)

class RefLegacyAdmin(admin.ModelAdmin):
    list_display = ('sistema','ref_legacy','referencia')
    search_fields = ('ref_legacy',)
    list_filter = ['sistema']

class SapAluminioAdmin(admin.ModelAdmin):
    list_display = ('referencia','acabado','aleacion','temple','largo_mm','desc','len_desc','cod_sap','tipo_mat')
    list_filter = ['tipo_mat','acabado','aleacion','temple']

admin.site.register(Acabado,AcabadoAdmin)
admin.site.register(Aleacion)
admin.site.register(Temple)
admin.site.register(Referencia, ReferenciaAdmin)
admin.site.register(RefLegacy, RefLegacyAdmin)
admin.site.register(SapAluminio, SapAluminioAdmin)
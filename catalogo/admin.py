from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from catalogo.models import *

class CristalTratamientoAdmin(admin.ModelAdmin):
    list_display = ('id','desc_en','desc_es',)

class CristalColorAdmin(admin.ModelAdmin):
    list_display = ('id','desc_en','desc_es',)

class CristalAcabadoAdmin(admin.ModelAdmin):
    list_display = ('id','desc_en','desc_es',)

class CristalEspesorAdmin(admin.ModelAdmin):
    list_display = ('id','cristal_es_mm','cristal_es_in')

class CristalColorEspesorAdmin(admin.ModelAdmin):
    list_display = ('id','color','espesor','cod_sap')

class SeparadorTipoAdmin(admin.ModelAdmin):
    list_display = ('id','desc_en','desc_es',)

class SeparadorEspesorAdmin(admin.ModelAdmin):
    list_display = ('id','sep_es_mm','sep_es_in')

class SeparadorMaterialAdmin(admin.ModelAdmin):
    list_display = ('id','separador_tipo','desc_en','desc_es')
    
class CristalAdmin(admin.ModelAdmin):
    list_display = ('id','tratamiento','color','espesor','acabado_cara_int','acabado_cara_ext',)
    exclude = ('desc_in_en','desc_in_es','desc_mm_en','desc_mm_es','hash')
    
class SeparadorAdmin(admin.ModelAdmin):
    list_display = ('id','material','espesor')
    exclude = ('desc_in_en','desc_in_es','desc_mm_en','desc_mm_es','hash')
    
class ComposicionCristalAdmin(admin.ModelAdmin):
    list_display = ('id','desc_in_en','desc_in_es')
    exclude = ('desc_mm_en', 'desc_mm_es','composicion_hash')

    
admin.site.register(CristalTratamiento,CristalTratamientoAdmin)
admin.site.register(CristalColor,CristalColorAdmin)
admin.site.register(CristalEspesor,CristalEspesorAdmin)
admin.site.register(CristalColorEspesor,CristalColorEspesorAdmin)
admin.site.register(CristalAcabado,CristalAcabadoAdmin)
admin.site.register(SeparadorTipo,SeparadorTipoAdmin)
admin.site.register(SeparadorMaterial,SeparadorMaterialAdmin)
admin.site.register(SeparadorEspesor,SeparadorEspesorAdmin)
admin.site.register(Cristal,CristalAdmin)
admin.site.register(Separador,SeparadorAdmin)
admin.site.register(ComposicionCristal,ComposicionCristalAdmin)



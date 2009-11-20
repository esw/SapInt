from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms
from unidades.models import *

class UnidadTipoSistemaInlineAdmin(admin.TabularInline):
    model = UnidadTipoSistema

class SistemaMedidaAdmin(admin.ModelAdmin):
    list_display = ('ref','abrev','nombre')
    inlines = [
        UnidadTipoSistemaInlineAdmin,
    ]

class TipoUnidadAdmin(admin.ModelAdmin):
    list_display = ('ref','abrev','nombre')
    
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('ref','abrev','nombre','sistema','tipo')
    list_filter = ('sistema','tipo')

class ConversionAdminForm(forms.ModelForm):
    class Meta:
        model = Conversion
    def clean(self):
        cleaned_data = self.cleaned_data
        unidad_origen = cleaned_data.get('unidad_origen')
        unidad_destino = cleaned_data.get('unidad_destino')
        if unidad_origen == unidad_destino:
            raise forms.ValidationError(_('No se puede agregar una conversion a la misma unidad'))
        return cleaned_data

class ConversionAdmin(admin.ModelAdmin):
    form = ConversionAdminForm
    list_display = ('unidad_origen','unidad_destino','factor','sistema_origen','sistema_destino')
    

admin.site.register(SistemaMedida,SistemaMedidaAdmin)
admin.site.register(TipoUnidad,TipoUnidadAdmin)
admin.site.register(UnidadMedida,UnidadMedidaAdmin)
admin.site.register(Conversion,ConversionAdmin)
from django import template

register = template.Library()

@register.inclusion_tag('base/form.html')
def build_form(form):
    return { 'form': form }
    
@register.inclusion_tag('base/base_form_admin.html')
def build_form_admin(form):
    return { 'form': form }

@register.inclusion_tag('base/base_formsets_admin.html')
def build_formsets_admin(formsets):
    return { 'formsets': formsets }

@register.inclusion_tag('base/form_list.html')
def build_form_list(forms,form_options):
    return { 'forms':forms,'form_options':form_options }
    
@register.inclusion_tag('base/form_formset.html')
def build_form_formset(forms,formset):
    return { 'forms':forms,'formset':formset }
    
@register.inclusion_tag('base/formset_list.html')
def build_list_formset(form_options,formsets):
    return { 'form_options':form_options,'formsets':formsets }

@register.inclusion_tag('base/form_formset_list.html')
def build_form_list_formset(form_options,form,formsets):
    return { 'form_options':form_options,'form':form,'formsets':formsets }
    
@register.inclusion_tag('base/table_formset.html')
def build_formset_table(formset):
    return { 'formset':formset }

@register.inclusion_tag('base/forms.html')
def build_forms(forms):
    return { 'forms': forms }

@register.inclusion_tag('table_header.html')
def table_header(forms):
    return { 'headers' : headers }


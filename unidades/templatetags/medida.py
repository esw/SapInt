from django.utils.translation import ugettext_lazy as _
from django import template
from unidades.models import SistemaMedida
from unidades.medida import frac_format

register = template.Library()

class FormatMedida(template.Node):
    def __init__(self,medida):
        self.medida = template.Variable(medida)
    
    def render(self, context):
        sistema = context['user'].get_profile().sistema_medida
        medida = self.medida.resolve(context)
        print "Medida=%s Id=%s" %(medida,sistema.id)
        return "%s" % (medida.get_unicode(unidad=sistema.u_tipo(medida.tipo)))

@register.tag
def format_medida(parser, token):
    try:
        tag_name, medida = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, '%r el tag requiere exactamente 1 argumento' % token.content.split()[0]
    return FormatMedida(medida)

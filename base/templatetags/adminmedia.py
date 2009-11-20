from django.template import Library

register = Library()

def admin_media_prefix():
    """
    Returns the string contained in the setting ADMIN_MEDIA_PREFIX.
    """
    try:
        from django.conf import settings
        return settings.ADMIN_MEDIA_PREFIX
    except ImportError:
        return ''
admin_media_prefix = register.simple_tag(admin_media_prefix)

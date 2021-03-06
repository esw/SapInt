import os
import os.path

import sys

# Django settings for ES project.

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(PROJECT_DIR)

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'sapint'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = 'admin'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '3306'             # Set to empty string for default. Not used with sqlite3.
    
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Bogota'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

LANGUAGES = (
    ('es', 'Espanol'),
    ('en', 'English'),
)

DEFAULT_LANGUAGE = 1

SITE_ID = 1

#AUTH_PROFILE_MODULE = 'usuarios.InfoUsuario'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR,'media')
ADMIN_MEDIA_ROOT = os.path.join(MEDIA_ROOT,'admin')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://sapint.energiasolarsa.com/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
MEDIA_PREFIX = '/site_media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

LOGIN_URL='/login'
LOGIN_REDIRECT_URL='/'

CACHE_BACKEND = "locmem:///?timeout=300&max_entries=500"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5kw)(y6kp5&#^-+(271)s^5bl!6m-ko*k#knmg0(o91*7mjgf9'
#SESSION_COOKIE_NAME = 'sessionid.navbar'

#NAVBAR_MAX_DEPTH = 2

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
#    'multilingual.context_processors.multilingual',
#    'navbar.context_processors.crumbs',
#    'navbar.context_processors.navbar',
#    'navbar.context_processors.navtree',
#    'navbar.context_processors.navbars',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
#    'multilingual.middleware.DefaultLanguageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
#    'reversion.middleware.RevisionMiddleware',
)

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/users/%s/" % o.id,
    
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
#    'multilingual',
    'base',
#    'filter',
#    'genericadmin',
    #'django_evolution',
#    'extensions',
    'unidades',
    'catalogo',
    'sapcat',
    'aluminio',
#    'threadedcomments',
#    'mailer',
#    'notification',
#    'reversion',
    'chronograph',
#    'navbar',
#    'logger',
)


#NOTIFICATION_BUILTIN_NOTICE_VIEWS = False
#NOTIFICATION_FEEDS = True
#NOTIFICATION_QUEUE_ALL = False

#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025

DELIM_CSV = '\t'

ARCH_IMP_DIR = 'imp_aluminio'
ARCH_IMP_ROOT = os.path.join(PROJECT_DIR + os.sep + ARCH_IMP_DIR)
ARCH_EXP_DIR = 'exp_aluminio'
ARCH_EXP_ROOT = os.path.join(PROJECT_DIR + os.sep + ARCH_EXP_DIR)

IMP_REFS = {
    'arch_acabados': 'acabados.txt',
    'arch_acabados_wms': 'acabados_wms.txt',
    'arch_alums': 'alums.txt',
    'arch_refs' : 'referencias.txt',
    'arch_refs_pexp' : 'referencias_pexp.txt',
    'arch_refs_wms' : 'referencias_wms.txt',
    'arch_sapalums' : 'sapalums.txt',
    'arch_ubicaciones':'ubicaciones.txt',
    'arch_ubicaciones_wms':'ubicaciones_wms.txt',
    'arch_saldos_wms': 'saldos_wms.txt',
}

L_SETTINGS_DIR = os.path.abspath(PROJECT_DIR + os.sep + '..' + os.sep + 'sapint_settings')

if os.path.exists(L_SETTINGS_DIR):
    sys.path.append(L_SETTINGS_DIR)
    try:
        from local_settings import *
    except ImportError:
        pass

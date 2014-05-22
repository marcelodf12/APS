"""
Django settings for aps project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

Requiere los paquetes
python-psycopg2
Unipath
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PATH = '/var/www/html/aps/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ahomuh^*!#m3w$udfbc*lowvu^+j84ro@fn_vc#(z!-%mi+w2y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

## Para que funcione esta linea debe hacerse pip install unipath
from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)

## Para el login
from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_URL = reverse_lazy('logout')

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicaciones.inicio',
    'aplicaciones.proyectos',
    'aplicaciones.items',
    'aplicaciones.fases',
    'aplicaciones.permisos',
    'aplicaciones.lineasBase',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'aps.urls'

WSGI_APPLICATION = 'aps.wsgi.application'

TEMPLATE_DIRS = (
    RUTA_PROYECTO.child('templates'),
)



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'projectManager',
        'USER':'postgres',
        'PASSWORD':'is2',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Archivos Dinamicos multimedia
MEDIA_ROOT = RUTA_PROYECTO.child('media')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    RUTA_PROYECTO.child('static'),
)



"""
Django settings for dk_blog project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kwho@+f9uo1dik7h96&_gb8a4nip665qww5p)qq$x*o@(f)ny2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'crispy_forms',
    'django_bootstrap_breadcrumbs',
    'user',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'dk_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dk_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {

}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'user.CustomUser'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'assets')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_URL = 'user:signin'
# Apps settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    # Set it as False to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery stuff by manually.
    # Use this when you're already using Bootstraip/jQuery based themes.
    'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '400',

        # Use proper language setting automatically (default)
        # 'lang': None,

        # Or, set editor language/locale forcely
        # 'lang': 'ko-KR',

        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/assets/css/printable.css',
        },
    },

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
    # 'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    # 'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    # must inherit 'django_summernote.AbstractAttachment'
    # 'attachment_model': 'my.custom.attachment.model',

    # You can disable attachment feature.
    'disable_attachment': False,

    # Set `True` to return attachment paths in absolute URIs.
    'attachment_absolute_uri': False,

    # You can add custom css/js for SummernoteWidget.
    'css': (
    ),
    'js': (
    ),

    # You can also add custom css/js for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'css_for_inplace': (
    ),
    'js_for_inplace': (
    ),

    # Codemirror as codeview
    # If any codemirror settings are defined, it will include codemirror files automatically.
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
    ),
    'codemirror': {
        'mode': 'htmlmixed',
        'lineNumbers': 'true',

        # You have to include theme file in 'css' or 'css_for_inplace' before using it.
        'theme': 'monokai',
    },

    # Lazy initialize
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    'lazy': False,

    # To use external plugins,
    # Include them within `css` and `js`.
    'js': {
        # '/some_static_folder/summernote-ext-print.js',
        # '//somewhere_in_internet/summernote-plugin-name.js',
    },
}

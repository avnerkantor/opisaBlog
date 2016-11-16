import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '&s^4!!#bz5!=q*i9w3xa!123cn^8@!w^nifb9em228wvb&xwf4'

INSTALLED_APPS = [
    'django.contrib.sites',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'disqus',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tikhinuch4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # 'django.core.context_processors.static',
            ],
        },
    },
]

# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',
#
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

WSGI_APPLICATION = 'tikhinuch4.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'he'
TIME_ZONE = 'Asia/Tel_Aviv'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Parse database configuration from $DATABASE_URL

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# Simplified static file serving.
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../static'),
)
SITE_ID = 1

# https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

AWS_STORAGE_BUCKET_NAME = 'opisa1'
AWS_ACCESS_KEY_ID = 'AKIAJPC2Q4AQF7ADFFPQ'
AWS_SECRET_ACCESS_KEY = '56dYfMDkkoPBhG/Mdzn4fXuUPDTsjPYGVKPtBa1S'

AWS_QUERYSTRING_AUTH = False
CKEDITOR_UPLOAD_PATH = "uploads/"
AWS_DEFAULT_ACL = 'public-read'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YouCustomToolbarConfig': [
            # {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            # {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            # {'name': 'forms',
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #            'HiddenField']},
            # '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Iframe']},
            '/',
            # {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            # {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            # {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            # {'name': 'about', 'items': ['About']},
            # '/',  # put this to force next toolbar on new line
            # {'name': 'youcustomtools', 'items': [
            #     # put the name of your editor.ui.addButton here
            #     'Preview',
            #     'Maximize',
            #
            # ]},
        ],
        'toolbar': 'YouCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # you extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}

DISQUS_API_KEY = 'o9TRCmIcdfalpU8XNOCaMGd5joWP4sIgO9qWYBqOTGCAp37mr1B5ssn59sYXx7bR'
DISQUS_WEBSITE_SHORTNAME = "tikhinuch"

try:
    from .local_settings import *
except Exception as e:
    pass
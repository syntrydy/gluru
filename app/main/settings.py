"""
Django settings for gluu project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = bool(int(os.environ.get('DEBUG', '1')))
HTTPS = bool(int(os.environ.get('HTTPS', '1')))

if HTTPS:
    os.environ['HTTPS'] = 'on'
    PROTOCOL = 'https'
else:
    PROTOCOL = 'http'


SITE_ID = 1

ALLOWED_HOSTS = ['127.0.0.1']

# Can be 1 or 2
GLUU_VERSION = os.environ.get('GLUU_VERSION')

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'res/uploads')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'res/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'res', 'staticfiles'),
)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'haystack',
    'alerts',
    'compressor',
    'search',
    'profiles',
    'tickets',
    'crispy_forms',
    'markdown_deux',
    'social.apps.django_app.default',
    'connectors.sugarcrm',
    'connectors.idp',
    'pagedown'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'main.middleware.TimezoneMiddleware',
    'main.middleware.ProfileMiddleware'
)

ROOT_URLCONF = 'main.urls'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'res', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.include_external_info',
            ],
            'debug': DEBUG
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': '',
    },
    'sugarcrm': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('SUGARCRM_NAME'),
        'USER': os.environ.get('SUGARCRM_USER'),
        'PASSWORD': os.environ.get('SUGARCRM_PASSWORD'),
        'HOST': os.environ.get('SUGARCRM_HOST'),
        'PORT': '',
    },
}

AUTHENTICATION_BACKENDS = (
    'profiles.gluu_oidc.GluuOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'profiles.UserProfile'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'connectors.sugarcrm.crm_interface.social_auth_sync_crm',
    'profiles.gluu_oidc.sync_phone_number'
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    'social.pipeline.disconnect.allowed_to_disconnect',
    'social.pipeline.disconnect.get_entries',
    'social.pipeline.disconnect.revoke_tokens',
    'social.pipeline.disconnect.disconnect'
)

if GLUU_VERSION == 1:
    GLUU_OAUTH2_CLIENT_ID = os.environ.get('GLUU_OAUTH2_CLIENT_ID_V1')
    GLUU_OAUTH2_CLIENT_SECRET = os.environ.get('GLUU_OAUTH2_CLIENT_SECRET_V1')
    SOCIAL_AUTH_GLUU_KEY = os.environ.get('SOCIAL_AUTH_GLUU_KEY_V1')
    SOCIAL_AUTH_GLUU_SECRET = os.environ.get('SOCIAL_AUTH_GLUU_SECRET_V1')

else:
    GLUU_OAUTH2_CLIENT_ID = os.environ.get('GLUU_OAUTH2_CLIENT_ID_V2')
    GLUU_OAUTH2_CLIENT_SECRET = os.environ.get('GLUU_OAUTH2_CLIENT_SECRET_V2')
    SOCIAL_AUTH_GLUU_KEY = os.environ.get('SOCIAL_AUTH_GLUU_KEY_V2')
    SOCIAL_AUTH_GLUU_SECRET = os.environ.get('SOCIAL_AUTH_GLUU_SECRET_V2')

SOCIAL_AUTH_END_SESSION_ENDPOINT = 'https://idp.gluu.org/oxauth/seam/resource/restv1/oxauth/end_session'
SOCIAL_AUTH_POST_LOGOUT_REDIRECT_URL = os.environ.get('SOCIAL_AUTH_POST_LOGOUT_REDIRECT_URL')

if bool(int(os.environ.get('SELF_SIGNED_CERT', '1'))):
    VERIFY_SSL = os.environ.get('SELF_SIGNED_CERT_PATH')
else:
    VERIFY_SSL = True

VERIFY_SSL = False
# SCIM and UMA
SCIM_TEST_MODE =  bool(int(os.environ.get('SCIM_TEST_MODE', '1')))

if SCIM_TEST_MODE:
    SCIM_TEST_MODE_ACCESS_TOKEN = os.environ.get('SCIM_TEST_MODE_ACCESS_TOKEN')

else:
    UMA_CLIENT_ID = os.environ.get('UMA_CLIENT_ID')
    UMA_CLIENT_SECRET = os.environ.get('UMA_CLIENT_SECRET')
# sms
SENDSMS_BACKEND = 'sendsms.backends.console.SmsBackend'

# twitter settings
TWITTER_USER = 'GluuFederation'
TWITTER_TIMEOUT = 3600
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# news
PRESS_RELEASES_URL = 'http://www.gluu.org/resources/press-releases/'
PRESS_RELEASES_TIMEOUT = 86400

TICKETS_PER_PAGE = 15
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 15
SEARCH_RESULTS_PER_PAGE = 15

HAYSTACK_CUSTOM_HIGHLIGHTER = 'search.highlight.GluuHighlighter'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'res', 'templates', 'whoosh_index'),
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(funcName)s line: %(lineno)d] - %(message)s'
        },
        'info': {
            'format': '[%(levelname)s] [%(asctime)s] - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'verbose'
        },
        'crm_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/crm.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'verbose'
        },
        'email_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/emails.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'info'
        },
        'idp_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/idp.log'),
            'maxBytes': '16777216',  # 16Mb
            'formatter': 'info'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['log_file', 'mail_admins', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'crm': {
            'handlers': ['crm_log'],
            'level': 'INFO'
        },
        'emails': {
            'handlers': ['email_log'],
            'level': 'INFO'
        },
        'idp': {
            'handlers': ['idp_log'],
            'level': 'INFO'
        },
    },
}

# mail settings
LIVE_EMAIL = bool(int(os.environ.get('LIVE_EMAIL', '1')))
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'

if LIVE_EMAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email Addresses
RECIPIENT_TEST_EMAIL = os.environ.get('RECIPIENT_TEST_EMAIL')
TEST_TEXT_EMAIL = bool(int(os.environ.get('TEST_TEXT_EMAIL', '1')))

DEFAULT_FROM_EMAIL = 'support@example.com>'

SUPPORT_EMAIL = 'support@example.com'
USER_MANAGEMENT_EMAIL = 'user@example.com'
DEFAULT_RECIPIENT_IDLE_TICKET_REMINDERS = os.environ.get('DEFAULT_RECIPIENT_IDLE_TICKET_REMINDERS', None)
RECIPIENT_NEW_NOTIFICATIONS = 'support@example.com'
BCC = 'user@exapmle.com'

# Sugar CRM Syncing
CRM_SYNCING = bool(int('1'))
CRM_SYNCING = bool(int(os.environ.get('CRM_SYNCING', '1')))
SUGAR_CRM_URL = os.environ.get('SUGAR_CRM_URL')
SUGAR_CRM_USERNAME = os.environ.get('SUGAR_CRM_USERNAME')
SUGAR_CRM_PASSWORD = os.environ.get('SUGAR_CRM_PASSWORD')

# Social Auth
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'
LOGIN_URL = '/login/gluu/'

EMAIL_FILE_PATH = '/tmp/email-messages/'
EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS', '1')))
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER =  os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =  os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))

# Cache
CACHE_TIMEOUT = 14400 # 4 hours in seconds
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "{0}/{1}".format(os.environ['REDISCLOUD_CACHE'], 0),
    }
}

BROKER_URL = os.environ['REDISCLOUD_URL']

# Django Compressor
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_OUTPUT_DIR = 'cdn'
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL

#Mailgun Credentials
MAILGUN_DOMAIN="Your mailgun domain will go here"
MAILGUN_KEY="Your mailgun key will go here"

# Email for daily open tickets notifications
EMAIL_OF_REPORTING_PERSON = "Email of reoprting person"

# Endpoints required for Gluu Idp
SCIM_CREATE_USER_CONSTANT = 'https://<your-domain>/identity/seam/resource/restv1/scim/v2/Users/'
SCIM_UPDATE_USER_CONSTANT = 'https://<your-domain>/identity/seam/resource/restv1/scim/v2/Users/{}/'

#Endpoints required for UMA
UMA_ACCESS_TOKEN_ENDPOINT='https://<your-domain>/oxauth/seam/resource/restv1/oxauth/token'
UMA_AUTHORIZE_RPT='https://<your-domain>/oxauth/seam/resource/restv1/requester/perm'
UMA_OBTAIN_RPT='https://<your-domain>/oxauth/seam/resource/restv1/requester/rpt'


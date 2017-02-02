# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0t1z6qr^r_dud+7zn3b4t!t9n+sw#xugv=ec+m$x^=pd0$kxft'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'user',
    'employee',
    'goods',
    'partner',
    'order',
    'file',
    'mall',
    'directsales',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'novice.urls'


REST_FRAMEWORK = {
    '''
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    '''
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

#mall config
MALL = {
    'ORDER_STATUS' : (
        
    ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                #directsales模块的上下文渲染器
                'directsales.context_processor.get_bonus',
            ],
        },
    },
]

WSGI_APPLICATION = 'novice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'novice',
        'USER':'ym',
        'PASSWORD':'panyuli1314520',
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")

#public static file ,example:jquery.js
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')



LOGGING = {  
    'disable_existing_loggers': False,  
    'version': 1,  
    'handlers': {  
        'console': {  
            # logging handler that outputs log messages to terminal  
            'class': 'logging.StreamHandler',  
            'level': 'DEBUG', # message level to be written to console  
        },  
    },  
    'loggers': {  
        '': {  
            # this sets root level logger to log debug and higher level  
            # logs to console. All other loggers inherit settings from  
            # root level logger.  
            'handlers': ['console'],  
            'level': 'DEBUG',  
            'propagate': False, # this tells logger to send logging message  
                                # to its parent (will send if set to True)  
        },  
        'django.db': {  
            # django also has database level logging  
        },  
    },  
}

#email
SEND_BROKEN_LINK_EMAILS = True
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
# EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'yimeng88@loongkylin.com'
EMAIL_HOST_PASSWORD = 'Lqh1314520'
EMAIL_SUBJECT_PREFIX = '[novice-django]'
DEFAULT_FROM_EMAIL = 'yimeng <yimeng88@loongkylin.com>'
ADMINS = (
    ('yimeng', 'yimeng88@loongkylin.com'),
)
MANAGERS = (
    ('yimeng', 'yimeng88@loongkylin.com'),
)


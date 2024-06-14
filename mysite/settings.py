from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if 'x-route-planning' in str(BASE_DIR):
    pass
else: 
    BASE_DIR = Path(__file__).resolve().parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-96a3#k(or!%2oi+76-=bofcs4)ees9rz@8muc2$f4uz&p+qqpe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'suzdalenkoalexey.pythonanywhere.com', '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
     # 'django.contrib.admin',
     # 'django.contrib.auth',
     # 'django.contrib.contenttypes',
     # 'django.contrib.sessions',
     # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',

  #  'corsheaders',
]

# CORS_ORIGIN_WHITELIST = ( 'http://127.0.0.1:5500', )

MIDDLEWARE = [
    #'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
   # {
   #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
   # },
   # {
   #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
   # },
   # {
   #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
   # },
   # {
   #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
   # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (BASE_DIR/'static',)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_KEY = 'AIzaSyBDKhqes2S-VlNPQmOi70qpJMkaCfhzyt4'
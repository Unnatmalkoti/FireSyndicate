from fire_syndicate.settings.base import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'FireSyndicateProductionDB',
            'USER': 'firesite',
            'PASSWORD': 'EfLWcLT52Hdc5QK',
            'HOST': 'fireproductiondb.cegpsexlbalz.ap-south-1.rds.amazonaws.com',
            'PORT': 5432,
        }
}

DEBUG = False

ALLOWED_HOSTS = ["*"]
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
STATIC_ROOT = os.path.join( BASE_DIR,"static_cdn")
CONN_MAX_AGE = 50
X_FRAME_OPTIONS = "DENY"
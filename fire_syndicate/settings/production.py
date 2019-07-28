from fire_syndicate.settings.base import *
# import django_heroku
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

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

#6aM5dwo3FrLOpJjx
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': "Firesyndicate-db",
#         'HOST' :"mongodb+srv://fire-db-user:<pBBkZw6MuLWLesfi>@firesyndicate-db-zpweo.mongodb.net/test?retryWrites=true&w=majority",
#         'USER' : "fire-db-user",
#         'PASSWORD' : "pBBkZw6MuLWLesfi"
#     }
# }



DEBUG = False

ALLOWED_HOSTS = ["*"]
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
STATIC_ROOT = os.path.join( BASE_DIR,"static_cdn")
CONN_MAX_AGE = 50
X_FRAME_OPTIONS = "DENY"
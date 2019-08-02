from fire_syndicate.settings.base import *




try:
    from fire_syndicate.settings.local import *
except:
    pass

DEBUG = True

ALLOWED_HOSTS = ["firesyndicate.tk","localhost"]
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
STATIC_ROOT = os.path.join( BASE_DIR,"static_cdn")
CONN_MAX_AGE = 50
X_FRAME_OPTIONS = "DENY"
from fire_syndicate.settings.base import *

#Overide Base settings here

SECRET_KEY = 'txw!_rv4wd3ftzbi^kv8k86%)9$itfgdfgdfgdfgsdfgse00%=0(1p9p42xo9wv(b5'

DEBUG=True

try:
    from fire_syndicate.settings.local import *
except:
    pass
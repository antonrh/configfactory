import pathlib

import environ
from django.utils.translation import gettext_lazy as _

###############
# DIRECTORIES #
###############
BASE_DIR = pathlib.Path(__file__).resolve(strict=True).parent.parent
ROOT_DIR = BASE_DIR.parent

###############
# ENVIRONMENT #
###############
env = environ.Env()
env.read_env(".env")

#########
# DEBUG #
#########
DEBUG = env.bool("APP_DEBUG", default=False)

############
# SECURITY #
############
SECRET_KEY = env.str("SECRET_KEY", default="secret")

#######
# URL #
#######
ROOT_URLCONF = "configfactory.conf.urls"

############
# DATABASE #
############

###############
# I18N / L10N #
###############
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = "en-us"
LANGUAGES = (("en", _("English")),)

########
# APPS #
########
INSTALLED_APPS = ("configfactory",)

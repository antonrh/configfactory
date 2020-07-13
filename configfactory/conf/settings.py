import pathlib

import environ
from django.utils.translation import gettext_lazy as _

#########
# PATHS #
#########
BASE_DIR = pathlib.Path(__file__).resolve(strict=True).parent.parent
ROOT_DIR = BASE_DIR.parent
ENV_FILE = ROOT_DIR.joinpath(".env")

###############
# ENVIRONMENT #
###############
env = environ.Env()

if ENV_FILE.exists():
    env.read_env(str(ENV_FILE))

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
ROOT_URLCONF = "configfactory.urls"

############
# DATABASE #
############
DATABASES = {"default": env.db("DATABASE_URL", default="sqlite://")}

###############
# I18N / L10N #
###############
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = "en-us"
LANGUAGES = (("en", _("English")),)

################
# STATIC FILES #
################
STATIC_URL = "/static/"

########
# APPS #
########
INSTALLED_APPS = (
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "configfactory",
)

########
# REST #
########
REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

from django.utils.translation import gettext_lazy as _

from configfactory.conf import dirs

############
# SECURITY #
############

SECRET_KEY = "test"

###############
# I18N / L10N #
###############

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = "en"
LANGUAGES = [("en", _("English"))]

LOCALE_PATHS = [dirs.BASE_DIR / "conf" / "locale"]

################
# APPLICATIONS #
################
INSTALLED_APPS = ["configfactory"]

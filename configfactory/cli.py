import os
import sys

from django.core import management

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configfactory.conf.settings")


def main():
    argv = sys.argv[:1] + ["configfactory"] + sys.argv[1:]
    management.execute_from_command_line(argv)


if __name__ == "__main__":
    main()

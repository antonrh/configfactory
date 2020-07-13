from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "ConfigFactory CLI"

    def handle(self, *args, **options):
        self.stdout.write("Hello, ConfigFactory !")

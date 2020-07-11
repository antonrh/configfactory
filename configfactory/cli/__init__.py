import click

from configfactory.cli import commands
from configfactory.main import get_application


def main() -> None:
    cli = click.Group(context_settings={"obj": get_application()})
    cli.add_command(commands.create_superuser)
    cli.main()

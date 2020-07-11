import click
from fastapi import FastAPI
from pydantic import EmailStr, validate_email
from pydantic.errors import EmailError

from configfactory.cli.decorators import app_command
from configfactory.db import get_database
from configfactory.exceptions import UserCreateError
from configfactory.repositories import UserRepository
from configfactory.services.user import UserService


@click.command("create-superuser")
@app_command()
async def create_superuser(app: FastAPI):
    database = get_database(app)
    user_repository = UserRepository(database=database)
    user_service = UserService(user_repository=user_repository)

    while True:
        try:
            email = click.prompt("Please, enter valid email")
            validate_email(email)
        except EmailError:
            click.echo("Invalid email.")
            continue

        password = click.prompt(
            "Please, enter password", hide_input=True, confirmation_prompt=True
        )
        try:
            user = await user_service.create_superuser(
                email=EmailStr(email), password=password
            )
            click.echo(f"User {user.email} successfully created.")
        except UserCreateError as exc:
            click.echo(f"Failed to create super user: {exc}")
            continue
        break

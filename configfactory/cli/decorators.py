import asyncio
import functools
from collections import Callable

import click
from fastapi import FastAPI


def app_command(asynchronous: bool = True, lifespan: bool = True) -> Callable:
    def wrapper(func):
        assert asyncio.iscoroutinefunction(
            func
        ), "Command function must be a coroutine."

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            app: FastAPI = click.get_current_context().obj

            async def run():
                if lifespan:
                    await app.router.startup()
                    try:
                        await func(app, *args, **kwargs)
                    finally:
                        await app.router.shutdown()
                else:
                    await func(app, *args, **kwargs)

            if asynchronous:
                return asyncio.run(run())
            return func(app, *args, **kwargs)

        return wrapped

    return wrapper

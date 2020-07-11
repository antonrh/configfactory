from fastapi import Depends
from starlette.requests import Request


def DependsState(name: str, *, use_cache: bool = True):
    def _dependency(request: Request):
        return getattr(request.app.state, name)

    return Depends(_dependency, use_cache=use_cache)

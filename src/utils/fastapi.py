from fastapi import FastAPI
from fastapi.routing import APIRoute
from .models import to_camelCase


def simplify_op_id(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = to_camelCase(route.name)

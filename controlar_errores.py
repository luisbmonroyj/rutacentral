from flask import abort, make_response
from functools import wraps


def control_errores():
    """Respuesta HTTP 500, para errores en cada blueprint"""
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                abort(make_response(str(e), 500))
        return wrapper
    return decorate

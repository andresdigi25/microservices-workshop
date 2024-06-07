import os
import sys
import logging
import traceback
import warnings
from functools import wraps
import json_logging
from datetime import date

log_level = os.getenv('LOG_LEVEL', 'INFO')

logger = logging.getLogger(os.getenv('LOGGER_NAME', 'demo-logger'))
logger.propagate = False

if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)

logger.setLevel(level=log_level)
logger.addHandler(logging.StreamHandler(sys.stdout))

json_logging.init_non_web(enable_json=True)


def process_output(input):
    for i, (key, value) in enumerate(input.items(), start=1):
        value['id'] = i
        value['date'] = str(date.today())
    return input

def set_level(level):
    logger.setLevel(level=level)


def init_flask_web_logger(app):
    from flask import request
    json_logging.init_flask(enable_json=True)
    json_logging.init_request_instrument(app, exclude_url_patterns=[r'/*'])

    @app.before_request
    def log_before_request():
        try:
            logger.info({
                'method': request.method,
                'url': request.url,
                'headers': dict(request.headers.items()),
                'data': request.data,
                'form': request.form.to_dict(),
                'files': request.files.to_dict()
            })
        except Exception as ex:
            logger.error(str(ex))

    @app.after_request
    def log_after_request(response):
        try:
            logger.info({
                'status_code': response.status_code,
                'headers': dict(response.headers.items()),
                'data': response.data
            })
        except Exception as ex:
            logger.error(str(ex))

        return response


def log(*args, **kwargs):
    func = None

    if len(args) == 1:
        func = args[0]

    fn_call = kwargs.get('fn_call', True)
    raise_ex = kwargs.get('raise_ex', True)

    def call(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):

            warnings.warn(
                "@log is deprecated, use only logger instead",
                DeprecationWarning
            )

            props = {'args': str(args), 'kwargs': str(kwargs)}

            if fn_call:
                logger.debug(f'fn: {fn.__name__}', extra={'props': props})

            try:
                return fn(*args, **kwargs)
            except Exception as ex:
                logger.error(traceback.format_exc(), extra={'props': props})

                if raise_ex:
                    raise ex

        return wrapped

    return call(func) if func else call


try:
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.datastructures import Headers, MutableHeaders
    from starlette.types import Message


    class LoggingMiddleware(BaseHTTPMiddleware):

        def __init__(self, app):
            super().__init__(app)

        async def set_body(self, request: Request):
            receive_ = await request._receive()

            async def receive() -> Message:
                return receive_

            request._receive = receive

        async def dispatch(self, request, call_next):
            await self.set_body(request)
            body = await request.body()

            logger.info(
                {
                    'method': request.method,
                    'url': str(request.url),
                    'headers': dict(request.headers),
                    'data': body
                }
            )

            response = await call_next(request)

            data = b''

            try:
                async for chunk in response.body_iterator:
                    data += chunk

                logger.info(
                    {
                        'status_code': response.status_code,
                        'headers': dict(response.headers),
                        'data': data
                    }
                )
            except Exception as ex:
                logger.error(str(ex))

            return Response(
                content=data,
                status_code=response.status_code,
                headers=MutableHeaders(raw=response.raw_headers),
                media_type=response.media_type
            )
except ModuleNotFoundError as ex:
    pass

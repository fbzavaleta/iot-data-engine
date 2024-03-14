from collections import namedtuple
from .core.routes import (
    bp as core_bp,
    bp_v1 as core_bp_v1,
)


RouteConfig = namedtuple('RouteConfig', 'blueprint options')
APP_ROUTES = (
    RouteConfig(core_bp,    {}),
    RouteConfig(core_bp_v1, {'url_prefix': '/feed'}),
)


def load_routes(app, routes=APP_ROUTES):
    for route in routes:
        app.register_blueprint(route.blueprint, **route.options)
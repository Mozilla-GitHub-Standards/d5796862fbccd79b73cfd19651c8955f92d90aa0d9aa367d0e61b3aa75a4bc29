
from mozsvc.config import get_configurator


def includeme(config):
    config.include("pyramid_multiauth")
    config.include("cornice")
    config.include("mozsvc")
    config.scan("keyretrieval.views")


def main(global_config, **settings):
    config = get_configurator(global_config, **settings)
    config.include(includeme)
    return config.make_wsgi_app()

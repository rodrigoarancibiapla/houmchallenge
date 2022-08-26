""" Configuration for the application """
from django.apps import AppConfig


class GeohoumConfig(AppConfig):
    """ Options for geohoum application """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geohoum'

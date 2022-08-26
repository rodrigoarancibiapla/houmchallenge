""" Client class to manage geographics calculations """

from geohoum.adapters.geo.igeo import IGEO


class GEOClient:
    """ Client class for geo lib """

    def __init__(self, geoapi: IGEO):
        """ Initialize geo client """
        self.geoapi = geoapi

    def calculate_distance(self, latitude1, longitude1, latitude2, longitude2):
        """ Calculate distance between two points """
        return self.geoapi.calculate_distance(
            latitude1, longitude1, latitude2, longitude2)

""" Class to manage geographics calculations, use geopy library """

from abc import abstractmethod

import geopy.distance

class GEOPYLIB:
    """ Client class for geo lib """
    @abstractmethod
    def calculate_distance(latitude1, longitude1, latitude2, longitude2):
        """ Calculate distance between two points"""
        return geopy.distance.geodesic(
            (latitude1, longitude1), (latitude2, longitude2)).km

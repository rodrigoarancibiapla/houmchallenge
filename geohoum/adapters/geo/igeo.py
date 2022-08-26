""" Abstract to manage geographics calculations """

from abc import ABC, abstractmethod

class IGEO(ABC):
    """ Abstract class for geo lib """

    @abstractmethod
    def calculate_distance(latitude1, longitude1,
                           latitude2, longitude2):
        """ Calculate distance between two points"""
        raise NotImplementedError

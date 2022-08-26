""" Unit test case """
import unittest

from geohoum.adapters.geo.geo_client import GEOClient
from geohoum.adapters.geo.geopylib import GEOPYLIB


class GeoLibTestCase(unittest.TestCase):
    """
    Ensure we can do geographical calculations
    """
    def test_distances(self):
        """ Ensure we can calculate distancie """
        geo_client = GEOClient(GEOPYLIB)
        distance = geo_client.calculate_distance(-77, -30, -78, -31)
        self.assertEqual(int(distance), 114)

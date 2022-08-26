""" Integration test case """
import unittest
from datetime import datetime, timedelta

from geohoum.models.position_model import Position
from geohoum.entities.positions import Positions

# Create your tests here.


class PositionsTestCase(unittest.TestCase):
    """ Bussiness logic test case"""
    def setUp(self):
        """ Create array of positions """
        pos_1 = Position(1, 10, 1, datetime.now(), datetime.now() +
                         timedelta(hours=1), -77, 30)
        pos_2 = Position(2, 10, 2, datetime.now() +
                         timedelta(hours=2), datetime.now() +
                         timedelta(hours=3), -
                         77, 34)  # 100.4 Km
        pos_3 = Position(3, 10, 3, datetime.now() +
                         timedelta(hours=4), datetime.now() +
                         timedelta(hours=6), -
                         77, 36)  # 50.2 Km
        pos_4 = Position(4, 10, 4, datetime.now() +
                         timedelta(hours=7), datetime.now() +
                         timedelta(hours=10), -
                         77, 39)  # 75.3 Km
        self.positions = [pos_1, pos_2, pos_3, pos_4]

    def test_position_filter_speed(self):
        """ Ensure we can filter positions and create trips """
        movs = Positions.filter_by_speed(self.positions, 80)
        self.assertEqual(len(movs), 1)
        self.assertEqual(movs[0].id_houmer, 10)
        self.assertEqual(movs[0].id_property_start, 1)
        self.assertEqual(movs[0].id_property_end, 2)
        self.assertEqual(movs[0].speed, 100)

        trips = Positions.filter_by_speed(self.positions, 30)
        self.assertEqual(len(trips), 3)
        trips = Positions.filter_by_speed(self.positions, 70)
        self.assertEqual(len(trips), 2)

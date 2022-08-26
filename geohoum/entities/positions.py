""" Module that contains business logic """
from geohoum.adapters.geo.geo_client import GEOClient
from geohoum.adapters.geo.geopylib import GEOPYLIB
from geohoum.models.trip_model import Trip

class Positions:
    """
    Business class used for manage positions
    """

    @staticmethod
    def filter_by_speed(positions, speed_limit):
        """ Create array of trips where speed was exceeded """
        trips = []
        geo_client = GEOClient(GEOPYLIB)
        for id_position in range(1, len(positions)):
            last_position = positions[id_position-1]
            actual_position = positions[id_position]
            distance = geo_client.calculate_distance(
                last_position.latitude,
                last_position.longitude,
                actual_position.latitude,
                actual_position.longitude)
            time = (actual_position.start_date -
                    last_position.end_date).seconds/3600
            speed = int(distance/time)
            if speed > speed_limit:
                trip = Trip(id_houmer=actual_position.id_houmer,
                            id_property_start=last_position.id_property,
                            id_property_end=actual_position.id_property,
                            start_travel_date=last_position.end_date,
                            end_travel_date=actual_position.start_date,
                            speed=speed)
                trips.append(trip)

        return trips

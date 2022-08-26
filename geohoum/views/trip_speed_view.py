"""
This class create the view that manage the GET action that
retrieve trips where the houmer passed the speed limit
"""
from rest_framework import generics

from geohoum.models.position_model import Position
from geohoum.entities.positions import Positions
from geohoum.serializers.trip_serializer import TripSerializer


class TripSpeedView(
    generics.ListAPIView
):
    """
    Retrieve a list of trips where the speed limit was exceeded
    """
    serializer_class = TripSerializer

    def get_queryset(self):
        """ Obtain trips that exceed speed limit """
        idhoumer = self.kwargs['idhoumer']
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        speed_limit = self.kwargs['speed']

        position_list = list(
            Position.objects.filter(
                id_houmer=idhoumer,
                start_date__year=year,
                start_date__month=month,
                start_date__day=day))
        movs = Positions.filter_by_speed(position_list, speed_limit)
        return movs

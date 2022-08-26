"""
This class create the view that manage the GET action that retrieve visited positions
"""

from rest_framework import generics

from geohoum.models.position_model import Position
from geohoum.serializers.property_visited_serializer import PropertyVisitedSerializer


class PropertiesVisitedView(
    generics.ListAPIView
):
    """
    Retrieve list of properties visited for a houmer and a date.
    """
    serializer_class = PropertyVisitedSerializer

    def get_queryset(self):
        """ Obtain positions filtered by ih houmer and date"""
        idhoumer = self.kwargs['idhoumer']
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']

        return list(
            Position.objects.filter(
                id_houmer=idhoumer,
                start_date__year=year,
                start_date__month=month,
                start_date__day=day))

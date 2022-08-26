"""
This class create the view that manage the POST action to create a new position
"""

from rest_framework import mixins
from rest_framework import generics

from geohoum.models.position_model import Position
from geohoum.serializers.position_serializer import PositionSerializer


class PositionCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    """
    Create a position in the system.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def post(self, request, *args, **kwargs):
        """ Call the method to create a position """
        return self.create(request, *args, **kwargs)

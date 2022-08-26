""" Serializer from a model to python data types """

from rest_framework import serializers
from geohoum.models.position_model import Position


class PropertyVisitedSerializer(serializers.ModelSerializer):
    """
    Class used to convert Property model to python data types
    """
    class Meta:
        """ Model and fields to serialize"""
        model = Position
        fields = ['id_houmer', 'id_property']

    def to_representation(self, instance):
        """ Add time between positions to result"""
        data = super().to_representation(instance)
        data["time"] = int(
            ((instance.end_date - instance.start_date).seconds) / 60)
        return data

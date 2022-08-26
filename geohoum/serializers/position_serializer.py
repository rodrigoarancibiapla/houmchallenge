""" Serializer from a model to python data types """
from rest_framework import serializers
from geohoum.models.position_model import Position


class PositionSerializer(serializers.ModelSerializer):
    """
    Class used to convert Position model to python data types
    """
    class Meta:
        """ Model and fields to serialize"""
        model = Position
        fields = '__all__'

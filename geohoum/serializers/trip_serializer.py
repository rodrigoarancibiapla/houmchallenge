""" Serializer from a model to python data types """

from rest_framework import serializers
from geohoum.models.trip_model import Trip

class TripSerializer(serializers.ModelSerializer):
    """
    Class used to convert Trip model to python data types
    """
    class Meta:
        """ Model and fields to serialize"""
        model = Trip
        exclude = ['id']


from django.db import models


class Trip(models.Model):
    """ Class that defines the trip of a
    houmer from a property to another
    """

    id_houmer = models.IntegerField(help_text="Houmer Id")
    id_property_start = models.IntegerField(
        help_text="Property Id trip start",)
    id_property_end = models.IntegerField(help_text="Property Id trip end",)
    start_travel_date = models.DateTimeField(help_text="Date time trip start",)
    end_travel_date = models.DateTimeField(help_text="Date time trip end",)
    speed = models.IntegerField(help_text="Speed in km/h",)

    class Meta:
        """
        Options of the model.
        Class will not be save to DB
        """
        managed = False

    # def __str__(self):
    #     """ String represnetation of the model"""
    #     return str(self.id_property_start) + " to " + \
    #         str(self.id_property_end) + " at " + str(self.speed)

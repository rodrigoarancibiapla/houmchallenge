
from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.core.validators import MaxValueValidator, MinValueValidator


class Position(models.Model):
    """ Class that defines the position of a
    houmer in a property y a moment
    """

    id_houmer = models.IntegerField(help_text="Houmer Id", validators=[
        MinValueValidator(1),
        MaxValueValidator(10000),
    ])
    id_property = models.IntegerField(help_text="Property Id", validators=[
        MinValueValidator(1),
        MaxValueValidator(1000000),
    ])
    start_date = models.DateTimeField(help_text="Visit start date and time")
    end_date = models.DateTimeField(help_text="End date and time of visit")
    latitude = models.FloatField(help_text="Latitude in grades", validators=[
        MinValueValidator(-90),
        MaxValueValidator(90),
    ])
    longitude = models.FloatField(help_text="Longitude in grades", validators=[
        MinValueValidator(-180),
        MaxValueValidator(180)
    ])

    class Meta:
        """ 
        Options of the model.
        """
        ordering = ['start_date']
        constraints = [
            CheckConstraint(
                check=Q(end_date__gt=F('start_date')),
                name='check_start_date',
            ),
        ]
        indexes = [
            models.Index(fields=['id_houmer', 'start_date', ])
        ]

    # def __str__(self):
    #     """ String represnetation of the model"""
    #     return str(self.id_houmer) + " in " + str(self.latitude) + "," + str(self.longitude)

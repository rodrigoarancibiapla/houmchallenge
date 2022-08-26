from django.urls import path

from geohoum.views.properties_visited_view import PropertiesVisitedView
from geohoum.views.position_create_view import PositionCreateView
from geohoum.views.trip_speed_view import TripSpeedView

urlpatterns = [
    path('geohoum/visits/<int:idhoumer>/<int:year>/<int:month>/<int:day>',
         PropertiesVisitedView.as_view(), name='position-list'),
    path('geohoum/speed/<int:speed>/<int:idhoumer>/<int:year>/<int:month>/<int:day>',
         TripSpeedView.as_view(), name='speed-list'),
    path('geohoum/', PositionCreateView.as_view(), name='position-create'),
]

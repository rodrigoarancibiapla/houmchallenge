""" End to end test case """
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.test import APITestCase

from geohoum.models.position_model import Position


class ApiTests(APITestCase):
    """ Api test case"""
    def test_create_position(self):
        """
        Ensure we can create a position.
        """
        datetime_now = datetime.now()
        datetime_now_plus_1 = datetime.now() + timedelta(hours=1)
        data = {
            "id_houmer": 10,
            "id_property": 202,
            "start_date": datetime_now,
            "end_date": datetime_now_plus_1,
            "latitude": -77.35566,
            "longitude": -33.785
        }
        response = self.client.post('/geohoum/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Position.objects.count(), 1)
        self.assertEqual(Position.objects.get().id_houmer, 10)
        self.assertEqual(Position.objects.get().id_property, 202)
        self.assertEqual(Position.objects.get().start_date.strftime(
            '%Y-%m-%dT%H:%M:%S'), datetime_now.strftime('%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(
            Position.objects.get().end_date.strftime('%Y-%m-%dT%H:%M:%S'),
            datetime_now_plus_1.strftime('%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(Position.objects.get().latitude, -77.35566)
        self.assertEqual(Position.objects.get().longitude, -33.785)

    def test_get_position(self):
        """
        Ensure we can get a position
        """
        start_date = '27/10/22 15:25:20'
        end_date = '27/10/22 17:25:20'

        start_date_obj = datetime.strptime(start_date, '%d/%m/%y %H:%M:%S')
        end_date_obj = datetime.strptime(end_date, '%d/%m/%y %H:%M:%S')
        data = {
            "id_houmer": 10,
            "id_property": 202,
            "start_date": start_date_obj,
            "end_date": end_date_obj,
            "latitude": -77.35566,
            "longitude": -33.785
        }
        response = self.client.post('/geohoum/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/geohoum/visits/10/2022/10/27')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(list(response.data)[0]['time'], 120)

    def test_speed(self):
        """
        Ensure we can detect toretos houmers.
        """
        start_date = '27/10/22 15:23:20'
        end_date = '27/10/22 16:24:20'

        start_date_obj = datetime.strptime(start_date, '%d/%m/%y %H:%M:%S')
        end_date_obj = datetime.strptime(end_date, '%d/%m/%y %H:%M:%S')
        data = {
            "id_houmer": 10,
            "id_property": 202,
            "start_date": start_date_obj,
            "end_date": end_date_obj,
            "latitude": -77.35566,
            "longitude": -33.785
        }
        response = self.client.post('/geohoum/', data, format='json')
        start_date = '27/10/22 17:23:20'
        end_date = '27/10/22 18:24:20'

        start_date_obj = datetime.strptime(start_date, '%d/%m/%y %H:%M:%S')
        end_date_obj = datetime.strptime(end_date, '%d/%m/%y %H:%M:%S')
        data = {
            "id_houmer": 10,
            "id_property": 202,
            "start_date": start_date_obj,
            "end_date": end_date_obj,
            "latitude": -77.35566,
            "longitude": -39.785
        }
        response = self.client.post('/geohoum/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/geohoum/speed/25/10/2022/10/27')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        response = self.client.get('/geohoum/speed/300/10/2022/10/27')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

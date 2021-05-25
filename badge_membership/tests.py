from django.http import response
from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase,APIClient
from badge_membership.models import BadgeName,PromoCode,Toko,Profile


class URLTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_url_list_produk(self):
        url = '/apibadge/list_produk'
        response = self.client.get(url, follow=True)
        # response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_url_list_produk(self):
        url = '/apibadge/profile'
        response = self.client.get(url, follow=True)
        # response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    

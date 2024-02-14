from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json

class APITestCase(TestCase):
    accessToken= ""
    
    def setUp(self):
        self.client = Client()

    def test_token(self):
        
        userData = {"username": "test@gmail.com","password":"test123"}
        response = self.client.post('https://kaizentree.onrender.com/api/token/',
        data=json.dumps(userData), content_type='application/json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        accessToken = response.json()['access']
        
    def test_get_items(self):
        # Send GET request to the API endpoint
        response = self.client.get('https://kaizentree.onrender.com/api/item/')


        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains expected items
        expected_items = [
            {"sku": "NY-STOCK", "name": "NY BEESWAX BUNDLE",
            "category": [5],"tags":[1],"in_stock": 2000,
    "available_stock": 2000}
        ]
        self.assertEqual(response.json(), expected_items)

    def test_create_item(self):
        # Create a new item
        new_item_data = {"sku": "NY-STOCK-TEST", "name": "NY-TEST BEESWAX BUNDLE",
            "category": [5],"tags":[1],"in_stock": 2050,
    "available_stock": 2050}
        
        response = self.client.post('https://kaizentree.onrender.com/api/item/', data=json.dumps(new_item_data), content_type='application/json')

        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the new item is created in the database
        self.assertTrue(Item.objects.filter(sku="XYZ789").exists())

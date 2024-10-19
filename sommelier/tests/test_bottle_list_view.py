from django.test import TestCase
from django.urls import reverse_lazy

from sommelier import models
from sommelier.tests import create_wine, create_bottle


class TestBottleListView(TestCase):
    endpoint = reverse_lazy('bottle-list')

    def test_get(self):
        wine = create_wine()
        expected_count = 3
        for _ in range(expected_count):
            create_bottle(wine)
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)
        bottles = response.context['bottles']
        self.assertEqual(len(bottles), expected_count, bottles)

    def test_get_with_taste(self):
        wine = create_wine(taste=models.Taste.DRY)
        other_wine = create_wine(taste=models.Taste.SEMI_DRY)
        expected_count = 1
        response = self.client.get(self.endpoint, {'taste': wine.taste})
        self.assertEqual(response.status_code, 200)
        bottles = response.context['bottles']
        self.assertEqual(len(bottles), expected_count, bottles)

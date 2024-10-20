import datetime as dt
from typing import Any, Literal

from django.db.models import Model
from django.test import TestCase
from django.urls import reverse_lazy

from sommelier import models
from sommelier.tests import (
    create_bottle,
    create_purchase_info,
    create_wine,
    update_bottle,
    update_purchase_info,
    update_wine,
)

GET_QUERY_PARAM_NAME = Literal[
    'taste',
    'kind',
    'countries',
    'type',
    'name',
    'producer',
    'year_from',
    'year_to',
    'score_from',
    'score_to',
    'keywords',
    'shops',
    'price_from',
    'price_to',
    'date_from',
    'date_to',
]


class TestBottleListView(TestCase):
    endpoint = reverse_lazy('bottle-list')

    def setUp(self):
        self.wine = create_wine()
        self.bottle = create_bottle(self.wine)
        self.purchase_info = create_purchase_info(self.bottle)

        self.other_wine = create_wine()
        self.other_bottle = create_bottle(self.other_wine)
        self.other_purchase_info = create_purchase_info(self.other_bottle)

    def common_test_get_with_params(
        self,
        param_name: GET_QUERY_PARAM_NAME,
        param_value: Any,
        expected_results: list[Model] | None = None,
    ):
        if expected_results is None:
            expected_results = [self.bottle]
        response = self.client.get(self.endpoint, {param_name: param_value})
        self.assertEqual(response.status_code, 200)
        bottles = response.context['bottles']
        self.assertEqual(len(bottles), len(expected_results), bottles)
        for expected_result in expected_results:
            self.assertIn(expected_result, bottles)

    def test_get(self):
        expected_count = 2
        for _ in range(expected_count):
            create_bottle(self.wine)
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)
        bottles = response.context['bottles']
        self.assertEqual(len(bottles), expected_count + 2, bottles)  # from setUp

    def test_get_with_taste(self):
        update_wine(self.wine, taste=models.Taste.DRY)
        update_wine(self.other_wine, taste=models.Taste.SEMI_DRY)
        self.common_test_get_with_params('taste', self.wine.taste)

    def test_get_with_kind(self):
        update_wine(self.wine, kind=models.Kind.RED)
        update_wine(self.other_wine, kind=models.Kind.ROSE)
        self.common_test_get_with_params('kind', self.wine.kind)

    def test_get_with_country(self):
        update_wine(self.wine, country=models.Country.AUSTRALIA)
        update_wine(self.other_wine, country=models.Country.CHILE)
        self.common_test_get_with_params('countries', self.wine.country)

    def test_get_with_countries(self):
        update_wine(self.wine, country=models.Country.AUSTRALIA)
        wine = create_wine(country=models.Country.AUSTRIA)
        update_wine(self.other_wine, country=models.Country.CHILE)
        self.common_test_get_with_params('countries', f'{self.wine.country},{wine.country}')

    def test_get_with_type(self):
        update_wine(self.wine, wine_type='expected type')
        update_wine(self.other_wine, wine_type='other type')
        self.common_test_get_with_params('type', self.wine.type)

    def test_get_with_name(self):
        update_wine(self.wine, name='expected name')
        update_wine(self.other_wine, name='other name')
        self.common_test_get_with_params('name', self.wine.name)

    def test_get_with_producer(self):
        update_wine(self.wine, producer='expected producer')
        update_wine(self.other_wine, producer='other producer')
        self.common_test_get_with_params('producer', self.wine.producer)

    def test_get_with_year_from(self):
        update_bottle(self.bottle, year=2020)
        update_bottle(self.other_bottle, year=2019)
        self.common_test_get_with_params('year_from', self.bottle.year)

    def test_get_with_year_to(self):
        update_bottle(self.bottle, year=2020)
        update_bottle(self.other_bottle, year=2021)
        self.common_test_get_with_params('year_to', self.bottle.year)

    def test_get_with_score_from(self):
        update_bottle(self.bottle, score=8.0)
        update_bottle(self.other_bottle, score=7.0)
        self.common_test_get_with_params('score_from', self.bottle.score)

    def test_get_with_score_to(self):
        update_bottle(self.bottle, score=7.0)
        update_bottle(self.other_bottle, score=8.0)
        self.common_test_get_with_params('score_to', self.bottle.score)

    def test_get_with_keyword(self):
        update_bottle(self.bottle, description='keyword1')
        update_bottle(self.other_bottle, description='keyword2')
        self.common_test_get_with_params('keywords', self.bottle.description)

    def test_get_with_keywords(self):
        update_bottle(self.bottle, description='keyword1 keyword2')
        bottle = create_bottle(self.wine)
        update_bottle(bottle, description='keyword1 keyword2 keyword3')
        update_bottle(self.other_bottle, description='keyword1 keyword3')
        self.common_test_get_with_params('keywords', 'keyword1 keyword2', [self.bottle, bottle])

    def test_get_multiple_with_shops(self):
        update_purchase_info(self.purchase_info, shop_name=models.Shop.GROSZEK)
        bottle = create_bottle(self.wine)
        purchase_info = create_purchase_info(bottle, shop_name=models.Shop.LEWIATAN)
        update_purchase_info(self.other_purchase_info, shop_name=models.Shop.BIEDRONKA)
        self.common_test_get_with_params(
            'shops',
            f'{self.purchase_info.shop_name},{purchase_info.shop_name}',
            [self.bottle, bottle]
        )

    def test_get_with_multiple_shops(self):
        update_purchase_info(self.purchase_info, shop_name=models.Shop.GROSZEK)
        purchase_info = create_purchase_info(self.bottle, shop_name=models.Shop.LEWIATAN)
        update_purchase_info(self.other_purchase_info, shop_name=models.Shop.BIEDRONKA)
        self.common_test_get_with_params('shops', f'{self.purchase_info.shop_name},{purchase_info.shop_name}')

    def test_get_with_price_from(self):
        update_purchase_info(self.purchase_info, price=19.99)
        update_purchase_info(self.other_purchase_info, price=19.89)
        self.common_test_get_with_params('price_from', self.purchase_info.price)

    def test_get_with_price_to(self):
        update_purchase_info(self.purchase_info, price=20.00)
        update_purchase_info(self.other_purchase_info, price=21.00)
        self.common_test_get_with_params('price_to', self.purchase_info.price)

    def test_get_with_date_from(self):
        today = dt.date.today()
        yesterday = today - dt.timedelta(days=1)
        update_purchase_info(self.purchase_info, date=today)
        update_purchase_info(self.other_purchase_info, date=yesterday)
        self.common_test_get_with_params('date_from', self.purchase_info.date)

    def test_get_with_date_to(self):
        today = dt.date.today()
        tomorrow = today + dt.timedelta(days=1)
        update_purchase_info(self.purchase_info, date=today)
        update_purchase_info(self.other_purchase_info, date=tomorrow)
        self.common_test_get_with_params('date_to', self.purchase_info.date)

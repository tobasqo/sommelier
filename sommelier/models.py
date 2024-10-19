import os

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class Kind(models.TextChoices):
    RED = 'R', 'Czerwone'
    WHITE = 'B', 'Białe'
    ROSE = 'P', 'Różowe'
    SPARKLING = 'M', 'Musujące'


class Taste(models.TextChoices):
    SWEET = 'S', 'Słodkie'
    SEMI_SWEET = 'PS', 'Półsłodkie'
    SEMI_DRY = 'PW', 'Półwytrawne'
    DRY = 'W', 'Wytrawne'


class Country(models.TextChoices):
    ARGENTINA = 'AR', 'Argentyna'
    AUSTRALIA = 'AU', 'Australia'
    AUSTRIA = 'AT', 'Austria'
    CHILE = 'CL', 'Chile'
    CROATIA = 'HR', 'Chorwacja'
    FRANCE = 'FR', 'Francja'
    GEORGIA = 'GE', 'Gruzja'
    SPAIN = 'ES', 'Hiszpania'
    CANADA = 'CA', 'Kanada'
    MOLDOVA = 'MD', 'Mołdawia'
    GERMANY = 'DE', 'Niemcy'
    NEW_ZEALAND = 'NZ', 'Nowa Zelandia'
    POLAND = 'PL', 'Polska'
    PORTUGAL = 'PT', 'Portugalia'
    SOUTH_AFRICA = 'ZA', 'RPA'
    ROMANIA = 'RO', 'Rumunia'
    SLOVENIA = 'SI', 'Słowenia'
    USA = 'US', 'USA'
    HUNGARY = 'HU', 'Węgry'
    ITALY = 'IT', 'Włochy'


class Shop(models.TextChoices):
    ALDI = 'Aldi'
    AUCHAN = 'Auchan'
    BIEDRONKA = 'Biedronka'
    CARREFOUR = 'Carrefour'
    DINO = 'Dino'
    ELECLERC = 'E.Leclerc'
    GROSZEK = 'Groszek'
    INTERMARCHE = 'Intermarche'
    KAUFLAND = 'Kaufland'
    LIDL = 'Lidl'
    SPOLEM = 'Społem'
    STOKROTKA = 'Stokrotka'
    ZABKA = 'Żabka'
    OTHER = 'Inny'


class Wine(models.Model):
    taste = models.CharField(max_length=2, choices=Taste.choices)
    kind = models.CharField(max_length=1, choices=Kind.choices)
    country = models.CharField(max_length=2, choices=Country.choices)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)

    def __str__(self):
        return f'[{self.producer}] {self.name} ({self.get_kind_display()}/{self.get_taste_display()})'


    class Meta:
        ordering = ['-id']
        get_latest_by = ["-id"]


# TODO: add image compression
def upload_to(instance: 'Bottle', filename: str):
    ext = os.path.splitext(filename)[1]
    safe_base = slugify(instance.wine.name)
    return os.path.join('wines', f'{safe_base}{ext}')


class Bottle(models.Model):
    wine = models.ForeignKey(Wine, related_name="bottles", on_delete=models.PROTECT)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    image = models.ImageField(upload_to=upload_to, blank=True)
    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.wine} - {self.year}"


    class Meta:
        ordering = ['-id']
        get_latest_by = ["-id"]


class ShopInfo(models.Model):
    bottle = models.ForeignKey(Bottle, related_name='shop_infos', on_delete=models.PROTECT)
    shop_name = models.CharField(max_length=20, choices=Shop.choices)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.shop_name} - {self.price}"


    class Meta:
        ordering = ['-id']
        get_latest_by = ["-id"]

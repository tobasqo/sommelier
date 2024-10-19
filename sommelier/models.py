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
    ALDI = 'Al', 'Aldi'
    AUCHAN = 'Au', 'Auchan'
    BIEDRONKA = 'Bi', 'Biedronka'
    CARREFOUR = 'Ca', 'Carrefour'
    DINO = 'Di', 'Dino'
    ELECLERC = 'El', 'E.Leclerc'
    GROSZEK = 'Gr', 'Groszek'
    INTERMARCHE = 'In', 'Intermarche'
    KAUFLAND = 'Ka', 'Kaufland'
    LIDL = 'Li', 'Lidl'
    SPOLEM = 'Sp', 'Społem'
    STOKROTKA = 'St', 'Stokrotka'
    ZABKA = 'Za', 'Żabka'
    OTHER = 'Ot', 'Inny'


class Wine(models.Model):
    TYPE_MAX_LENGTH = 50
    NAME_MAX_LENGTH = 100
    PRODUCER_MAX_LENGTH = 100

    taste = models.CharField(max_length=2, choices=Taste.choices)
    kind = models.CharField(max_length=1, choices=Kind.choices)
    country = models.CharField(max_length=2, choices=Country.choices)
    type = models.CharField(max_length=TYPE_MAX_LENGTH)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    producer = models.CharField(max_length=PRODUCER_MAX_LENGTH)

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
    YEAR_MIN = 1900
    YEAR_MAX = 2100
    SCORE_MIN = 0
    SCORE_MAX = 10

    wine = models.ForeignKey(Wine, related_name="bottles", on_delete=models.PROTECT)
    year = models.IntegerField(validators=[MinValueValidator(YEAR_MIN), MaxValueValidator(YEAR_MAX)])
    image = models.ImageField(upload_to=upload_to, blank=True)
    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(SCORE_MIN), MaxValueValidator(SCORE_MAX)],
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.wine} - {self.year}"


    class Meta:
        ordering = ['-id']
        get_latest_by = ["-id"]


class ShopInfo(models.Model):
    PRICE_MIN = 0.0

    bottle = models.ForeignKey(Bottle, related_name='shop_infos', on_delete=models.PROTECT)
    shop_name = models.CharField(max_length=20, choices=Shop.choices)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(PRICE_MIN)])
    date = models.DateField()

    def __str__(self):
        return f"{self.shop_name} - {self.price}"


    class Meta:
        ordering = ['-id']
        get_latest_by = ["-id"]

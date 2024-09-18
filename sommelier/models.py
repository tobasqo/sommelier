from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


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
        return f'[{self.producer}] {self.name} ({self.kind}/{self.taste})'


def save_to(instance: 'Bottle', filename: str):
    ext = filename.rsplit('.', 1)[1]
    return f"{instance.wine.name}_{instance.shop_info.date}.{ext}"


class Bottle(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.PROTECT)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    image = models.ImageField(upload_to=save_to, blank=True)
    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.wine} - {self.year}"


class ShopInfo(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete=models.PROTECT, related_name='shop_info')
    shop_name = models.CharField(max_length=20, choices=Shop.choices)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.shop_name} - {self.price}"

import datetime as dt

from django.core.files.uploadedfile import SimpleUploadedFile

from sommelier import models


def create_wine(
    *,
    taste: models.Taste = models.Taste.DRY,
    kind: models.Kind = models.Kind.RED,
    country: models.Country = models.Country.AUSTRALIA,
    type: str = 'Shiraz Cabernet',
    name: str = 'Shiraz Cabernet',
    producer: str = "JACOB'S CREEK",
):
    return models.Wine.objects.create(
        taste=taste,
        kind=kind,
        country=country,
        type=type,
        name=name,
        producer=producer,
    )


def create_bottle(
    wine: models.Wine,
    *,
    year: int = 2024,
    image: SimpleUploadedFile | None = None,
    score: float = 8,
    description: str | None = None,
):
    return models.Bottle.objects.create(
        wine=wine,
        year=year,
        image=image,
        score=score,
        description=description,
    )


def create_shop_info(
    bottle: models.Bottle,
    *,
    shop_name: models.Shop.GROSZEK,
    price: float = 30.0,
    date: dt.datetime = dt.datetime.now().date,
):
    return models.ShopInfo.objects.create(
        bottle=bottle,
        shop_name=shop_name,
        price=price,
        date=date,
    )

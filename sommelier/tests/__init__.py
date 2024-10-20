import datetime as dt

from django.core.files.uploadedfile import SimpleUploadedFile

from sommelier import models


def create_wine(
    *,
    taste: models.Taste = models.Taste.DRY,
    kind: models.Kind = models.Kind.RED,
    country: models.Country = models.Country.AUSTRALIA,
    wine_type: str = 'wine type',
    name: str = 'wine name',
    producer: str = 'wine producer',
):
    return models.Wine.objects.create(
        taste=taste,
        kind=kind,
        country=country,
        type=wine_type,
        name=name,
        producer=producer,
    )


def update_wine(
    wine: models.Wine,
    *,
    taste: models.Taste | None = None,
    kind: models.Kind | None = None,
    country: models.Country | None = None,
    wine_type: str | None = None,
    name: str | None = None,
    producer: str | None = None,
):
    if taste is not None:
        wine.taste = taste
    if kind is not None:
        wine.kind = kind
    if country is not None:
        wine.country = country
    if wine_type is not None:
        wine.type = wine_type
    if name is not None:
        wine.name = name
    if producer is not None:
        wine.producer = producer
    wine.save()


def create_bottle(
    wine: models.Wine,
    *,
    year: int = 2024,
    image: SimpleUploadedFile | None = None,
    score: float = 8.0,
    description: str | None = None,
):
    return models.Bottle.objects.create(
        wine=wine,
        year=year,
        image=image,
        score=score,
        description=description,
    )


def update_bottle(
    bottle: models.Bottle,
    *,
    year: int | None = None,
    image: SimpleUploadedFile | None = None,
    score: float | None = None,
    description: str | None = None,
):
    if year is not None:
        bottle.year = year
    if image is not None:
        bottle.image = image
    if score is not None:
        bottle.score = score
    if description is not None:
        bottle.description = description
    bottle.save()


def create_purchase_info(
    bottle: models.Bottle,
    *,
    shop_name: models.Shop = models.Shop.GROSZEK,
    price: float = 30.0,
    date: dt.date | None = None
):
    if date is None:
        date = dt.datetime.now().date()
    return models.PurchaseInfo.objects.create(
        bottle=bottle,
        shop_name=shop_name,
        price=price,
        date=date.isoformat(),
    )


def update_purchase_info(
    purchase_info: models.PurchaseInfo,
    *,
    shop_name: models.Shop | None = None,
    price: float | None = None,
    date: dt.date | None = None,
):
    if shop_name is not None:
        purchase_info.shop_name = shop_name
    if price is not None:
        purchase_info.price = price
    if date is not None:
        purchase_info.date = date.isoformat()
    purchase_info.save()

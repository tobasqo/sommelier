from django.contrib import admin

from sommelier import models


@admin.register(models.Wine)
class WineAdmin(admin.ModelAdmin):
    # TODO: add inline bottles
    pass


@admin.register(models.Bottle)
class BottleAdmin(admin.ModelAdmin):
    # TODO: add inline shop infos
    pass


@admin.register(models.ShopInfo)
class ShopInfoAdmin(admin.ModelAdmin):
    pass

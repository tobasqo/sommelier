from django.contrib import admin

from sommelier import models


@admin.register(models.Wine)
class WineAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bottle)
class BottleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ShopInfo)
class ShopInfoAdmin(admin.ModelAdmin):
    pass

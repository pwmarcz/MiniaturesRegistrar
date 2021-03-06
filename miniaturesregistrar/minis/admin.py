from django.contrib import admin
from minis.models import System, Army, Miniature, PaintManufacturer, Paint, Element

# Register your models here.


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Army)
class ArmyAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Miniature)
class MiniaturesAdmin(admin.ModelAdmin):
    list_display = ("name", "mini_image")


@admin.register(PaintManufacturer)
class PaintManufacturerAdmin(admin.ModelAdmin):
    # list_display = ("manufacturer", )
    pass


@admin.register(Paint)
class PaintAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ("number", )

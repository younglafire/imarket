from django.contrib import admin
from .models import Guitar, Fuzz, Amp


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'body_type', 'created_at')
    list_filter = ('brand', 'body_type', 'pickup_configuration')
    search_fields = ('name', 'brand', 'description')
    ordering = ('-created_at',)


@admin.register(Fuzz)
class FuzzAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'fuzz_type', 'created_at')
    list_filter = ('brand', 'fuzz_type')
    search_fields = ('name', 'brand', 'description')
    ordering = ('-created_at',)


@admin.register(Amp)
class AmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'wattage', 'amp_type', 'created_at')
    list_filter = ('brand', 'amp_type', 'wattage')
    search_fields = ('name', 'brand', 'description')
    ordering = ('-created_at',)

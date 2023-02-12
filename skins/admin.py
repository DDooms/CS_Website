from django.contrib import admin
from .models import Skin, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class SkinAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'exterior_quality', 'rarity')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Skin, SkinAdmin)
admin.site.site_url = '/home'

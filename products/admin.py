from django.contrib import admin

from .models import Category, Product, Vat, Unit


@admin.register(Vat)
class VatAdmin(admin.ModelAdmin):
    list_display = ['vat_title', 'value']
    search_fields = ['vat_title', 'value']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['cat_title']
    list_display = ['cat_title', 'active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pro_title', 'category', 'qanty', 'active']
    search_fields = ['pro_title', 'category', 'qanty', 'active']
    list_filter = ['active', 'category']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['unit_title', 'char']
    search_fields = ['unit_title', 'char']
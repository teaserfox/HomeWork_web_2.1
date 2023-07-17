from django.contrib import admin
from catalog.templates.catalog.models.Category import Category
from catalog.templates.catalog.models.Products import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'name', 'purchase_price']
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

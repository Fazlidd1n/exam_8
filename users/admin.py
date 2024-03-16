from django.contrib import admin

from users.models import Category, Product


@admin.register(Category)
class CategoryMPTTModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

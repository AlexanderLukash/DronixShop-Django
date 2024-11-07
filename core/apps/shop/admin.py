from django.contrib import admin

from unfold.admin import ModelAdmin

from core.apps.shop.models.categories import Category
from core.apps.shop.models.products import Product


# Admin view for category
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name", "parent", "slug", "created_at", "updated_at")
    list_display_links = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["id"]


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
        "brand",
        "price",
        "slug",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_display_links = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["id"]

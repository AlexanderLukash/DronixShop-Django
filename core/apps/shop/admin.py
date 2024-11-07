from django.contrib import admin

from unfold.admin import ModelAdmin

from core.apps.shop.models.categories import Category


# Admin view for category
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name", "parent", "slug", "created_at", "updated_at")

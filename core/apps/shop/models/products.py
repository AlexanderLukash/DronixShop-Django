from django.db import models
from django.urls import reverse

from core.apps.common.models import TimedBaseModel
from core.apps.shop.models.categories import Category


# Models for products
class Product(TimedBaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    title = models.CharField(
        verbose_name="Title",
        max_length=250,
    )
    brand = models.CharField(
        verbose_name="Brand",
        max_length=250,
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
    )
    slug = models.SlugField(
        verbose_name="URL",
        max_length=250,
        unique=True,
        null=False,
        editable=True,
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=7,
        decimal_places=2,
        default=99.99,
    )
    image = models.ImageField(
        verbose_name="Image",
        upload_to="products",
        blank=True,
        null=True,
    )
    available = models.BooleanField(
        verbose_name="Available",
        default=True,
    )
    is_active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True

from django.db import models
from django.urls import reverse

from core.apps.common.models import TimedBaseModel
from core.apps.shop.entities.products import ProductEntity
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
        upload_to="products/%Y/%m/%d/images/",
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

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            category=self.category,
            title=self.title,
            brand=self.brand,
            description=self.description,
            slug=self.slug,
            price=self.price,
            image=self.image.url if self.image else None,
            available=self.available,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True

from django.db import models


# Models for categories
class Category(models.Model):
    name = models.CharField(
        max_length=250,
        db_index=True,
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
    )
    slug_field = models.SlugField(
        max_length=250,
        unique=True,
        null=False,
        editable=True,
    )

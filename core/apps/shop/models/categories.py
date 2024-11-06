from django.db import models
# from django.urls import reverse
from django.utils.text import slugify

from core.apps.common.models import TimedBaseModel, rand_slug
from core.apps.shop.entities.categories import CategoryEntity


# Models for categories
class Category(TimedBaseModel):
    name = models.CharField(
        verbose_name='Category',
        max_length=250,
        db_index=True,
    )
    parent = models.ForeignKey(
        verbose_name='Parent',
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=250,
        unique=True,
        null=False,
        editable=True,
    )

    def to_entity(self) -> CategoryEntity:
        return CategoryEntity(
            id=self.id,
            name=self.name,
            parent_id=self.parent.id,
            slug=self.slug,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        unique_together = (['slug', 'parent'])
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(f'{rand_slug()}-pickBetter{self.name}')
        super(Category, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse

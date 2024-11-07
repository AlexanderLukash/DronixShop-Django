from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

from core.apps.shop.models.categories import Category


@dataclass
class ProductEntity:
    id: Optional[int]
    category: Category
    title: str
    brand: str
    description: str
    slug: str
    price: Decimal
    image: Optional[str]
    available: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    def __str__(self):
        return f"{self.title} by {self.brand}"

    def get_absolute_url(self):
        return f"/product/{self.id}/" if self.id else None

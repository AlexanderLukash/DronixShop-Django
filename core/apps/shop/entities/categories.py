from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from core.apps.shop.models.categories import Category


@dataclass
class CategoryEntity:
    id: int  # noqa
    name: str
    parent: Optional[Category]
    slug: str
    created_at: datetime
    updated_at: datetime

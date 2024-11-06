from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CategoryEntity:
    id: int  # noqa
    name: str
    parent_id: Optional[int]
    slug: str
    created_at: datetime
    updated_at: datetime

from dataclasses import dataclass
from datetime import datetime
from typing import (
    Any,
    Optional,
)


@dataclass
class CategoryEntity:
    id: int  # noqa
    name: str
    parent: Optional[Any]
    slug: str
    created_at: datetime
    updated_at: datetime

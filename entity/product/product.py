from entity.color.color import Color
from entity.size.size import Size

from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    id: int
    name: str
    code: str
    category: str
    unit_price: float
    inventory: int
    sizes: List[Size] = field(default_factory=list)
    colors: List[Color] = field(default_factory=list)
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    code: str
    category: str
    size: str
    unit_price: float
    inventory: int
    color: str
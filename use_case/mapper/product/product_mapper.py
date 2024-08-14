from use_case.mapper.mapper_interface import BaseMapper
from entity.product.product import Product
from entity.size.size import Size
from entity.color.color import Color

class ProductMapper(BaseMapper):
    @staticmethod
    def to_dict(product: Product) -> dict:
        return {
                'id': product.id,
                'name': product.name,
                'code': product.code,
                'category': product.category,
                'unit_price': product.unit_price,
                'inventory': product.inventory,
                'sizes': [{'id': size.id, 'name': size.name} for size in product.sizes],
                'colors': [{'id': color.id, 'name': color.name} for color in product.colors]
            }
        
    @staticmethod
    def from_dict(data: dict) -> Product:
        return Product(
                    id=data["id"],
                    name=data["name"],
                    code=data["code"],
                    category=data["category"],
                    unit_price=data["unit_price"],
                    inventory=data["inventory"],
                    sizes=[Size(id=size["id"], name=size["name"]) for size in data["sizes"]],
                    colors=[Color(id=color["id"], name=color["name"]) for color in data["colors"]]
                )

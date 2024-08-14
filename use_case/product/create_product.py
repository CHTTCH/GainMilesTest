from entity.product.product import Product
from entity.color.color import Color
from entity.size.size import Size
from use_case.repository.repository_interface import RepositoryInterface
from use_case.mapper.product.product_mapper import ProductMapper
class CreateProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, data: dict):
        new_product = Product(
            id=None,
            name=data['name'],
            code=data['code'],
            category=data['category'],
            unit_price=data['unit_price'],
            inventory=data['inventory'],
            sizes=[Size(id=None, name=size) for size in data['sizes']],
            colors=[Color(id=None, name=color) for color in data['colors']]
        )

        product_dict = self.repository.add(ProductMapper.to_dict(new_product))
        #! need to replace with product_output
        return product_dict
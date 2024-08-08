from entity.product.product import Product
from use_case.repository.repository_interface import RepositoryInterface

class CreateProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, data):
        new_product = Product(
            id=None,
            name=data['name'],
            code=data['code'],
            category=data['category'],
            size=data['size'],
            unit_price=data['unit_price'],
            inventory=data['inventory'],
            color=data['color']
        )
        return self.repository.add(new_product)
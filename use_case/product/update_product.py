from use_case.repository.repository_interface import RepositoryInterface

class UpdateProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, product_id, data):
        product = self.repository.get_by_id(product_id)
        if product:
            product.name = data['name']
            product.code = data['code']
            product.category = data['category']
            product.size = data['size']
            product.unit_price = data['unit_price']
            product.inventory = data['inventory']
            product.color = data['color']
            return self.repository.update(product)
        return None

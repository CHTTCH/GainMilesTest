from use_case.repository.repository_interface import RepositoryInterface
from entity.product.product import Product
from entity.size.size import Size
from entity.color.color import Color

class ReadProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def get_all(self):
        products_dict=self.repository.get_all()
        
        if products_dict is None: return None
        else: return products_dict

    def get_by_id(self, product_id):
        product_dict=self.repository.get_by_id(product_id)

        if product_dict is None:
            return None
        else:
            return product_dict

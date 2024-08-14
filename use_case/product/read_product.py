from use_case.repository.repository_interface import RepositoryInterface
from entity.product.product import Product
from entity.size.size import Size
from entity.color.color import Color

class ReadProduct:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def get_all(self):
        product_models=self.repository.get_all()
        
        if product_models is None:
            return None
        else:
            return [
                Product(
                    id=product_model["id"],
                    name=product_model["name"],
                    code=product_model["code"],
                    category=product_model["category"],
                    unit_price=product_model["unit_price"],
                    inventory=product_model["inventory"],
                    sizes=[Size(id=size["id"], name=size["name"]) for size in product_model["sizes"]],
                    colors=[Color(id=color["id"], name=color["name"]) for color in product_model["colors"]]
                ) for product_model in product_models
            ]

    def get_by_id(self, product_id):
        product_model=self.repository.get_by_id(product_id)

        if product_model is None:
            return None
        else:
            return Product(
                    id=product_model["id"],
                    name=product_model["name"],
                    code=product_model["code"],
                    category=product_model["category"],
                    unit_price=product_model["unit_price"],
                    inventory=product_model["inventory"],
                    sizes=[Size(id=size["id"], name=size["name"]) for size in product_model["sizes"]],
                    colors=[Color(id=color["id"], name=color["name"]) for color in product_model["colors"]]
                )

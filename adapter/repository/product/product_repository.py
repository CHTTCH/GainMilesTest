from adapter.database import db
from adapter.repository.product.product_model import ProductModel
from adapter.repository.size.size_model import SizeModel
from adapter.repository.color.color_model import ColorModel
from entity.product.product import Product
from use_case.repository.repository_interface import RepositoryInterface

class ProductRepository(RepositoryInterface):
    
    def add(self, product: dict) -> ProductModel:
        new_product = ProductModel(
            name=product["name"],
            code=product["code"],
            category=product["category"],
            unit_price=product["unit_price"],
            inventory=product["inventory"]
        )
        db.session.add(new_product)
        db.session.flush()
        
        for size in product["sizes"]:
            db.session.add(SizeModel(name=size["name"], product_id=new_product.id))
            
        for color in product["colors"]:
            db.session.add(ColorModel(name=color["name"], product_id=new_product.id))
        
        db.session.commit()
        
        product["id"] = new_product.id

        return product

    def get_all(self) -> list:
        product_models=ProductModel.query.all()
        
        if product_models is None:
            return None
        else:
            return [
                {
                    'id': product_model.id,
                    'name': product_model.name,
                    'code': product_model.code,
                    'category': product_model.category,
                    'unit_price': product_model.unit_price,
                    'inventory': product_model.inventory,
                    'sizes': [{'id': size.id, 'name': size.name} for size in product_model.sizes],
                    'colors': [{'id': color.id, 'name': color.name} for color in product_model.colors]
                }
                for product_model in product_models
            ]

    def get_by_id(self, product_id: int) -> ProductModel:
        product_model=ProductModel.query.get(product_id)
        
        if product_model is None:
            return None
        else:
            return {
                'id': product_model.id,
                'name': product_model.name,
                'code': product_model.code,
                'category': product_model.category,
                'unit_price': product_model.unit_price,
                'inventory': product_model.inventory,
                'sizes': [{'id': size.id, 'name': size.name} for size in product_model.sizes],
                'colors': [{'id': color.id, 'name': color.name} for color in product_model.colors]
            }

    def update(self, product_id, product_dict: dict) -> bool:
        product_model=ProductModel.query.get(product_id)

        if product_model:
            for key, value in product_dict.items():
                if key == "sizes":
                    product_model.sizes=[SizeModel(name=color_name, product_id=product_id) for color_name in value]
                elif key == "colors":
                    product_model.colors=[ColorModel(name=size_name, product_id=product_id) for size_name in value]
                else:
                    setattr(product_model, key, value)
            db.session.commit()
            return True
        return False

    def delete(self, product_id: int) -> bool:
        product = ProductModel.query.get(product_id)
        
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False

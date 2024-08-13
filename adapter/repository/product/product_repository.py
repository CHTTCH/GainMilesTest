from adapter.database import db
from adapter.repository.product.product_model import ProductModel
from adapter.repository.size.size_model import SizeModel
from adapter.repository.color.color_model import ColorModel
from entity.product.product import Product
from use_case.repository.repository_interface import RepositoryInterface

class ProductRepository(RepositoryInterface):
    
    def __get_all_colors(self, product: Product):
        color_names=[color.name for color in product.colors]
        existing_colors = db.session.query(ColorModel).filter(ColorModel.name.in_(color_names)).all()
        existing_color_dict = {color.name: color for color in existing_colors}
        
        return existing_color_dict
    
    def __get_all_sizes(self, product: Product):
        size_names=[size.name for size in product.sizes]
        existing_sizes = db.session.query(SizeModel).filter(SizeModel.name.in_(size_names)).all()
        existing_size_dict = {size.name: size for size in existing_sizes}
        
        return existing_size_dict
        
    def add(self, product: Product) -> ProductModel:
        new_product = ProductModel(
            name=product.name,
            code=product.code,
            category=product.category,
            unit_price=product.unit_price,
            inventory=product.inventory
        )
        db.session.add(new_product)
                
        for size in product.sizes:
            existing_size_dict = self.__get_all_sizes(product=product)
            
            if size.name in existing_size_dict:
                size_model=existing_size_dict[size.name]
            else:
                size_model = SizeModel(name=size.name)    
                db.session.add(size_model)
            new_product.sizes.append(size_model)
            
        for color in product.colors:
            existing_color_dict = self.__get_all_colors(product=product)
            
            if color.name in existing_color_dict:
                color_model=existing_color_dict[color.name]
            else:
                color_model = ColorModel(name=color.name)    
                db.session.add(color_model)
            new_product.colors.append(color_model)
        
        db.session.commit()
        
        product.id = new_product.id

        return product

    def get_all(self) -> list:
        return ProductModel.query.all()

    def get_by_id(self, product_id: int) -> ProductModel:
        return ProductModel.query.get(product_id)

    def update(self, product: ProductModel) -> ProductModel:
        db.session.commit()
        return product

    def delete(self, product_id: int) -> bool:
        product = ProductModel.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False

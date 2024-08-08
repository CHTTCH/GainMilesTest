from adapter.database import db
from entity.product.product import Product
from use_case.repository.repository_interface import RepositoryInterface

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)

class ProductRepository(RepositoryInterface):
    def add(self, product: Product) -> ProductModel:
        new_product = ProductModel(
            name=product.name,
            code=product.code,
            category=product.category,
            size=product.size,
            unit_price=product.unit_price,
            inventory=product.inventory,
            color=product.color
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

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

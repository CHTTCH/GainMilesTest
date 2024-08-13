from adapter.database import db

product_size_association = db.Table('product_size_association', db.metadata,
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('size_id', db.Integer, db.ForeignKey('sizes.id'))
)

product_color_association = db.Table('product_color_association', db.metadata,
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('color_id', db.Integer, db.ForeignKey('colors.id'))
)

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    
    sizes = db.relationship('SizeModel', secondary=product_size_association, backref='products')
    colors = db.relationship('ColorModel', secondary=product_color_association, backref='products')
from adapter.database import db

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    
    sizes = db.relationship('SizeModel', cascade="all, delete-orphan")
    colors = db.relationship('ColorModel', cascade="all, delete-orphan")
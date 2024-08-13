from adapter.database import db

class SizeModel(db.Model):
    __tablename__ = 'sizes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
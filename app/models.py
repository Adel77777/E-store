from .extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    variants = db.relationship('Variant', backref='product', cascade='all, delete-orphan', lazy=True)

class Variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
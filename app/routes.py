from flask import Blueprint, render_template
from .extensions import db
from .models import Product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    featured = (Product.query.filter_by(is_active=True).order_by(Product.id.desc()).limit(4).all())
    return render_template('index.html', featured=featured)

@main.route('/shop')
def shop():
    products = (Product.query.filter_by(is_active=True).all())
    return render_template('shop.html', products=products)

@main.route('/product/<int:product_id>')
def product(product_id):
    item = db.get_or_404(Product, product_id)
    if not item.is_active:
        abort(404)
    in_stock = [v for v in item.variants if v.stock > 0]
    colors = sorted({v.color for v in in_stock})
    sizes = sorted({v.size for v in in_stock})
    return render_template('product.html', product=item, colors=colors, sizes=sizes)
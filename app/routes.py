from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    products = [
        {'name': 'Product 1', 'price': 9.99, 'image': 'https://placehold.co/300'},
        {'name': 'Product 2', 'price': 9.99, 'image': 'https://placehold.co/300'}
    ]
    return render_template('index.html', products=products)

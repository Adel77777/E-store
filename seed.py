import random
from app import create_app
from app.extensions import db
from app.models import Product, Variant

app = create_app()

NAMES = ["Classic Clog", "Kids Clog", "Slide Comfort", "Platform Clog"]
COLORS = ["Black", "White", "Red"]
SIZES = [38, 39, 40, 41, 42, 43]

with app.app_context():
    if Product.query.count() == 0:
        for i, name in enumerate(NAMES, start=1):
            product = Product(name=name,
            price = random.choice([2800, 3500, 3800, 4000]), 
            description= "Light, comfortable, and stylish footwear for everyday wear.", 
            image=f"https://placehold.co/600x600/png?text={name.replace(' ', '+')}"
            )
            for color in COLORS:
                for size in SIZES:
                    product.variants.append(Variant(color=color, size=size, stock=random.choice([0, 0, 2, 5])))
            db.session.add(product)
        db.session.commit()
        print("Database seeded successfully.", len(NAMES), "products added.")
    else:
        print("Database already seeded. No new products added.")


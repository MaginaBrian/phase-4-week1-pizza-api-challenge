from server import db, app
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        
        db.drop_all()
        db.create_all()

        
        r1 = Restaurant(name="Domino's", address="123 Main St")
        r2 = Restaurant(name="Kiki's Pizza", address="456 Oak Ave")
        db.session.add_all([r1, r2])

        
        p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
        p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        db.session.add_all([p1, p2])

        db.session.commit()

        
        rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
        rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
        db.session.add_all([rp1, rp2])

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
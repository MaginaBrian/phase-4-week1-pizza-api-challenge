# phase-4-week1-pizza-api-challenge
🍕 Pizza Restaurant API Challenge
A RESTful API for managing restaurants, pizzas, and their prices, built with Flask, SQLAlchemy, and Flask-Migrate using the MVC architecture.

🚀 Features
List all restaurants
View a restaurant and its pizzas
Delete a restaurant
List all pizzas
Add a pizza to a restaurant with a price

🛠 Technologies Used
Python 3.12
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLite
Postman

📁 Project Structure

├── server/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   ├── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_pizza_controller.py
│   ├── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
├── README.md

⚙️ Setup Instructions
Clone the repository:

git clone https://github.com/your-username/phase-4-week1-pizza-api-challenge.git
cd phase-4-week1-pizza-api-challenge

Set up virtual environment:

pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

Set Flask app:

export FLASK_APP=server

Run migrations:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the database:

python3 server/seed.py

Run the server:
flask run

📬 API Endpoints

Method	    Endpoint	                  Description
GET	       /restaurants	              List all restaurants
GET	      /restaurants/<id>	          Get restaurant and its pizzas
DELETE 	  /restaurants/<id>	          Delete a restaurant
GET	      /pizzas	                  List all pizzas
POST	  /restaurant_pizzas	           Add a pizza to a restaurant
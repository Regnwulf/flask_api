from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:254254aa@localhost:5432/customer_flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(255))
    role = db.Column(db.String(255))

    def __init__(self, age, name, role):
        self.age = age
        self.name = name
        self.role = role

# Product Schema
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'age', 'name', 'role')

# Init Schema
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})

# Create a Customer
@app.route('/customer', methods=['POST'])
def add_customer():
    age = request.json['age']
    name = request.json['name']
    role = request.json['role']
    new_customer = Customer(age, name, role)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.jsonify(new_customer)

# Get All Products
@app.route('/customer', methods=['GET'])
def get_customers():
    all_customers = Customer.query.all()
    result = customers_schema.dump(all_customers)
    return jsonify(result)

# Get Single Product
@app.route('/customer/<id>', methods=['GET'])
def get_customer(id):
    customer_get = Customer.query.get(id)
    return customer_schema.jsonify(customer_get)

# Update a Customer
@app.route('/customer/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)
    age = request.json['age']
    name = request.json['name']
    role = request.json['role']
    customer.age = age
    customer.name = name
    customer.role = role
    db.session.commit()
    return customer_schema.jsonify(customer)

# Delete Product
@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return customer_schema.jsonify(customer)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

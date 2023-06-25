import json
from flask import Flask, request

from database.handlers.customers_handler import CustomersHandler
from database.mysql_wrapper import MySqlWrapper
from database.constants import DATABASE, PASSWORD, USERNAME

app = Flask(__name__)
# Initialize the MySqlWrapper
mysql_wrapper = MySqlWrapper(USERNAME, PASSWORD, DATABASE)
# Initialize the customers handler
customers_handler = CustomersHandler(mysql_wrapper)

@app.route('/<int:id>', methods=['GET'])
def get_customer(id):
    customers = customers_handler.get_customers(['*'], f'customer_id = {id}')
    return json.dumps(customers), 200

@app.route('/', methods=['GET'])
def get_customers():
    customers = customers_handler.get_customers("*", '')
    return json.dumps(customers), 200

@app.route('/create_customer', methods=['POST'])
def create_customer():
    customer_data = json.loads(request.data)
    customers_handler.create_customer(customer_data)
    return customer_data, 201

@app.route('/update_customer/<int:id>', methods=['PUT'])
def update_customer(id):
    customer_data = json.loads(request.data)
    customers_handler.update_customers(customer_data, f'customer_id = {id}')
    return customer_data, 200

@app.route('/delete_customer/<int:id>', methods=['DELETE'])
def delete_resource(id):
    customers_handler.delete_customers(f'customer_id = {id}')
    return 'Customer deleted', 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
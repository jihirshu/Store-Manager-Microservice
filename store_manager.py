from flask import Flask
from flask import jsonify

app = Flask(__name__)

import csv
inventory = {}
with open('inventory.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if (row[0] == 'item_id'):
            continue
        id = row[0].strip()
        name = row[1].strip()
        qty = int(row[2].strip())
        price = float(row[3].strip())
        print(id, name, qty, price)
        if (id not in inventory.keys()):
            inventory[id] = {}
            inventory[id]['name'] = name
            inventory[id]['qty'] = qty
            inventory[id]['price'] = price
        else:
            if (inventory[id]['name'] == name and inventory[id]['price'] == price):
                inventory[id]['qty'] = inventory[id]['qty'] + qty
            else:
                raise Exception('Same item id but different name or price attributes')



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("Welcome to the store manager MicroService")
    return 'Welcome to the store manager MicroService'


@app.route('/items')
def get_items():
    items = {}
    for item in inventory.keys():
        if item not in items.keys():
            items[item] = inventory[item]['name']
    return jsonify(items)

@app.route('/sell/<item>/<qty>')
def knapsack_solver(item, qty):

    qty = int(qty)
    if item not in inventory.keys():
        return jsonify("Invalid item code : Does not exist in the database")

    if (qty > inventory[item]['qty']):
        return jsonify("Requested quantity exceeds inventory quantity")

    inventory[item]['qty'] = inventory[item]['qty'] - qty

    pay = inventory[item]['price'] * qty

    return jsonify("Please collect %.2f $ and sell the items" % pay)

@app.route('/inventory')
def show():
    return jsonify(inventory)

@app.route('/item/<item>')
def get_item(item):
    if item not in inventory.keys():
        return jsonify("Item code does not exist in the database")

    return jsonify(inventory[item])

@app.route('/order/<item>/<qty>')
def order(item, qty):
    qty = int(qty)
    if item not in inventory.keys():
        return jsonify("Item code does not exist in the database")
    inventory[item]['qty'] = inventory[item]['qty'] + qty

    return jsonify("Inventory updated",inventory)

@app.route('/add_new/<item>/<name>/<price>/<qty>')
def addNew(item, name, price, qty):
    qty = int(qty)
    price = float(price)

    if item  in inventory.keys():
        return jsonify("Item code already exists in the database")
    inventory[item] = {}

    inventory[item]['name'] = name
    inventory[item]['qty'] = qty
    inventory[item]['price'] = price

    return jsonify("Inventory updated",inventory)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Store-Manager-Microservice

A sample micro service for store inventory management

Steps

1. Create a virtual environment -- virtualenv env
2. Activate the environment -- source env/bin/activate
3. install prerequisites -- make install
4. run the service -- python store_manager.py

Go to http://127.0.0.1:5000/

Use http://127.0.0.1:5000/inventory to get the entire inventory details

Use http://127.0.0.1:5000/items to get the items and their ids

Use http://127.0.0.1:5000/sell/<item_id>/<qty> to update the inventory with respect to sold item and quantity 
For example : http://127.0.0.1:5000/sell/001/34 means 34 units of item id 001 was sold

Use http://127.0.0.1:5000/item/<item_id> to get data about a particular item

Use http://127.0.0.1:5000/order/<item_id>/<qty> to add item quantity to inventory

Use http://127.0.0.1:5000/add_new/<item>/<name>/<price>/<qty> to add a new item to the inventory

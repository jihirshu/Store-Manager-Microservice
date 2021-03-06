# Store-Manager-Microservice

A sample micro service for store inventory management

Docker implementation :

docker build -t store_manager .  
docker run -p 5000:5000 store_manager  


Go to [http://0.0.0.0:5000/](http://0.0.0.0:5000/)

Use [http://0.0.0.0:5000/inventory] (http://0.0.0.0:5000/inventory) to get the entire inventory details

Use [http://0.0.0.0:5000/items] (http://0.0.0.0:5000/items) to get the items and their ids

Use http://0.0.0.0:5000/sell/<item_id>/<qty> to update the inventory with respect to sold item and quantity 
For example : [http://0.0.0.0:5000/sell/001/34] (http://0.0.0.0:5000/sell/001/34) means 34 units of item id 001 was sold

Use http://0.0.0.0:5000/item/<item_id> to get data about a particular item

Use http://0.0.0.0:5000/order/<item_id>/<qty> to add item quantity to inventory

Use http://0.0.0.0:5000/add_new/<item>/<name>/<price>/<qty> to add a new item to the inventory

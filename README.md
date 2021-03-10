# Store-Manager-Microservice

### A sample micro service for store inventory management
A very basic API to demonstrate a Flask based microservice in a docker container

#### Docker implementation :


	docker build -t store_manager .  
	docker run -p 5000:5000 store_manager  


##### Welcome Page -- Go to [http://0.0.0.0:5000/](http://0.0.0.0:5000/)


##### Inventory  --   http://0.0.0.0:5000/inventory 

##### Get item details -  http://0.0.0.0:5000/items

##### Inventory update after sale - http://0.0.0.0:5000/sell/<*itemID*>/<*qty*> 
###### For example : [http://0.0.0.0:5000/sell/001/34] (http://0.0.0.0:5000/sell/001/34) means 34 units of item id 001 was sold

##### Get item data - http://0.0.0.0:5000/item/<*itemID*> 

##### Add item quantity to inventory - http://0.0.0.0:5000/order/<*itemID*>/<*qty*>

##### Add new item to inventory - http://0.0.0.0:5000/add_new/<*itemID*>/<*name*>/<*price*>/<*qty*>


### Alternate Installation 

1. cd to repo directory
2. Create a virtual environment -- virtualenv env
3. Activate the environment -- source env/bin/activate
4. install prerequisites -- make install
5. run the service -- python store_manager.py

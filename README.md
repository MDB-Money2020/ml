# Suggestions 
Suggestions feature implementation.

### How it Works:
The current version is very simple. We take our feature space, demean,
 and normalize. In this space, we compute an average cosine similarity 
 of menu item vs historical orders of a user. We take the argmax of 
 these cosine similarity scores to determine the general closeness a 
 user is with a certain menu item. Future iterations are possible.

### Structure
The Flask server is located in `suggestion_server.py`. It sets up the 
server and starts running it.

`online_model.py` contains a pre-trained model that will run on the 
historic orders of a user and the menu items of a restaurant.

`fb` module contains firebase helper functions. These do not actually
directly access the firebase database; instead it uses the Node server
backend for smart cashier which provides helper functions.

`offline_model` module contains code for training the model.

### Usage
The server will take in two parameters in 
a GET request: `userId` and `restaurantId` 
which are both strings. It will return a json list of `menuIds`. If
the two parameters are not supplied, a 400 request is returned, otherwise
200. The URL is: smartcash-suggestions.herokuapp.com.

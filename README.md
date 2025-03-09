# crudapp
#UserManagement API #
This flask app allows the client to GET users in the db and also add  new users
Its intergrated with a sqlite db it also has both api and web pages

#installation steps #
Clone this repository 
#endpoints #
 @app.route('/get_users', methods=[‘GET’])  – returns the users in the db
@app.route('/add_users'/<uid>, methods=[‘POST’]) – adds a new user to the db
@app.route('/update_users'/<uid>, methods=[‘PUT’]) – update a user’s details 



#requirements#
Python 3.x




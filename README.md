# Used Items For Sale
Implementing a project as part of the Udaity Full Stack Web Developr nano-degree.
This project enables to list items for sale in a used items web site. It enables users to sign/log-in with their Google or Facebook accounts and then add/edit/delete items for sale. 
The items are listed according to categories. 

#Technology used
- Python 2.7 
- Flask web framework
- Sqlalchemy with an sqLligtht database

#A bit about how the web app works
- Flask is used to create a web app server wcich is configured to run locally on http://localhost and port 5000
- Each URL which is entered is checked inside the app and based on the route the app is running a function which then creates the output to be presented back to the user. 
- Some actions require loggin. This is supported using Google and Facebook Oauth 2.0 login. 
- The mechanisms for both Facebook and Google are using an app ID and secret which I generated in the Facebook/Google developers web site. To create your own app-sign in you can create your own IDs and secret and then need to replace the specific files to new ones (client_secrets.json and fb_client_secrets.json).
- The app also implements JSON end points 

## Running the app
1) clone or download a copy and un-zip it.
2) go into the project directory
3) make sure your inside the directory that contains project.py and the add_cateogires_to_db.py, and two directories named 'templates' and 'static'.
4) Type **database_setup.py** to initialize the databse.
5) Type **add_cateogires_to_db.py** to populate the database with categories. 
6) Type **python project.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the app.
7) You can view existing items (at the begining there are no items).
8) To add an item log-in with your Facebook or Google accounts.
Then you can add items, edit and delete them if required.

For each new item you must add also an image. 



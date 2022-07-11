# Flask-BookInventoryManagement_GoogleBookAPI
This is a Flask Book Inventory Management designed using the Google Book API.

In the <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/tree/main/code"><b>code</b></a> folder:
- The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/tree/main/code/models">models</a> folder which stores the Database Model related code for book, store and user.
- The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/tree/main/code/resources">resources</a> folder which stores the book, store and user code related to the <b>GET</b>, <b>POST</b>, <b>PUT</b> and <b>DELETE</b> operations for the API.
  - The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/resources/book.py">book.py</a> file in this resources folder has the code that retrieves data from the <b>Google Book API</b>. <i>(It is used for Retrieving Details of a Book by its ISBN number through a URL)</i>
- The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/app.py">app.py</a> file is where the URLs for performing the 4 RESTful operations are defined.
- The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/security.py">security.py</a> file is used to provide Authentication and Validation to the <b>UserModel</b>.
- The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/db.py">db.py</a> file is used to Implement SQLAlchemy through the <b>db</b> variable
- The <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/data.db">data.db</a> file stores all the Database Tables when <b>app.py</b> is executed.

<br>

Steps to Execute the Code:
- Run <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/requirements.txt">pip install -r requirements.txt</a> <i>(Preferably inside a Virtual Environment)</i>
- Delete the <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/data.db">data.db</a> file.
- Move into the <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/tree/main/code">code</a> folder and Run the command, <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/code/app.py">python app.py</a> to run the <b>Flask App</b>.
- Open <a href="https://www.postman.com/">Postman</a> while the server is running on <b>http://127.0.0.1:8000/</b> and perform the <b>GET</b>, <b>POST</b>, <b>PUT</b> and <b>DELETE</b> operations.

<br>

You can Refer to the <a href="https://github.com/n-rohit/Flask-BookInventoryManagement_GoogleBookAPI/blob/main/demo_vid.mp4">demo_vid.mp4</a> Video to understand how the code exactly works. 

<i>This is a core backend code written in Python-Flask with no front end whatsoever.</i>

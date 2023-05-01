# django-project

Open a command prompt or terminal window.

Navigate to the directory where you want to create the project.

Type the following command and hit enter:

django-admin startproject auth

Type the following command to activate the virtual environment:

for mac source env/bin/activate

This will create a new directory named "auth" containing the basic files and folders needed for a Django project.

To verify that the project was created successfully, navigate into the "auth" directory and type the following command:



Request body : 

1. Register
* URL: POST http://localhost:8000/api/register/
* Request body:
{ "email": "user@example.com", "password": "password123", "first_name": "vivek", "last_name": "jha" }   

2. Login
* URL: POST http://localhost:8000/api/login/
* Request body:{ "email": "user@example.com", "password": "password123" }   
* Response body:json{ "token": "e5b54a5b2bb8f5a5b919a5a5c5f5f5e5e5b2a5a5" }   
3. Logout
* URL: POST http://localhost:8000/api/logout/
* Authorization header: Token e5b54a5b2bb8f5a5b919a5a5c5f5f5e5e5b2a5a5 (replace the token value with the one you received from the login endpoint)
* Response body:json  Copy code{ "message": "Logged out successfully" }   


Make sure to replace http://localhost:8000 with the base URL of your Django server. Also, note that you need to have the UserSerializer imported and defined in order for the registration endpoint to work properly.




python manage.py runserver

This will start the development server. You should see output indicating that the server is running.


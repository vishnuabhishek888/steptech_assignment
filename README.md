# steptech_assignment
Django Application


1. This Django application is designed to perform the following functionalities:
a. Define a route /hello that returns the string "Hello, World!" when accessed.
b. Implement a route /users that retrieves a list of users from a MySQL database and   displays them as a list in an HTML table.
c. Implement a route /new_user that renders an HTML page to accept input from the user and stores the information in the database.
d. Create a route /users/<id> that retrieves a specific user's details from the database.




2. Setup and Run Instructions:
a. Clone the repository: git clone https://github.com/your-username/your-project.git
b. Change into the project directory: cd your-project
c. Create a virtual environment (optional): python3 -m venv venv
d. Activate the virtual environment (optional):
        For Windows: venv\Scripts\activate.bat
3. Set up the MySQL database:
       Create a new MySQL database.
       Update the database configuration in the project's settings.py file.
       Apply migrations to create the necessary tables: python manage.py migrate
         (Optional) Populate the database with sample data:
       You can manually add sample data using the Django admin interface or
        Create a script or Django management command to populate the database       

4. Run the application: python manage.py runserver
Access the application in your web browser at http://localhost:8000
     b. Database Schema and Sample Data:

The application uses a MySQL database. The schema for the users table should include the following fields:

id (primary key)
name (string)
email (string)
age (integer)
created_at (timestamp)

You can populate the database with sample data either manually using the Django admin interface or programmatically by creating a script or Django management command.
c. Additional Dependencies or Setup Requirements:
The application has the following dependencies:
Django: The web framework used to build the application.
MySQL Connector/Python: Python connector for MySQL database.
These dependencies are specified in the requirements.txt file. You can install them using pip install -r requirements.txt.
d. Git Workflow and Contribution:
To contribute to the project, follow these steps:
Fork the repository on GitHub.
Clone the forked repository: git clone https://github.com/your-username/your-project.git
Create a new branch for your changes: git checkout -b new-feature
Make your changes and commit them: git commit -am 'Add new feature'
Push the changes to your forked repository: git push origin new-feature
Create a pull request on the original repository's GitHub page to submit your changes for review and merge.
Make sure to keep your forked repository in sync with the original repository to incorporate any changes made by other contributors.
That's it! You're ready to set up and contribute to the Django application. Enjoy coding!


Write SQL queries to: 
      - Insert sample data into the "users" table.   

	INSERT INTO users (name, email, role)
VALUES
 ('Abhishek', 'abhishek@gmail.com', 'Software Developer'),
     	  ('Aman', 'aman@gmail.com', 'Frontend Developer');




      - Retrieve all users from the "users" table.   

	SELECT * FROM users;


      - Retrieve a specific user by their ID. 

	SELECT * FROM users WHERE id = <user_id>;




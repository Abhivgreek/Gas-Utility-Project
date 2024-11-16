Technologies Used
Django: Web framework for developing the backend.
SQLite (default) or any other DBMS: For managing the database.
Python 3.x: Backend programming language.
pip: Python package manager.
Project Setup
Pre-requisites
Before running the project, ensure that you have the following installed on your local machine:

Python 3.x (version 3.8 or above)
pip (Python package manager)
You can verify if Python and pip are installed by running the following commands:


python --version
pip --version
Clone the Repository
Clone this repository to your local machine using Git:


git clone https://github.com/your-username/gas-utility-service.git
cd gas-utility-service
Setup Virtual Environment
Create a new virtual environment in the project directory:


python -m venv venv
Activate the virtual environment:

On Windows:


.\venv\Scripts\activate
On macOS/Linux:


source venv/bin/activate
Your terminal prompt should now change to show the virtual environment name, like (venv).

Install Dependencies
After activating the virtual environment, install the required dependencies by running:


pip install -r requirements.txt
This will install Django and any other necessary Python packages.

Apply Migrations
Django uses migrations to handle changes to the database schema. To apply the migrations, run:


python manage.py migrate
This command will set up the database and apply any pending migrations.

Run the Development Server
To start the development server, run the following command:


python manage.py runserver
By default, the server will run at http://127.0.0.1:8000/.

You should see a message similar to the following:


Django version 4.x.x, using settings 'gas_utility_service.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Usage
API Endpoints:

/api/requests/: To submit, track, and view customer service requests.
/admin/: Admin dashboard for managing customer service requests (requires admin login).
Admin Panel: After creating a superuser, you can access the Django Admin panel at http://127.0.0.1:8000/admin/. You can manage users, view requests, and perform other administrative tasks.

To create a superuser for the Django admin, run:


python manage.py createsuperuser
Follow the prompts to set up the admin credentials.

Testing
To run tests for the project, use the following command:


python manage.py test
This will discover and run all test cases in the tests.py file of each app.

Deployment
To deploy this project to a production server, you can use WSGI servers like Gunicorn or Waitress. Here's how you can deploy using Waitress:

Install Waitress if you haven’t already:



pip install waitress
Run the application with Waitress:



waitress-serve --port=8000 gas_utility_service.wsgi:application
Make sure to configure the production database and settings as necessary for deployment.

Contributing
We welcome contributions to improve the project. To contribute, follow these steps:

Fork the repository.
Create a new branch.
Make your changes and commit them.
Push your changes to your fork.
Open a pull request with a description of your changes.
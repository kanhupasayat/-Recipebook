1= Create Virtual Environment:
Set up a virtual environment to isolate dependencies:

python -m venv env

2= Activate the Virtual Environment
Activate the virtual environment to use its dependencies:

.\env\Scripts\activate

3=Navigate to Your Django Project Directory:
Change directory to your Django project folder:

cd -Recipebook

4= Install Dependencies:
Install project dependencies listed in Requirement.txt:

pip install -r Requirement.txt

5=Apply Database Migrations:
Apply migrations to set up your database:

python manage.py migrate

6=Create a Superuser:
Create an administrative user to access the Django admin interface:

python manage.py createsuperuser


7=Run the Development Server:
Start the Django development server:

python manage.py runserver

These steps provide a clear and concise guide to setting up and running your Django project. Make sure to replace -Recipebook with the actual name of your Django project directory








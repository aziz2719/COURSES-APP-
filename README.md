#Courses
***
A simple API for users to view and create various courses
***
#Getting started
***
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
***
#Prerequisites
This is a project written using Python, Django and Django Rest Framework
***
####1. Сreating a folder
>On the desktop, create the test-project folder
***
####2. Terminal

#####In your terminal:
>Open a terminal and write commands:
>cd Desktop/test-project or cd 'Desktop'/test-project
****
####3. Clone the repository
```
https://github.com/aziz2719/COURSES-APP-.git
```
***
####4. Create the virtual enviroment
```
python3 -m venv venv
source myvenv/bin/activate
```
***
####5. Install the requirements
```
pip install -r req.txt
```
***
####6. Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
***
####7. Create a new superuser
```
python manage.py createsuperuser
```
***
####8. Run the server
```
python manage.py runserver
```
***
#Built With
>__Django - The framework used__
>__Django Rest Framework - The toolkit used to build API__
>__Swagger UI - for API documentation__
---
#Swagger UI
Run the server and go to: ```http://127.0.0.1:8000/swagger/```
***
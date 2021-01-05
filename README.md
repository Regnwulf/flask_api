# Flask API

Customer's registration Flask Restful API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Let's start!

### Prerequisites

Virtualenv

PostgreSQL Database

Setup "# Database" on ./app.py with your local PostgreSQL config.

All the application requisites are on requirements.txt root folder

### Installing

mkdir flask_api

cd flask_api

pip install virtualenv

python -m venv venv

git clone https://github.com/Regnwulf/flask_api.git

To activate venv on Windows:
\path\to\env\Scripts\activate

To activate venv on Linux:
source venv/bin/activate

pip install -r requirements.txt

Create a new Database prompt commands:

python

from app import db

db.create_all()

exit()

### Running Server

python flask run

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/) - Python SQL Toolkit
* [Psycopg](https://www.psycopg.org/docs/) - PostgreSQL database adapter for Python
* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/examples.html/) - Object serialization/deserialization library for Flask
* [PostgreSQL](https://www.postgresql.org/docs/) - PostgreSQL database


from flask_sqlalchemy import flask_sqlalchemy
from . import APP

DB = SQLAlchemy(APP)


class Dog(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    dog = DB.Column(DB.Text)
    name = DB.Column(DB.Text)
    breed = DB.Column(DB.Text)

    def __str__(self):
        return f'{self.name} is a {self.breed} and can be found at {self.dog}'

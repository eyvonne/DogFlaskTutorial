from flask import Flask, render_template, request
import requests
from .models import *
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']

    DB.init_app(app)

    @app.route('/')
    def home():
        return "Success the Flask app is running"

    @app.route('/render')
    def render():
        return render_template('home.html')

    @app.route('/renderwithinsert/<insert>')
    def render_insert(insert):
        return render_template('insert.html', insertion=insert)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return "DB reset"

    @app.route('/puppy')
    def puppy():
        json = requests.get('https://dog.ceo/api/breeds/image/random').json()
        image = json['message']
        return render_template('dog.html', picture=image)

    @app.route('/save_dog')
    def save_dog():
        json = requests.get('https://dog.ceo/api/breeds/image/random').json()
        image = json['message']
        breed = image
        return render_template('save_dog.html', picture=image, breed=image)

    @app.route('/saved_dog', methods=['POST'])
    def saved_dog():
        image = request.values['doglink']
        breed = request.values['dogbreed']
        name = request.values['name']
        dog = Dog(dog=image, name=name, breed=breed)
        DB.session.add(dog)
        DB.session.commit()
        return render_tempate('saved_dog.html', picture=image, breed=breed, name=name)

    return app

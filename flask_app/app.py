from flask import Flask, render_template
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

    @app.route('/puppy')
    def puppy():
        json = requests.get('https://dog.ceo/api/breeds/image/random').json()
        image = json['message']
        return render_template('dog.html', picture=image)

    return app

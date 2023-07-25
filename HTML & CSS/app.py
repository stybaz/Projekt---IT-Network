from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, widgets
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)
app.config['SECRET_KEY'] = "seckertkey"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pojistenci")
def pojistenci():
    return render_template("pojistenci.html")

@app.route("/pojisteni")
def pojisteni():
    return render_template("pojisteni.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/template")
def template():
    return render_template("template.html")

app.run(debug=True,port=100)
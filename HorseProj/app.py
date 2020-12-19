import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://blah:blah@ec2-54-227-254-13.compute-1.amazonaws.com:5432/HorseClub[key=2418&key=2418]'
#
# db = SQLAlchemy(app)
# db.create_all()
# db.session.commit()


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/prices')
def prices():
    return render_template("prices.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/registration')
def reg():
    return render_template("regist.html")


@app.route('/schedule')
def schedule():
    return render_template("schedule.html")


if __name__ == '__main__':
    app.run(debug=True)

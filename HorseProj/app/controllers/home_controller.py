from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/home/index')
def index():
    # ...
    return render_template(
        "home/index.html",
    )


@app.route('/about')
@app.route('/home/about')
def about():
    # ...
    return render_template(
        "home/about.html",
    )


@app.route('/prices')
@app.route('/home/prices')
def price():
    # ...
    return render_template(
        "home/prices.html",
    )

import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/shopping.html')
def shopping():
    return render_template('shopping.html')

@app.route('/shopping2.html', methods = ['GET', 'POST'])
def shopping_post():
    if request.method == 'POST':
        address = request.form['address']
        maxRange = request.form['maxRange']
        searchItem = request.form['searchItem']
        return render_template('shopping2.html', address=address, maxRange=maxRange, searchItem=searchItem)
    else:
        return render_template('shopping2.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/tutorial.html')
def tutorial():
    return render_template('tutorial.html') 

if __name__ == '__main__':
    app.debug = True
    app.run()

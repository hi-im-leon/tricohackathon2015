import sqlite3
import random
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from geopy.geocoders import Nominatim

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
        return render_template('shopping2.html', address=getLocation(address), maxRange=maxRange, searchItem=searchItem)
    else:
        return render_template('shopping2.html')

def getLocation(address):
    location = Nominatim()
    whereamI = location.geocode(address)
    return whereamI.address

def getRandomPrices():
    stores = ['Trader Joe\'s', 'MOM\'s Organic Market','ACME','Foodie\'s Market', 'Super Fresh', 'Whole Foods Market', 'Narbeth American Family Market', 'Giant', 'Spring Grocery Store', 'Swiss Farm Stores']
    base_price = random.randrange(1, 11)
    all_prices = []
    for i in range(10):
          price = round(base_price + base_price * random.random()-.3, 2)
          all_prices.append((price, stores[i]))
    all_prices.sort()
    return all_prices

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/tutorial.html')
def tutorial():
    return render_template('tutorial.html') 

if __name__ == '__main__':
    app.debug = True
    app.run()

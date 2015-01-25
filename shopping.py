import sqlite3
import random
from contextlib import closing
import random
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from geopy.geocoders import Nominatim
from yelpapi import YelpAPI
import argparse

app = Flask(__name__)
app.config.from_object(__name__)
yelp_api = YelpAPI("nYf-OcL6lk1xmoPFsBohLQ", "Kp2QhxoCwJuDES_K9oayIiQpBjA", "nDRp6rQTnRdkBPv59TD6rlYLgU7nczo5", "VJZBGBY833RIPfMGtSJg0DyAaCk")

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
        latitude = getLat(address)
        longitude = getLong(address)
        return render_template('shopping2.html', address=getLocation(address), maxRange=maxRange, searchItem=searchItem, latitude=latitude, longitude=longitude, 
            dictionary=getStores(address,maxRange), number=len(getStores(address,maxRange)), list_of_store = getRandomPrices())
    else:
        return render_template('shopping2.html')

def getRandomPrices():
    stores = ['Trader Joe\'s', 'MOM\'s Organic Market','ACME','Foodie\'s Market', 'Super Fresh', 'Whole Foods Market', 'Narbeth American Family Market', 'Giant', 'Spring Grocery Store', 'Swiss Farm Stores']
    base_price = random.randrange(1, 11)
    all_prices = []
    
    for i in range(10):
        dict_price = {}
        price = round(base_price + base_price * random.random()-.3, 2)
        dict_price["store"] = stores[i]
        dict_price["price"] = price  
        all_prices.append(dict_price)
        sorted_prices = sorted(all_prices, key=lambda k: k['price'])
    return sorted_prices


def getLocation(address):
    location = Nominatim()
    whereamI = location.geocode(address)
    return whereamI.address

def getRandomPrices():
    stores = ['Trader Joe\'s', 'MOM\'s Organic Market','ACME','Foodie\'s Market', 'Super Fresh', 'Whole Foods Market', 'Narbeth American Family Market', 'Giant', 'Spring Grocery Store', 'Swiss Farm Stores']
    base_price = random.randrange(1, 11)
    all_prices = []
    
    for i in range(10):
        dict_price = {}
        price = round(base_price + base_price * random.random()-.3, 2)
        dict_price["store"] = stores[i]
        dict_price["price"] = price  
        all_prices.append(dict_price)
        sorted_prices = sorted(all_prices, key=lambda k: k['price'])
    return sorted_prices

def getLat(address):
    location = Nominatim()
    whereamI = location.geocode(address)
    return whereamI.latitude

def getLong(address):
    location = Nominatim()
    whereamI = location.geocode(address)
    return whereamI.longitude

def getStores(address, maxRange):
    storeDictionary = []
    getSearches = yelp_api.search_query(category_filter="grocery", location=address, sort=2)
    for business in getSearches["businesses"]:
        newBusiness = {}
        newBusiness["name"] = business["name"]
        print(newBusiness["name"])
        newBusiness["address"] = ', '.join(business['location']['display_address'])
        print(newBusiness["address"])
        storeDictionary.append(newBusiness)
    return storeDictionary


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/tutorial.html')
def tutorial():
    return render_template('tutorial.html') 

# YELP STUFF



if __name__ == '__main__':
    app.debug = True
    app.run()




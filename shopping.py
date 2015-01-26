import sqlite3
import random
from contextlib import closing
import random
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from geopy.geocoders import Nominatim
from yelpapi import YelpAPI
import argparse
import json

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
        dictionary = getStores(address, maxRange)
        list_of_store = getRandomPrices(dictionary)
        storeList = json.dumps(list_of_store)
        return render_template('shopping2.html', address=getLocation(address), maxRange=maxRange, searchItem=searchItem, latitude=latitude, longitude=longitude, 
            dictionary=dictionary, number=len(dictionary), list_of_store = list_of_store, storeList=storeList)
    else:
        return render_template('shopping2.html')

def getLocation(address):
    location = Nominatim()
    whereamI = location.geocode(address)
    return whereamI.address

def getRandomPrices(dictionary):
    stores2 = []
    for i in range(len(dictionary)):
        stores2.append(dictionary[i]['name'])
    base_price = random.randrange(1, 3)
    all_prices = []
    
    for i in range(len(stores2)):
        dict_price = {}
        price = round(base_price + base_price * random.random()-.3, 2)
        dict_price["store"] = stores2[i]
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
        newBusiness["address"] = ', '.join(business['location']['display_address'])
        storeDictionary.append(newBusiness)
    return storeDictionary

# def latlongList(dictionary):
#     stores1 = []
#     for i in range(len(dictionary)):
#         a = getLat(dictionary[i]["address"])
#         b = getLat(dictionary[i]["address"])
#         stores1.append(a,b)
#         print(stores1[i])
#     return stores1

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




import random
# generates random prices seperated by space


# key = item, value = base price
items_base_prices = {'apple': 1, "banana": 2, "orange": 3, "coffee":5, "sprite": 2,
	"bottled water": 1, "tomato soup": 5, "cup noodle": 2, "coke": 1, "lays" :1, "avocado": 4}

# number of stores
num_stores = 5

for item in items_base_prices:
	base_price = items_base_prices[item]
	print item,
	for i in range(num_stores-1):
		print round(base_price + base_price * random.random()-.3, 2),
	print round(base_price + base_price * random.random()-.3, 2)
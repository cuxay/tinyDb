from tinydb import TinyDB

shop_data = {
    'phones': [
        {'name': 'iphone', 'price': 1000, 'memory': 128, 'year': 2020, 'color': 'black', 'brand': 'apple'},
        {'name': 'samsung', 'price': 220, 'memory': 512, 'year': 2024, 'color': 'white', 'brand': 'samsung'},
        {'name': 'xiaomi', 'price': 500, 'memory': 128, 'year': 2010, 'color': 'black', 'brand': 'xiaomi'},
    ],
    'laptops': [
        {'name': 'macbook', 'price': 10000, 'memory': 128, 'year': 2020, 'color': 'black', 'brand': 'apple'},
        {'name': 'macbook pro', 'price': 20000, 'memory': 256, 'year': 2019, 'color': 'black', 'brand': 'apple'},
        {'name': 'macbook air', 'price': 15000, 'memory': 128, 'year': 2018, 'color': 'black', 'brand': 'apple'},
    ],
    'computers': [
        {'name': 'acer', 'price': 10000, 'memory': 128, 'year': 2021, 'color': 'black', 'brand': 'acer'},
        {'name': 'asus', 'price': 20000, 'memory': 128, 'year': 2023, 'color': 'black', 'brand': 'asus'},
        {'name': 'hp', 'price': 15000, 'memory': 128, 'year': 2024, 'color': 'black', 'brand': 'hp'},
    ]
}

db = TinyDB('shop.json')

for category, items in shop_data.items():
    table = db.table(category)
    table.insert_multiple(items)

from tinydb import TinyDB
import requests
from goods import shop_data
import json

db = TinyDB('shop.json')

for category, items in shop_data.items():
    table = db.table(category)
    table.insert_multiple(items)
    






db=TinyDB("db.json")
rn=TinyDB('randomuser.json')
user={
    'name':'suxayl',
    'surname':'bobomirzayev',
    'age':20,
    'job':'student',
    
}
user2={
    'name':'otash',
    'surname':'abdurasulov',
    'age':18,
    'job':'student',
}


url='https://randommer.io/api/Name?nameType=fullname&quantity=26'
headers={
    'X-API-KEY':'ddbcf37d25694fb79c4773d46e59da4d' 
}
response=requests.get(url,headers=headers)
r=response.json()
for i in r:
    rn.insert({'fullname':f'{i}'})
db.insert(user2)
db.insert(user)


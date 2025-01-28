from tinydb import TinyDB
import requests
import json
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
print(r)
print('hello world')
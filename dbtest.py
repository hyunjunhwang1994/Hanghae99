from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:sparta@cluster0.jmcjmfs.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta.study

doc = {'image': 'image-src', 'name':'라이츄', 'store':'CU방배점', 'stock':3}
db.poketmons.insert_one(doc)
doc = {'image': 'image-src', 'name':'콘치', 'store':'GS관악점','stock':0}
db.poketmons.insert_one(doc)
doc = {'image': 'image-src', 'name':'콘치', 'store':'GS서초점','stock':1}
db.poketmons.insert_one(doc)
doc = {'image': 'image-src', 'name':'몬스터', 'store':'GS강남점','stock':0}
db.poketmons.insert_one(doc)

doc = {'image': 'image-src', 'name':'피카츄', 'store':'CU방배점', 'stock':3}
db.poketmons.insert_one(doc)
doc = {'image': 'image-src', 'name':'피카츄', 'store':'GS관악점','stock':0}
db.poketmons.insert_one(doc)
doc = {'image': 'image-src', 'name':'꼬부기', 'store':'GS서초점','stock':1}
db.poketmons.insert_one(doc)
doc = {'image': 'image-src', 'name':'꼬부기', 'store':'GS강남점','stock':0}
db.poketmons.insert_one(doc)
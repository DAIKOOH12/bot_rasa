import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbtest1"]

from bs4 import BeautifulSoup
cm = mydb["training1"]
chimuc = cm.find({"Content": { "$regex": "\n" }})
i = 0
for x in chimuc:
    nd = x["Content"]
    if nd.find('\n') > 0:
        i += 1
        cm.update_many({"Content": { "$regex": "\n" }},{"$set": {"Content": x['Content'].replace('\n', '<br>')}})
# print(i)
import yaml

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbtest1"]
chimuc = mydb["training"]
cm = chimuc.find({"DeMuc": "8b06986b-89cf-4a8d-8a2f-e14ff9e3123e"})
# # names_yaml = {}
# i = 0
#
import re
for x in cm:
    names_yaml = "-[" + x["Content"] + "](chimuc:" + x["Value"] + ")"
    splCharReplaceList = re.sub("[!@#$%^&*{};:,./<>?`|~=_\t+]", " ", names_yaml)
    names = yaml.safe_load(splCharReplaceList)
    with open('./data/nlum.yml', 'a', encoding = "utf-8") as file:
        yaml.dump(names, file, default_flow_style = False, allow_unicode = True, encoding = None)

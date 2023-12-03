import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbtest1"]
dblist = myclient.list_database_names()
# print(dblist)
# cd =
# for x in mycol.find():
#     print(x)

from bs4 import BeautifulSoup

demuc = mydb["jdDeMuc"]
dm = demuc.find({"Text": "Biên giới quốc gia"})
for d in dm:
    with open("./demuc/" + d["Value"] + ".html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        nd = soup.find_all("p", attrs={"class": "pNoiDung"})
        dieu = soup.find_all("p", attrs={"class": "pDieu"})
        ghiChu = soup.find_all("p", attrs={"class": "pGhiChu"})

        # for b in ghiChu:
        #     allLink

        link = soup.find_all("a", attrs={"class": ""})
        # ghichu = soup.find_all("p", attrs={"class": "pGhiChu"})
        i = 0
        for x in dieu:
            ma_dieu = x.a
            # link = ghichu[i].a["href"]
            # nd_link = ghichu[i].a.text.strip()
            mycol = mydb["training1"]
            mycol.insert_one(
                {"Value": ma_dieu["name"], "Name": x.text.strip(), "Content": nd[i].text.strip(), "DeMuc": d["Value"],
                 "ghiChu": ghiChu[i].text.strip()})
            # print(ma_dieu['name'] + " " + x.text.strip() + " - " + nd_link + ": " + link)
            # print(nd[i].text.strip())
            i += 1
        # print(i)


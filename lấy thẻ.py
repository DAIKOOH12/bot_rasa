
# lấy thẻ trên trang web
import requests
from bs4 import BeautifulSoup
#
# url = 'http://127.0.0.1:5500/demuc/0abd54e4-923f-48a3-9f22-b9672dcf4185.html'
# response = requests.get(url)
#
# if response.status_code == 200:
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')
#
#     # Tiếp tục xử lý với BeautifulSoup theo cách bạn muốn
#     # ...
#     # Tìm tất cả các div có class là "container"
#     divs = soup.find_all('div', class_='picturebox')
#
#     # Lặp qua từng div để lấy nội dung của thẻ <p> sâu trong div
#     for div in divs:
#         paragraph = div.find('a')
#         if paragraph:
#             print("Nội dung của thẻ a:", paragraph.get('title'))
#             # print("href: ", paragraph.get('href'))
#             print("\n")
# else:
#     print(f"Failed to fetch the webpage. Status code: {response.status_code}")


#test kết nối mongodb
from pymongo import MongoClient
import pymongo

client = MongoClient('mongodb://localhost:27017/')

db = client["dbtest1"]
tra = db['training1']
# # hung = tra.create_index([('Name', "text")], name = 'index_name')
# nd = tra.find({ "$text": {"$search": "Kiểm tra, giám sát cửa khẩu phụ" } },{ "score": { "$meta": "textScore" }}).sort([("score", pymongo.DESCENDING)]).limit(1)
# hung1 = tra.list_indexes()
# print(nd['Content'])
# print(hun
#
# g1)

# if 'Content' in nd:
#     print(nd['Content'])

# for document in nd:
#     if 'Content' in document:
#         print(document['Content'])
#     else:
#         print("Document does not have a 'content' field")
#

query = { "$text": {"$search": "Kiểm tra, giám sát cửa khẩu phụ" } }
projection = { "score": { "$meta": "textScore" } }

# Thực hiện truy vấn và sắp xếp kết quả
results = tra.find(query, projection).sort([("score", {"$meta": "textScore"})]).limit(5)

# In kết quả
for result in results:
    print(result['Content']+ "\nhaha")
    break

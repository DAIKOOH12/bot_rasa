# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk import Action
import requests
from bs4 import BeautifulSoup
from rasa_sdk.executor import CollectingDispatcher
import feedparser
import pymongo


class action_get_document(Action):
    def name(self):
        return 'action_get_document'
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(self.get_document())
        return []
    def get_document(self):
        url = 'http://www.fithou.edu.vn/'
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Tiếp tục xử lý với BeautifulSoup theo cách bạn muốn
            # ...
            # Tìm tất cả các div có class là "container"
            divs = soup.find_all('div', class_='picturebox')

            # Lặp qua từng div để lấy nội dung của thẻ <p> sâu trong div
            for div in divs:
                paragraph = div.find('a')
                if paragraph:
                    # print("Nội dung của thẻ a:", paragraph.get('title'))
                    return paragraph.get('title')
        else:
            return "false"
                # print(f"Failed to fetch the webpage. Status code: {response.status_code}")

class action_ask_adr(Action):
    def name(self):
        return 'action_ask_adr'

    def run(self, dispatcher, tracker, domain):
        employee_name = tracker.get_slot('CL_name')

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["keke"]
        employees = db["caNhan"]
        addresses = db["diaChi"]

        employee = employees.find_one({"tên": employee_name})
        if employee:
            address = addresses.find_one({"id_cá_nhân": employee["_id"]})

            # if address['địa_chỉ'] != "":
        #     dispatcher.utter_message(text=f"Địa chỉ của {employee_name} là {address['địa_chỉ']}.")
        # else:
        #     dispatcher.utter_message(text=f"Không tìm thấy")
            if address and address['địa_chỉ'] != "":
                dispatcher.utter_message(text=f"Địa chỉ của {employee_name} là {address['địa_chỉ']}.")
            else:
                dispatcher.utter_message(text=f"Không tìm thấy địa chỉ của {employee_name}")
        else:
            dispatcher.utter_message(text=f"Không tìm thấy nhân viên tên {employee_name}")
        return []

class action_nd_luat(Action):
    def name(self):
        return 'action_nd_luat'

    def run(self, dispatcher, tracker, domain):
        # return []
        ten = tracker.get_slot('ten_luat')
        #
        client = pymongo.MongoClient('mongodb://localhost:27017/')

        db = client["dbtest1"]
        tra = db['training1']
        #
        # # nd = tra.find({"$text": {"$search": ten}},{"score": {"$meta": "textScore"}}).sort([("score", pymongo.DESCENDING)]).limit(1)
        # # for document in nd:
        # #     if 'Content' in document:
        # #         dispatcher.utter_message(text=f"{document['Content']}")
        # #         break
        # #     else:
        # #         dispatcher.utter_message(text="Document does not have a 'content' field")
        #
        query = {"$text": {"$search": ten}}
        projection = {"score": {"$meta": "textScore"}}

        # Thực hiện truy vấn và sắp xếp kết quả
        results = tra.find(query, projection).sort([("score", {"$meta": "textScore"})]).limit(1)

        for result in results:
            dispatcher.utter_message(text=f"{result['Name']} ({result['link']}) \n {result['Content']}")


        # dispatcher.utter_message(ten)
        # return []



#dung đã sửa ở đây




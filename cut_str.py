from pymongo import MongoClient
from selenium import webdriver
from bs4 import BeautifulSoup
import pymongo
def get_string(str):
    fl = str.rfind("số ")
    str1 = str[fl+len("số "): len(str)]
    new_str = ""
    for i in str1:
        if i != ',' and i != ' ':
            new_str += i
        else:
            break
    return new_str

def search_and_get_html(query):
    search_url = f"https://vbpl.vn/pages/vbpq-timkiem.aspx?type=0&s=0&SearchIn=Title,Title1&Keyword={query}"

    # Sử dụng trình duyệt Selenium
    # chromeDriver = '/home/phuong/Downloads/chromedriver_linux64/chromedriver'
    driver = webdriver.Edge()  # Hoặc sử dụng trình duyệt khác
    driver.get(search_url)

    # Lấy nội dung HTML sau khi trang đã được tải
    html_content = driver.page_source

    # Đóng trình duyệt
    driver.quit()
    return html_content

def get_date(search_query):
    # search_query = input("Nhập vào chuỗi cần tìm kiếm trên vbpl.vn: ")
    #
    # Tìm kiếm và lấy HTML
    search_result_html = search_and_get_html(search_query)

    # Kiểm tra xem có dữ liệu HTML hay không
    if search_result_html:
        soup = BeautifulSoup(search_result_html, 'html.parser')
        divs = soup.find_all('div', class_='item')
        if divs:
            for div in divs:
                titles = div.find('p')
                if titles:
                    theA = titles.find('a')
                    if search_query in theA.get_text().strip():
                        divHL = div.find('div', class_="right")
                        if divHL:
                            thePHL = divHL.find('p', class_="red")
                            if thePHL:
                                the_moi = thePHL.get_text().strip()
                                return the_moi[the_moi.find(":") + 1:len(the_moi)]
                            else:
                                return "Còn hiệu lực"
                        else:
                            return "Lỗi"
                    else:
                        continue
                else:
                    return "Lỗi"

            # for title in titles:
            #     nd = title.find('a')
            #     print(nd.get('title'))
            # print(titles.get(''))
            # if titles.get(tit)

    else:
        return "Không có dữ liệu HTML được trả về."

    return "Không tìm thấy"

client = MongoClient('mongodb://localhost:27017/')

db = client["dbtest1"]
tra = db['testHL']


# list = tra.find().limit(50)
# list = tra.find({"TrangThai": {"$exists": False}})
list = tra.find({"Name": "Điều 1.4.LQ.1."})
# for li in list:
#     print(li['Name'])

i = 0

for lis in list:
    # i+=1
    # print(i)
    key = get_string(lis['key'])
    # print("key: " + key)
    if len(key) < 10:
        # print(lis['Name'])
        continue

    result = get_date(key)
    if lis['TrangThai'] != result:
        i+=1
        print(i)
        print(lis['Name'])
        print(lis['TrangThai'])
        print(result + "\n")
    # print("result: " + result + "\n")
    #
    # # Điều kiện để xác định bản ghi cần cập nhật
    # condition = {"_id": lis['_id']}
    # #
    # # # Dữ liệu mới cần cập nhật
    # new_data = {"$set": {"TrangThai": result}}
    # #
    # # # Thực hiện câu lệnh cập nhật
    # tra.update_one(condition, new_data)



# key = input("Nhập: ")
# result = get_string(key)
# print(result)






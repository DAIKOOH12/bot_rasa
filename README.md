# ỨNG DỤNG RASA CHO VĂN BẢN PHÁP LUẬT
## Ý tưởng xây dựng
Xây dựng ứng dụng hỗ trợ người dùng tra cứu, hỏi đáp tri thức pháp luật dựa trên nguồn dữ liệu được khai thác từ Bộ Pháp điển Việt Nam và CSDL văn bản QPPL. Ứng dụng phải mang lại được các tiện ích tốt hơn cho người dùng so với các dịch vụ hiện đang được cung cấp trên mạng Internet. Nó khắc phục được điểm yếu hiện nay của Bộ Pháp điển Việt Nam là không được cập nhật kịp thời các văn bản QPPL mới đã có hiệu lực thi hành. Áp dụng các công nghệ tiên tiến về xử lý ngôn ngữ tự nhiên để tự động phân tích nội dung văn bản. Từ đó tạo ra các dịch vụ hỗ trợ người dùng tra cứu, hỏi đáp tri thức nằm trong văn bản QPPL. Dưới đây là một số gợi ý về các chức năng cần có (nhưng không giới hạn) của phần mềm ứng dụng mới.
1. Hỗ trợ tra cứu, xem các nội dung văn bản QPPL đang có hiệu lực theo trật tự sắp xếp về chủ đề, đề mục, chỉ mục và các điều giống như Bộ Pháp điển Việt Nam. Phần mềm tự động tạo liên kết giữa các điều khoản, chỉ mục được tham chiếu lẫn nhau trong nội dung của văn bản QPPL. Nó cho phép đánh dấu phân biệt các nội dung đã được và chưa được pháp điển hóa. Các nội dung chưa pháp điển hóa thì được sắp xếp theo một trật tự do phần mềm tự động tính toán gợi ý từ việc phân tích nội dung văn bản phù hợp. Người dùng có thể thực hiện phản hồi lại thông tin về mức độ chính xác của các gợi ý sắp xếp để phần mềm có thể ghi nhớ và đưa ra các cải tiến về sắp xếp phù hợp hơn cho các lần tiếp theo.
2. Phần mềm tự động trích rút các thuật ngữ, từ ngữ được định nghĩa và sử dụng trong các văn bản QPPL. Nó thực hiện đánh dấu tất cả các từ ngữ và cho xem nhanh định nghĩa được sử dụng khi tra cứu nội dung của từng điều khoản. Phần mềm cho phép tra cứu nhanh bảng chỉ mục (index) tất cả các từ ngữ và định nghĩa tương ứng của nó trong văn bản
3. Cho phép người dùng tìm kiếm nhanh để xem các nội dung văn bản QPPL liên quan theo các gợi ý về từng nhóm vấn đề và từ khóa chính hay được sử dụng trong hệ thống tri thức pháp luật của Việt Nam. Hỗ trợ sắp xếp, tìm kiếm các bảng, biểu mẫu được quy định trong các văn bản QPPL theo các nhóm thủ tục hành chính để người dùng có thể dễ dàng khai thác theo nhu cầu
4. Hỗ trợ trả lời các câu hỏi của người dùng về pháp luật dựa trên việc trích rút tri thức từ các văn bản QPPL hiện đang có hiệu lực. Phần mềm phải hiển thị nguồn tham chiếu trích dẫn các điều khoản trong văn bản nhằm trả lời cho câu hỏi của người dùng. Khi đặt câu hỏi, người dùng có thể nhận được một số gợi ý về các câu hỏi tương tự hoặc liên quan để có thể tự khám phá sâu hơn về các tri thức của pháp luật
## Triển khai dự án
### Tải dự án về cho project của bạn
1. Cấu trúc thư mục:
  - Khởi tạo 1 folder <tên_folder> để chứa project
3. Lấy kho code
  - Đối với bot rasa: 
```bash
git clone https://github.com/DAIKOOH12/bot_rasa.git

```
  - Đối với api giao diện:
```bash
git clone https://github.com/DAIKOOH12/bot_rasa.git

```
 - Lúc này trong máy sẽ có 2 folder: bot_rasa và các file/thư mục liên quan đến API
3. Các bước để tiến hàng sử dụng project
  - Trước khi mở IDE trên máy, tại thư mục root hãy viết câu lệnh sau trên **Terminal** để khởi chạy server mongodb:
  ```bash
  sudo systemctl start mongod

  ```
  - Trong máy hiện tại của bạn nên có 1 IDE sử dụng để quản lí database trong MongoDB, ở đây tôi sẽ dùng MongoDB Compass.
  - Kết nối đến cơ sở dữ liệu hoặc import dữ liệu từ file đã có sẵn để bắt đầu sử dụng project.
  - Tiếp theo, khởi động IDE liên quan để sửa đổi các đoạn mã trong project (khuyến khích sử dụng Pycharms)
  - Tại đây ta sẽ thấy câu trúc thư mục như sau:
    ![image](https://github.com/DAIKOOH12/bot_rasa/assets/95415495/43e36e28-9eca-42e3-8574-c93f77499fdd)
  - file **main.py** chính là file xử lí backend của project và thư mục **bot_rasa** chính là con bot được tích hợp vào.
  - Trước khi ta có thể gọi con bot lên giao diện thì ta cần thực hiện 1 số thao tác sau:
      - Tại **Terminal** di chuyển đến thư mục **bot_rasa**:
        ```bash
        cd bot_rasa

        ```
      - Bot rasa có 1 cấu trúc vô cùng quan trọng đó là **actions**, trước khi bạn muốn con bot hiểu câu hỏi người dùng thì việc khởi chạy **actions**
      vô cùng quan trọng.
      - Hãy thực hiện dòng lệnh để khởi chạy **actions**:
        ```bash
        rasa run actions

        ```
        => Kết quả đạt được tương ứng với hình dưới đây:
        ![image](https://github.com/DAIKOOH12/bot_rasa/assets/95415495/d8af558d-f826-4440-a9c8-0572b47824f6)

      - Tiếp theo ta cần chạy con bot trên server của rasa bot.
      - Mở 1 **Terminal** mới và thực hiện câu lệnh sau:
        ```bash
        rasa run --enable-api --debug

        ```
        => Kết quả đạt được tương ứng với hình ảnh dưới đây
        ![image](https://github.com/DAIKOOH12/bot_rasa/assets/95415495/042cdee5-a971-43c4-a44a-58c4d4aa845c)

      - Lúc này chúng ta đã khởi động được con bot, việc còn lại là ta cần khởi chạy api để có thể gọi con bot đó lên giao diện.
      - Tại file main.py đang được sử dụng framework **Flask** để xây dựng backend nên bạn cần **install Flask** cho máy.
      - Tiếp theo mở 1 **Terminal** mới (Terminal này chạy tại thư mục root), thực câu lệnh sau để chạy api trên **localhost**:
        ```bash
        python3 main.py

        ```
      - Sau khi thực hiện câu lệnh trên ta sẽ nhận được thông báo: Running on http://127.0.0.1:5000 . Truy cập dường dẫn đó và bạn sẽ nhận được kết quả dưới đây:
      ![image](https://github.com/DAIKOOH12/bot_rasa/assets/95415495/d041043f-d18c-41f7-a63e-bf56f450720b)
      - Giờ hãy thử chào hỏi, đặt câu hỏi cho con và đợi response từ nó nhé.
- Sau đây là 1 số kết quả Q&A của bot:
  ![image](https://github.com/DAIKOOH12/bot_rasa/assets/95415495/fd4a7f29-a816-458d-a03f-0cb1874c4761)
  ![image](https://github.com/DAIKOOH12/bot_rasa/assets/95415495/ae37787a-6231-4a9d-b830-ef918ed7ae6a)


- Yêu cầu:
  - Python: version >= 3.8
  - Mongodb: version >= 6.0
  - Hệ điều hành: Linux

<div align="center">

[![Join the chat on Rasa Community Forum](https://img.shields.io/badge/forum-join%20discussions-brightgreen.svg)](https://forum.rasa.com/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI version](https://badge.fury.io/py/rasa.svg)](https://badge.fury.io/py/rasa)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa.svg)](https://pypi.python.org/pypi/rasa)
[![Build Status](https://github.com/RasaHQ/rasa/workflows/Continuous%20Integration/badge.svg)](https://github.com/RasaHQ/rasa/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=RasaHQ_rasa&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=RasaHQ_rasa)
[![Documentation Status](https://img.shields.io/badge/docs-stable-brightgreen.svg)](https://rasa.com/docs)
![Documentation Build](https://img.shields.io/netlify/d2e447e4-5a5e-4dc7-be5d-7c04ae7ff706?label=Documentation%20Build)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git.svg?type=shield)](https://app.fossa.com/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git?ref=badge_shield)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/orgs/RasaHQ/projects/23)

</div>

Để xem thông tin chi tiết sẩn phẩm truy cập tại: https://docs.google.com/document/d/14Frute7pFVsCidqv1ZAf2ZiSOM2QC9YOrWXZlm5ogns/edit?usp=sharing
<h2 align="">License</h2>

Copyright (C) 2021 Dialogue Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.(C) 2021 Dialogue Technologies Inc. All rights reserved.

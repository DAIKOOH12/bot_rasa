# ỨNG DỤNG RASA CHO VĂN BẢN PHÁP LUẬT
## Ý tưởng xây dựng
Xây dựng ứng dụng hỗ trợ người dùng tra cứu, hỏi đáp tri thức pháp luật dựa trên nguồn dữ liệu được khai thác từ Bộ Pháp điển Việt Nam và CSDL văn bản QPPL. Ứng dụng phải mang lại được các tiện ích tốt hơn cho người dùng so với các dịch vụ hiện đang được cung cấp trên mạng Internet. Nó khắc phục được điểm yếu hiện nay của Bộ Pháp điển Việt Nam là không được cập nhật kịp thời các văn bản QPPL mới đã có hiệu lực thi hành. Áp dụng các công nghệ tiên tiến về xử lý ngôn ngữ tự nhiên để tự động phân tích nội dung văn bản. Từ đó tạo ra các dịch vụ hỗ trợ người dùng tra cứu, hỏi đáp tri thức nằm trong văn bản QPPL. Dưới đây là một số gợi ý về các chức năng cần có (nhưng không giới hạn) của phần mềm ứng dụng mới.
1. Hỗ trợ tra cứu, xem các nội dung văn bản QPPL đang có hiệu lực theo trật tự sắp xếp về chủ đề, đề mục, chỉ mục và các điều giống như Bộ Pháp điển Việt Nam. Phần mềm tự động tạo liên kết giữa các điều khoản, chỉ mục được tham chiếu lẫn nhau trong nội dung của văn bản QPPL. Nó cho phép đánh dấu phân biệt các nội dung đã được và chưa được pháp điển hóa. Các nội dung chưa pháp điển hóa thì được sắp xếp theo một trật tự do phần mềm tự động tính toán gợi ý từ việc phân tích nội dung văn bản phù hợp. Người dùng có thể thực hiện phản hồi lại thông tin về mức độ chính xác của các gợi ý sắp xếp để phần mềm có thể ghi nhớ và đưa ra các cải tiến về sắp xếp phù hợp hơn cho các lần tiếp theo.
2. Phần mềm tự động trích rút các thuật ngữ, từ ngữ được định nghĩa và sử dụng trong các văn bản QPPL. Nó thực hiện đánh dấu tất cả các từ ngữ và cho xem nhanh định nghĩa được sử dụng khi tra cứu nội dung của từng điều khoản. Phần mềm cho phép tra cứu nhanh bảng chỉ mục (index) tất cả các từ ngữ và định nghĩa tương ứng của nó trong văn bản
3. Cho phép người dùng tìm kiếm nhanh để xem các nội dung văn bản QPPL liên quan theo các gợi ý về từng nhóm vấn đề và từ khóa chính hay được sử dụng trong hệ thống tri thức pháp luật của Việt Nam. Hỗ trợ sắp xếp, tìm kiếm các bảng, biểu mẫu được quy định trong các văn bản QPPL theo các nhóm thủ tục hành chính để người dùng có thể dễ dàng khai thác theo nhu cầu
4. Hỗ trợ trả lời các câu hỏi của người dùng về pháp luật dựa trên việc trích rút tri thức từ các văn bản QPPL hiện đang có hiệu lực. Phần mềm phải hiển thị nguồn tham chiếu trích dẫn các điều khoản trong văn bản nhằm trả lời cho câu hỏi của người dùng. Khi đặt câu hỏi, người dùng có thể nhận được một số gợi ý về các câu hỏi tương tự hoặc liên quan để có thể tự khám phá sâu hơn về các tri thức của pháp luật
## Triển khai dự án
- Tải dự án về cho project của bạn
```bash
git clone https://github.com/DAIKOOH12/bot_rasa.git

```
- Yêu cầu:
  - Python: bản mới nhất
  - Mongodb: bản mới nhất
  - Hệ điều hành: Windows/Linux/MacOS
</br>
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

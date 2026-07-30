# 👨‍🏫 Hướng Dẫn Giáo Viên - Dạy Học Sinh Dự Án AI

Tài liệu này giúp giáo viên hướng dẫn học sinh lớp 7-8 xây dựng ứng dụng AI với Streamlit.

## 📚 Mục Tiêu Học Tập

Sau dự án này, học sinh sẽ hiểu:

✅ **AI là gì?** - AI không phải "siêu trí tuệ", chỉ là mô hình dự đoán từ dữ liệu

✅ **Function Calling** - Cách AI "gọi" các công cụ khi cần

✅ **API là gì?** - Cách các ứng dụng "nói chuyện" với nhau

✅ **Lập trình Thực Tế** - Tạo ứng dụng web thực sự mà bạn bè có thể dùng

## 🎯 Lên Kế Hoạch Dạy Học (4-5 Tiết)

### Tiết 1: Giới Thiệu (45 phút)

**Nội dung:**
- Giải thích "AI là gì"
- Demo ứng dụng hoạt động
- Giải thích từng phần code

**Hoạt động:**
- Cho học sinh chạy ứng dụng
- Hỏi: "AI làm gì để trả lời câu hỏi?"
- Hỏi: "Tại sao không phải AI tính toán mà là máy tính?"

**Kết Quả Mong Đợi:**
- Học sinh hiểu tổng quan
- Kích thích tò mò

### Tiết 2: Cài Đặt & Test (45 phút)

**Nội dung:**
- Cài Python (nếu chưa có)
- Cài Streamlit & thư viện
- Lấy Google API key
- Chạy ứng dụng

**Hoạt động:**
- Hướng dẫn từng bước
- Giáo viên giải quyết vấn đề
- Học sinh test ứng dụng

**Kết Quả Mong Đợi:**
- Mỗi học sinh có bản chạy được
- Mọi người có thể chat với AI

### Tiết 3: Hiểu Code - Phần Giao Diện (45 phút)

**Nội dung:**
- Giải thích `streamlit` (UI framework)
- Giải thích `st.write()`, `st.chat_message()`, `st.button()`
- Học sinh sửa tiêu đề, màu sắc

**Hoạt động (Workshop):**
1. Mở `app.py`
2. Thay đổi tiêu đề từ "🤖 Trợ Lý AI Đa Năng" → "🚀 [Tên của em]"
3. Thay đổi emoji
4. Chạy lại xem thay đổi

**Code Example:**
```python
# Trước
st.markdown('<h1>🤖 Trợ Lý AI Đa Năng</h1>')

# Sau (học sinh sửa)
st.markdown('<h1>🚀 Trợ Lý AI của [Tên học sinh]</h1>')
```

**Kết Quả Mong Đợi:**
- Học sinh hiểu `st.write()` là "loa phát"
- Thấy được tác dụng thay đổi code ngay lập tức

### Tiết 4: Hiểu Code - Phần Công Cụ (45 phút)

**Nội dung:**
- Giải thích `tools.py`
- Giải thích Function Calling
- Hướng dẫn thêm công cụ mới

**Hoạt động (Guided Lab):**

1. **Xem cách hoạt động:**
   - Mở `tools.py`
   - Tìm hàm `calculator()`
   - Giải thích code

2. **Test công cụ:**
   ```bash
   python test_tools.py
   ```

3. **Thêm Công Cụ Mới:**
   - Học sinh viết hàm `greet_user()` đơn giản
   ```python
   @staticmethod
   def greet_user(name: str) -> dict:
       """Chào hỏi người dùng"""
       return {
           "greeting": f"Xin chào {name}!",
           "status": "success"
       }
   ```

**Kết Quả Mong Đợi:**
- Hiểu AI gọi hàm Python như thế nào
- Biết cách thêm tính năng mới

### Tiết 5: Tự Do Sáng Tạo (45 phút)

**Nội dung:**
- Học sinh thêm công cụ riêng
- Học sinh thiết kế UI theo ý thích
- Demo cho lớp

**Gợi Ý Công Cụ:**
- 🎲 Máy phát sinh số ngẫu nhiên
- 📋 Todo list tracker
- 🎯 Mục tiêu hôm nay
- 🔐 Password generator
- 📝 Note keeper

**Hoạt động (Creative):**
- Chia nhóm 2-3 bạn
- Mỗi nhóm thêm 1-2 công cụ mới
- Demo: "AI của chúng tôi có thể..."

## 🔧 Hỗ Trợ Giáo Viên

### Vấn Đề Thường Gặp & Giải Pháp

| Vấn Đề | Nguyên Nhân | Giải Pháp |
|--------|-----------|----------|
| "Python not found" | Python không được cài hoặc PATH sai | Cài lại Python, nhớ tích "Add to PATH" |
| "API key không hoạt động" | Key sai hoặc hết hạn | Lấy key mới từ aistudio.google.com |
| "Streamlit not found" | Chưa cài streamlit | `pip install streamlit` |
| Code chạy lâu | API Google bị slow | Kiểm tra internet, cân nhắc timeout |
| Port 8501 đã dùng | Streamlit khác chạy | `streamlit run app.py --logger.level=debug` |

### Demo Code

Khi giáo viên muốn demo:

1. **Máy tính:**
   ```
   Nhập: "2 + 2 bằng mấy?"
   → AI sử dụng calculator
   → Kết quả: 8
   ```

2. **Thời tiết:**
   ```
   Nhập: "Hà Nội mưa không?"
   → AI sử dụng get_weather
   → Hiển thị dữ liệu thực
   ```

3. **Dịch:**
   ```
   Nhập: "Dịch 'I love coding' sang Việt"
   → AI sử dụng translate
   ```

## 🎓 Giải Thích Khái Niệm Cho Học Sinh

### AI Không Thực Sự "Thông Minh"

**Cách Giải Thích:**
> "AI giống như một học sinh rất giỏi nhưng chỉ biết cách trả lời dựa vào những gì nó đã học. Nó không "suy nghĩ" thực sự, chỉ dự đoán câu trả lời tiếp theo dựa trên mẫu."

**Ví Dụ:**
- Nếu hỏi "2 + 2 = ?", AI sẽ trả lời dựa trên dữ liệu học
- Nó không "suy luận" mà chỉ "nhớ lại"

### Function Calling

**Cách Giải Thích:**
> "Function Calling giống như AI nói với chúng ta: 'Tôi cần dữ liệu về thời tiết, vui lòng gọi hàm get_weather(). Tôi sẽ sử dụng kết quả để trả lời câu hỏi.'"

**Sơ đồ:**
```
Người dùng: "Thời tiết ở Hà Nội?"
    ↓
AI nhận diện: "Cần thời tiết"
    ↓
AI: "Gọi get_weather('Hanoi')"
    ↓
Python chạy get_weather() → Lấy dữ liệu
    ↓
AI nhận dữ liệu
    ↓
AI: "Trả lời cho người dùng"
```

### API

**Cách Giải Thích:**
> "API là 'bộ phận nói chuyện' giữa các ứng dụng. Khi chúng ta cần dữ liệu từ Google Gemini hoặc dự báo thời tiết, chúng ta gửi 'yêu cầu' qua API."

**Hình Minh Họa:**
```
App Của Chúng Ta ←→ API ←→ Google Gemini
              ←→ API ←→ Weather Service
              ←→ API ←→ Wikipedia
```

## 📊 Tiêu Chí Đánh Giá

### Mức Độ 1: Cơ Bản (70-79 điểm)
- ✅ Cài được ứng dụng
- ✅ Chạy được ứng dụng
- ✅ Hiểu được tổng quan

### Mức Độ 2: Tốt (80-89 điểm)
- ✅ Hiểu code
- ✅ Có thể sửa nhỏ (tiêu đề, màu sắc)
- ✅ Giải thích được Function Calling

### Mức Độ 3: Xuất Sắc (90-100 điểm)
- ✅ Thêm được công cụ mới
- ✅ Hiểu cách hoạt động của API
- ✅ Giải thích được các khái niệm AI
- ✅ Demo được cho bạn bè

## 🎨 Mở Rộng Dự Án

### Cấp Độ 1: Sửa Đơn Giản
```python
# Thay đổi tiêu đề
st.title("🚀 AI của tôi")

# Thay đổi màu sắc trong CSS
primaryColor = "#FF5733"  # Từ xanh sang đỏ
```

### Cấp Độ 2: Thêm Công Cụ
```python
@staticmethod
def birthday_countdown(birthday_date: str) -> dict:
    """Tính ngày còn lại đến sinh nhật"""
    from datetime import datetime
    today = datetime.now()
    birthday = datetime.strptime(birthday_date, "%d/%m")
    # Tính toán...
    return {"days_left": days}
```

### Cấp Độ 3: Deploy
- Đẩy code lên GitHub
- Deploy lên Streamlit Cloud
- Chia sẻ link với bạn bè

## 💡 Mẹo Dạy Hiệu Quả

1. **Học qua Làm**
   - Cho học sinh tự viết code, không chỉ copy-paste
   - Khuyến khích sửa, thử, sai lầm

2. **Kích Thích Tò Mò**
   - "Nếu ta thêm công cụ này, sẽ xảy ra gì?"
   - "Có cách nào làm nó tốt hơn không?"

3. **Kết Nối Thực Tế**
   - "ChatGPT hoạt động như thế nào? Giống cái này!"
   - "Bạn thấy không, AI không phép thuật"

4. **Chia Nhóm**
   - Học sinh giỏi giúp bạn
   - Tạo cộng đồng học tập

5. **Celebrate Success**
   - Khi ai đó thêm công cụ mới → tung hô
   - Khi ứng dụng chạy → chụp hình

## 📖 Tài Liệu Tham Khảo Cho Giáo Viên

- [Streamlit Documentation](https://docs.streamlit.io)
- [Google Generative AI Quickstart](https://ai.google.dev/docs/quickstart)
- [How LLMs Work - YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- [AI Basics Course](https://course.fast.ai)

---

**Chúc bạn dạy học vui vẻ! 🎉**

Nếu có câu hỏi, hãy liên hệ hoặc check README.md

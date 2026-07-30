# 📖 HƯỚ DẪN HOÀN CHỈNH - Trợ Lý AI Đa Năng

Tài liệu này tổng hợp tất cả những gì bạn cần biết về dự án.

---

## 🎯 TỔNG QUAN DỰ ÁN

### Dự Án Là Gì?
**Trợ Lý AI Đa Năng** là ứng dụng web được xây dựng với:
- **Giao Diện:** Streamlit (Python web framework)
- **AI Engine:** Google Gemini 1.5 Flash
- **Công Cụ:** 6 tính năng thông minh (máy tính, thời tiết, dịch, v.v.)

### Tính Năng
✅ Chat với AI  
✅ Máy tính toán học  
✅ Dự báo thời tiết  
✅ Dịch văn (8 ngôn ngữ)  
✅ Tìm kiếm thông tin (Wikipedia)  
✅ Định dạng JSON  

### Tech Stack
- **Frontend:** Streamlit 1.40+
- **Backend:** Python 3.8+
- **AI:** Google Generative AI API
- **APIs:** OpenWeatherMap, MyMemory Translation, Wikipedia

### Chi Phí
💰 **Miễn phí hoàn toàn!**
- Python: Miễn phí
- Streamlit: Miễn phí
- Google Gemini API: Miễn phí (500 req/phút)
- Các API khác: Miễn phí

---

## 🚀 BẮT ĐẦU NHANH

### Điều Kiện Tiên Quyết
- Máy tính (Windows/Mac/Linux)
- Kết nối internet
- Google Account

### 3 Bước Chạy (15 phút)

**Bước 1: Cài Python**
```bash
# Tải từ python.org
# Cài đặt với ☑️ "Add Python to PATH"
# Kiểm tra
python --version
```

**Bước 2: Cài Thư Viện**
```bash
pip install -r requirements.txt
```

**Bước 3: Chạy**
```bash
streamlit run app.py
```

---

## 📁 CẤU TRÚC DỰ ÁN

```
📁 trợ-lý-ai/
│
├── 🎯 BẮTĐẦU
│   └── START_HERE.md ← ĐỌCTỪĐÂY
│
├── 📖 HƯỚNG DẪN
│   ├── QUICKSTART.md (5 phút)
│   ├── README.md (Chi tiết)
│   ├── INSTALLATION_GUIDE.md (Cài đặt)
│   ├── EXAMPLES.md (Ví dụ)
│   ├── TEACHER_GUIDE.md (Dạy học)
│   ├── DEPLOYMENT.md (Deploy)
│   ├── PROJECT_SUMMARY.md (Tóm tắt)
│   ├── INDEX.md (Chỉ mục)
│   └── COMPLETE_GUIDE.md (Hướng dẫn này)
│
├── 💻 CODE
│   ├── app.py (Ứng dụng chính - 300 dòng)
│   ├── tools.py (Công cụ - 400 dòng)
│   └── test_tools.py (Test - 150 dòng)
│
├── ⚙️ SETUP
│   ├── requirements.txt (Thư viện)
│   ├── .env.example (Mẫu API key)
│   ├── .gitignore (Git ignore)
│   ├── Makefile (Lệnh tiện)
│   └── .streamlit/config.toml (Cấu hình)
│
└── 📚 KHÁC
    └── (venv/) Virtual Environment
```

---

## 🔑 FILE QUAN TRỌNG

### Để Chạy
1. **requirements.txt**
   ```bash
   pip install -r requirements.txt
   ```
   - Cài tất cả thư viện cần thiết

2. **app.py**
   ```bash
   streamlit run app.py
   ```
   - Giao diện Streamlit chính

3. **.env hoặc .env.example**
   - Lưu API Key của Google
   - Quan trọng cho bảo mật!

### Để Hiểu
1. **README.md** - Bắt đầu từ đây
2. **app.py** - Code giao diện
3. **tools.py** - Code công cụ
4. **TEACHER_GUIDE.md** - Giải thích chi tiết

### Để Deploy
1. **DEPLOYMENT.md** - Hướng dẫn
2. **requirements.txt** - Cần đúng
3. **.gitignore** - Bảo vệ API key

---

## 🧠 CÁCH HOẠT ĐỘNG

### Flow Tổng Quát
```
Người Dùng
    ↓
[Gõ câu hỏi]
    ↓
Streamlit (Giao Diện)
    ↓
[Gửi tới Google Gemini API]
    ↓
AI (Google Gemini)
    ↓
[Phân tích: Cần công cụ nào?]
    ↓
Function Calling
    ↓
[Gọi hàm Python]
    ↓
Công Cụ (tools.py)
    ↓
[Lấy dữ liệu]
    ↓
AI (Tạo phản hồi)
    ↓
Streamlit (Hiển thị)
    ↓
Người Dùng [Nhận kết quả]
```

### Ví Dụ Chi Tiết
```
User: "Thời tiết ở Hà Nội?"
    ↓
Streamlit nhận → gửi tới Gemini
    ↓
Gemini: "Cần dùng tools.get_weather('Hanoi')"
    ↓
Python gọi get_weather()
    ↓
API thời tiết trả về: {"temp": "32°C", "desc": "Sunny", ...}
    ↓
Gemini: "Hà Nội hôm nay nắng 32°C"
    ↓
Streamlit hiển thị câu trả lời
```

---

## 🔧 6 CÔNG CỤ CHÍNH

### 1️⃣ Máy Tính (Calculator)
```python
# Gọi
tools.calculator("2 + 2 * 3")

# Kết quả
{"expression": "2 + 2 * 3", "result": 8, "status": "success"}

# Dùng cho
- Tính biểu thức
- Hỗ trợ +, -, *, /, %, (), sqrt, sin, cos, ...
```

### 2️⃣ Thời Tiết (Weather)
```python
# Gọi
tools.get_weather("Hanoi")

# Kết quả
{
  "city": "Hanoi",
  "temperature": "32°C",
  "description": "Sunny",
  "humidity": "60%",
  "wind_speed": "12 km/h"
}

# Dùng cho
- Dự báo thời tiết
- API miễn phí: wttr.in
```

### 3️⃣ Dịch Văn (Translator)
```python
# Gọi
tools.translate_text("Hello", "Vietnamese")

# Kết quả
{
  "original": "Hello",
  "translated": "Xin chào",
  "target_language": "Vietnamese",
  "status": "success"
}

# Dùng cho
- Dịch sang 8 ngôn ngữ
- API miễn phí: MyMemory
```

### 4️⃣ Thời Gian (Time)
```python
# Gọi
tools.get_current_time()

# Kết quả
{
  "time": "14:30:45",
  "date": "18/07/2026",
  "day_of_week": "Thursday",
  "status": "success"
}

# Dùng cho
- Lấy giờ hiện tại
- Không cần API (dùng device)
```

### 5️⃣ Tìm Kiếm (Search)
```python
# Gọi
tools.search_information("Albert Einstein")

# Kết quả
{
  "query": "Albert Einstein",
  "results": [
    {"title": "Albert Einstein", "snippet": "..."},
    ...
  ]
}

# Dùng cho
- Tìm kiếm Wikipedia
- API miễn phí
```

### 6️⃣ JSON (Formatter)
```python
# Gọi
tools.format_as_json('{"name":"John","age":30}')

# Kết quả
{
  "formatted": "{\n  \"name\": \"John\",\n  \"age\": 30\n}",
  "status": "success"
}

# Dùng cho
- Định dạng JSON
- Kiểm tra JSON hợp lệ
```

---

## 🎯 CÁC CÔNG CỤ HOẠT ĐỘNG NHƯ THẾ NÀO

### Function Calling
AI không "biết" thực hiện tính toán hay lấy thời tiết. Nó chỉ:
1. **Nhận diện**: "Người dùng cần thời tiết"
2. **Quyết định**: "Dùng công cụ get_weather"
3. **Gọi hàm**: `get_weather("Hanoi")`
4. **Nhận dữ liệu**: `{"temp": "32°C", ...}`
5. **Trả lời**: "Hà Nội 32°C, nắng"

### Vì Sao Cần?
- ✅ Dữ liệu luôn cập nhật (thời tiết thực tế)
- ✅ Kết quả chính xác hơn
- ✅ Mở rộng được (thêm công cụ dễ dàng)

---

## 📝 CODE CHÍNH (app.py)

### Cấu Trúc
```python
# 1. Import thư viện
import streamlit as st
import google.generativeai as genai

# 2. Cấu hình trang
st.set_page_config(...)

# 3. Session state (lưu chat history)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Sidebar (cấu hình)
with st.sidebar:
    api_key = st.text_input("API Key")

# 5. Main chat interface
user_input = st.chat_input("Nhập câu hỏi...")
if user_input:
    # Gửi tới AI
    response = process_message(user_input)
    # Hiển thị
    st.write(response)
```

### Hàm Chính
```python
def process_message(user_input):
    """Xử lý tin nhắn từ người dùng"""
    # 1. Gửi tới Gemini
    response = model.generate_content(user_input)
    
    # 2. Nếu AI gọi công cụ
    if response.function_call:
        tool_result = execute_tool(...)
        # Gửi lại AI kết quả
    
    # 3. AI trả lời
    return assistant_message
```

---

## 🧪 TEST & DEBUG

### Test Công Cụ
```bash
python test_tools.py
```

Output:
```
================================================== 
🧮 TEST: MÁY TÍNH
==================================================
Biểu thức: 2 + 2
Kết quả: {'expression': '2 + 2', 'result': 4, 'status': 'success'}
...
```

### Debug Errors
```python
# Trong app.py, thêm:
import logging
logging.basicConfig(level=logging.DEBUG)

# Rồi xem logs
streamlit run app.py --logger.level=debug
```

---

## 🔑 SETUP API KEY (Quan Trọng!)

### Lấy API Key
1. Truy cập: https://aistudio.google.com/apikey
2. Đăng nhập Gmail
3. Click "Create API Key in new project"
4. Sao chép key

### Cấu Hình Cách 1: File .env (Nên)
```bash
# 1. Tạo file .env (từ .env.example)
GOOGLE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

# 2. app.py sẽ đọc tự động
```

### Cấu Hình Cách 2: Nhập Trong App
```
Mở app → Sidebar → Nhập API key
```

### ⚠️ Bảo Mật
- ❌ Không để API key trong code
- ❌ Không push .env lên GitHub
- ✅ Dùng .gitignore
- ✅ Dùng environment variables

---

## 🎨 TÙYCHỈNH

### Thay Đổi Tiêu Đề
**File:** `app.py` (dòng ~70)
```python
# Tìm
st.markdown('<h1>🤖 Trợ Lý AI Đa Năng</h1>')

# Thay thành
st.markdown('<h1>🚀 AI Của [Tên]</h1>')
```

### Thay Đổi Màu Sắc
**File:** `.streamlit/config.toml`
```toml
primaryColor = "#FF5733"  # Thay màu
backgroundColor = "#FFFFFF"
```

### Thêm Công Cụ Mới
**File:** `tools.py`
```python
@staticmethod
def my_new_tool(input_param: str) -> dict:
    """Mô tả công cụ"""
    # Code xử lý
    return {"result": "..."}

# Thêm vào TOOLS_DEFINITIONS
{
    "name": "my_new_tool",
    "description": "...",
    "input_schema": { ... }
}
```

Rồi trong `app.py`, công cụ sẽ tự hoạt động! ✨

---

## 🚀 DEPLOY (Chia Sẻ Online)

### Yêu Cầu
- GitHub Account (miễn phí)
- Streamlit Cloud Account (miễn phí)

### Các Bước
1. **Push GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy Streamlit Cloud**
   - Vào: https://share.streamlit.io
   - Click "New app"
   - Chọn repo + main file (app.py)
   - Deploy!

3. **Cấu Hình Secret**
   - Settings → Secrets
   - Thêm: `GOOGLE_API_KEY = "..."`

4. **Share Link**
   - Link: `https://yourname-ai-app-xxxxx.streamlit.app`
   - Chia sẻ với bạn bè!

---

## 🎓 KHÁI NIỆM QUAN TRỌNG

### AI Không Thực Sự "Thông Minh"
- AI dự đoán từ dữ liệu
- Nó không "suy nghĩ" như người
- Nó là mô hình toán học phức tạp

### Large Language Model (LLM)
- Được huấn luyện trên miliardi dữ liệu văn bản
- Dự đoán từ tiếp theo (next token prediction)
- Lặp lại process để tạo phản hồi

### Function Calling (API Calling)
- AI nhận diện khi nào cần dùng tool
- AI gọi hàm Python
- Nhận kết quả, trả lời dựa trên đó
- Cách AI "có hành động"

### API (Application Programming Interface)
- Cầu nối giữa các ứng dụng
- Ví dụ: App yêu cầu thời tiết → API → Trả dữ liệu
- Tất cả ứng dụng hiện đại đều dùng API

---

## 🐛 KHẮC PHỤC SỰ CỐ

| Lỗi | Nguyên Nhân | Giải Pháp |
|-----|-----------|----------|
| "Python not found" | Python không cài | Cài Python, tích "Add to PATH" |
| "ModuleNotFoundError" | Thiếu thư viện | `pip install -r requirements.txt` |
| "API key invalid" | Key sai | Lấy key mới từ aistudio.google.com |
| "Port 8501 in use" | Port bận | `streamlit run app.py --server.port 8502` |
| "Connection refused" | Internet yếu | Kiểm tra internet, thử VPN |
| "Timeout" | API chậm | Chờ 30 giây, thử lại |

---

## 📚 TỆPNÊN ĐỌC THEO THỨ TỰ

### Cho Người Mới
1. `START_HERE.md` ← Bạn đang đọc
2. `QUICKSTART.md` ← Chạy ngay
3. `README.md` ← Hiểu rõ
4. `EXAMPLES.md` ← Ý tưởng

### Cho Giáo Viên
1. `TEACHER_GUIDE.md` ← Dạy học sinh
2. `INSTALLATION_GUIDE.md` ← Hỗ trợ cài
3. `PROJECT_SUMMARY.md` ← Tóm tắt
4. Xem `app.py` & `tools.py`

### Cho Lập Trình Viên
1. `README.md` ← Hiểu tổng
2. `app.py` & `tools.py` ← Xem code
3. `DEPLOYMENT.md` ← Deploy
4. `TEACHER_GUIDE.md` ← Mở rộng

---

## ✅ DANH SÁCH KIỂM TRA

### Trước Khi Chạy
- [ ] Python cài được
- [ ] API key lấy được
- [ ] Thư viện cài được
- [ ] File đủ

### Sau Khi Chạy
- [ ] App mở ở localhost:8501
- [ ] Nhập API key thành công
- [ ] AI trả lời câu hỏi
- [ ] Công cụ hoạt động

### Trước Khi Deploy
- [ ] Code không lỗi
- [ ] requirements.txt đúng
- [ ] .gitignore có .env
- [ ] .env không push

### Sau Khi Deploy
- [ ] App online
- [ ] Link chia sẻ được
- [ ] Bạn bè dùng được
- [ ] API key bảo mật

---

## 🎉 HOÀN THÀNH!

Nếu bạn:
✅ Cài được Python  
✅ Lấy được API key  
✅ Chạy được app  
✅ AI trả lời được câu hỏi  

**Chúc mừng! Bạn đã hoàn thành dự án! 🎊**

---

## 🚀 BƯỚC TIẾP THEO

### Nâng Cao
- [ ] Thêm công cụ mới
- [ ] Lưu chat history vào database
- [ ] Thêm user authentication
- [ ] Tối ưu UI/UX
- [ ] Deploy lên sản xuất

### Học Thêm
- Python advanced
- Web development (Django, FastAPI)
- Database (SQL, NoSQL)
- DevOps & CI/CD
- Cloud platforms (AWS, GCP)

---

## 📞 LIÊN HỆ

Cần giúp?
1. Kiểm tra file hướng dẫn
2. Google lỗi + "Streamlit"
3. Stack Overflow
4. Hỏi bạn/thầy cô

---

**Chúc bạn thành công! 🚀**

*Tạo bởi: Kiro AI Assistant*  
*Phiên bản: 1.0.0*  
*Cập nhật: July 18, 2026*

**[→ Bắt đầu: QUICKSTART.md](QUICKSTART.md)**

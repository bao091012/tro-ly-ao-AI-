# 🎯 BẮT ĐẦU TỪ ĐÂY

Chào bạn! 👋 Đây là dự án **Trợ Lý AI Đa Năng**.

Tài liệu này sẽ hướng dẫn bạn từng bước.

---

## ❓ Bạn Là Ai?

### 👤 "Tôi là học sinh, lần đầu"
→ Đọc: [`QUICKSTART.md`](QUICKSTART.md) (5 phút)

### 👨‍💼 "Tôi là giáo viên, cần hướng dẫn"
→ Đọc: [`TEACHER_GUIDE.md`](TEACHER_GUIDE.md) (20 phút)

### 💻 "Tôi là lập trình viên, muốn mở rộng"
→ Đọc: [`README.md`](README.md) rồi xem [`DEPLOYMENT.md`](DEPLOYMENT.md)

### 🤷 "Tôi không biết"
→ Tiếp tục đọc dưới đây!

---

## 📚 Dự Án Này Là Gì?

**Trợ Lý AI** là một ứng dụng web:

```
Bạn:   "Hôm nay thời tiết thế nào?"
           ↓
Ứng Dụng: (Gọi AI)
           ↓
AI:    "Dùng công cụ: get_weather('Hanoi')"
           ↓
       "Kết quả: 32°C, nắng"
           ↓
Bạn:   Thấy trả lời trên màn hình
```

**Bạn sẽ học:**
- ✅ Python (lập trình)
- ✅ Streamlit (tạo giao diện web)
- ✅ AI & Function Calling (AI thông minh)
- ✅ API (giao tiếp giữa ứng dụng)

**Chi phí:** Hoàn toàn miễn phí! 🎉

---

## 🚀 Bắt Đầu (3 Bước)

### ✅ Bước 1: Chuẩn Bị (5 phút)

**Cần:**
- Máy tính (Windows/Mac/Linux)
- Internet
- Google Account

**Hành động:**
1. Lấy Google API Key từ: https://aistudio.google.com/apikey
   - Click nút xanh
   - Sao chép key
   - Lưu vào nơi an toàn

2. Cài Python từ: https://python.org
   - Tải phiên bản mới nhất
   - **Quan trọng:** Tích ☑️ "Add Python to PATH"

### ✅ Bước 2: Cài Đặt (10 phút)

Mở Terminal/PowerShell và chạy:

```bash
# 1. Copy tất cả file vào 1 folder

# 2. Mở folder đó

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Tạo file .env
# - Copy .env.example thành .env
# - Mở .env
# - Thay "your_api_key_here" bằng key từ bước 1
```

### ✅ Bước 3: Chạy (2 phút)

```bash
streamlit run app.py
```

✨ Xong! Ứng dụng sẽ mở ở `localhost:8501`

---

## 🎮 Test Ứng Dụng

Hãy hỏi AI:
- "2 + 2 bằng mấy?"
- "Thời tiết ở Hà Nội?"
- "Dịch 'Hello' sang Việt"
- "Albert Einstein là ai?"

AI sẽ sử dụng công cụ tương ứng! 🤖

---

## 📖 Tài Liệu Tiếp Theo

### Nếu Muốn Hiểu Rõ
→ Đọc: [`README.md`](README.md)

### Nếu Muốn Chi Tiết Cài Đặt
→ Đọc: [`INSTALLATION_GUIDE.md`](INSTALLATION_GUIDE.md)

### Nếu Muốn Ý Tưởng Câu Hỏi
→ Đọc: [`EXAMPLES.md`](EXAMPLES.md)

### Nếu Muốn Dạy Học
→ Đọc: [`TEACHER_GUIDE.md`](TEACHER_GUIDE.md)

### Nếu Muốn Chia Sẻ Online
→ Đọc: [`DEPLOYMENT.md`](DEPLOYMENT.md)

### Nếu Muốn Xem Tất Cả File
→ Đọc: [`INDEX.md`](INDEX.md)

---

## ⚠️ Gặp Vấn Đề?

### Lỗi: "Python not found"
```
Giải pháp: Cài lại Python, tích "Add to PATH"
Đọc: INSTALLATION_GUIDE.md
```

### Lỗi: "API key không hoạt động"
```
Giải pháp: Lấy key mới, kiểm tra .env
Đọc: README.md - phần Khắc Phục Sự Cố
```

### Lỗi: "Streamlit not found"
```
Giải pháp: pip install streamlit
```

### Lỗi Khác
```
Đọc: INSTALLATION_GUIDE.md - phần Khắc Phục Sự Cố
```

---

## 💡 Mẹo Hữu Ích

✅ **Dùng Virtual Environment**
- Giúp tách thư viện riêng
- Tránh xung đột
- Cách tạo: `python -m venv venv`

✅ **Lưu API Key An Toàn**
- Đừng để trong code
- Dùng file `.env`
- Dùng `.gitignore` để bảo vệ

✅ **Hiểu Code Trước Khi Chạy**
- Đọc hướng dẫn
- Hiểu flow
- Mới chạy

✅ **Test Công Cụ Trước**
- Chạy: `python test_tools.py`
- Kiểm tra từng công cụ
- Rồi chạy app

---

## 🎓 Bài Học Quan Trọng

### 1. AI Không Phải "Thần Kỳ"
- AI dự đoán dựa trên dữ liệu
- Nó không thực sự "suy nghĩ"
- Nó là mô hình toán học

### 2. Function Calling Là Mạnh Mẽ
- AI có thể gọi hàm Python
- Lấy dữ liệu thực tế
- Trả lời chính xác hơn

### 3. API Kết Nối Mọi Thứ
- Google Gemini API → AI
- Weather API → Thời tiết
- Wikipedia API → Tìm kiếm
- Tất cả nói chuyện qua API

---

## 🎯 Mục Tiêu Cuối Cùng

Sau dự án này, bạn sẽ:

✅ Hiểu cách AI hoạt động

✅ Biết lập trình với Python

✅ Tạo được web app với Streamlit

✅ Sử dụng được API

✅ Có portfolio thực tế

✅ Có thể dạy bạn khác

---

## 🚀 Lộ Trình Học

```
Ngày 1: Cài + Chạy + Test
   ↓
Ngày 2: Hiểu code + Sửa giao diện
   ↓
Ngày 3: Thêm công cụ mới
   ↓
Ngày 4: Deploy + Chia sẻ
   ↓
Ngày 5: Sáng tạo & Mở rộng
```

---

## 📋 Danh Sách File

### Để Chạy
- `app.py` - Ứng dụng chính
- `tools.py` - Công cụ
- `requirements.txt` - Thư viện

### Để Cấu Hình
- `.env.example` → đổi tên `.env`
- `.streamlit/config.toml`

### Để Hiểu
- `README.md` - Chi tiết
- `TEACHER_GUIDE.md` - Dạy học
- `EXAMPLES.md` - Ví dụ
- `INSTALLATION_GUIDE.md` - Cài đặt

### Để Deploy
- `DEPLOYMENT.md` - Hướng dẫn

---

## ❓ Câu Hỏi Thường Gặp

**Q: Tôi cần kinh nghiệm gì?**
A: Chỉ cần biết Python cơ bản. Dự án sẽ dạy thêm!

**Q: Có chi phí không?**
A: Không! Tất cả miễn phí (Python, Streamlit, Google AI, v.v.)

**Q: Có thể tùy chỉnh không?**
A: Có! Bạn có thể sửa UI, thêm công cụ, v.v.

**Q: Có thể deploy không?**
A: Có! Streamlit Cloud miễn phí, hoặc các nơi khác.

**Q: Cần bao lâu?**
A: 3-5 ngày để hoàn thành. Tuỳ tốc độ học.

---

## 🎉 Bạn Sẵn Sàng?

### Hành động ngay:

**Bước 1:**
```
👉 Tải Python từ python.org
👉 Cài đặt (tích "Add to PATH")
```

**Bước 2:**
```
👉 Lấy API Key từ aistudio.google.com/apikey
👉 Lưu lại
```

**Bước 3:**
```
👉 Copy tất cả file vào 1 folder
👉 Mở Terminal
👉 Chạy: pip install -r requirements.txt
```

**Bước 4:**
```
👉 Chạy: streamlit run app.py
👉 Thấy ứng dụng mở
👉 Nhập API key
👉 Chat với AI!
```

---

## 📞 Cần Giúp?

1. **Cài đặt:** Xem `INSTALLATION_GUIDE.md`
2. **Lỗi:** Tìm trong tài liệu tương ứng
3. **Chi tiết:** Xem `README.md`
4. **Dạy học:** Xem `TEACHER_GUIDE.md`
5. **Tất cả file:** Xem `INDEX.md`

---

## ✨ Thành Công!

Nếu bạn:
- ✅ Cài được Python
- ✅ Lấy được API key
- ✅ Cài được thư viện
- ✅ Chạy được ứng dụng
- ✅ AI trả lời được

**Chúc mừng! Bạn đã hoàn thành bước 1! 🎉**

---

## 🚀 Bước Tiếp Theo?

1. Hiểu code (đọc `README.md`)
2. Sửa giao diện (đơn giản)
3. Thêm công cụ (trung bình)
4. Deploy online (nâng cao)

---

**Hãy bắt đầu ngay! Thế giới AI đang chờ bạn! 🤖✨**

---

*Tạo bởi: Kiro AI Assistant*
*Cho: Học sinh, sinh viên, lập trình viên*
*Cập nhật: July 18, 2026*

**[→ Đọc QUICKSTART.md để bắt đầu](QUICKSTART.md)**

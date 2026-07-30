# ⚡ Hướng Dẫn Nhanh - Chạy Ứng Dụng trong 5 Phút

## 1️⃣ Lấy API Key (2 phút)

👉 Truy cập: **https://aistudio.google.com/apikey**

→ Click nút đó xanh "Create API Key in new project"

→ Sao chép key vào nơi an toàn

## 2️⃣ Cài Đặt Python (Nếu Chưa Có)

👉 Tải: **https://python.org** → Chọn Windows / macOS / Linux

👉 Cài đặt (nhớ tích "Add Python to PATH")

👉 Mở terminal kiểm tra:
```bash
python --version
```

## 3️⃣ Cài Đặt Ứng Dụng (2 phút)

**Bước 1:** Mở terminal / PowerShell

**Bước 2:** Copy code này vào terminal:

```bash
# Tạo folder dự án
mkdir trợ-lý-ai
cd trợ-lý-ai

# Tạo virtual environment (tuỳ chọn)
python -m venv venv

# Kích hoạt (Windows)
venv\Scripts\activate

# Kích hoạt (macOS/Linux)
source venv/bin/activate
```

**Bước 3:** Copy toàn bộ file từ dự án vào folder này

**Bước 4:** Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

## 4️⃣ Cấu Hình API Key (30 giây)

**Cách 1: Dùng file .env (Nên dùng)**
```bash
# Mở file .env bằng notepad/VS Code
# Thay "your_api_key_here" bằng key bạn lấy ở bước 1
```

**Cách 2: Nhập trong ứng dụng**
- Không cần làm gì, khi chạy ứng dụng bạn sẽ nhập trực tiếp

## 5️⃣ Chạy Ứng Dụng! 🎉

```bash
streamlit run app.py
```

→ Trình duyệt sẽ mở tự động ở `http://localhost:8501`

→ Nhập API key (nếu chưa)

→ Bắt đầu chat! 🤖

## 🧪 Test Nhanh

Hãy thử những câu này:

✅ "2 + 2 bằng mấy?" → AI dùng máy tính

✅ "Thời tiết ở Hà Nội?" → AI lấy dữ liệu thời tiết

✅ "Dịch 'Hello' sang Tiếng Việt" → AI dịch

✅ "Albert Einstein là ai?" → AI tìm kiếm

## ⚠️ Vấn Đề Thường Gặp

| Vấn Đề | Giải Pháp |
|--------|----------|
| API key không hoạt động | Copy lại key từ aistudio.google.com |
| Python không tìm thấy | Cài lại Python, nhớ tích "Add to PATH" |
| Streamlit not found | Chạy: `pip install streamlit` |
| Connection timeout | Kiểm tra internet, thử VPN |
| Module not found | Chạy: `pip install -r requirements.txt` lại |

## 🎓 Tìm Hiểu Code

1. **app.py** - Phần giao diện (Streamlit)
2. **tools.py** - Phần xử lý công cụ
3. **requirements.txt** - Danh sách thư viện cần cài

## 📱 Muốn Chia Sẻ?

### Deploy lên Streamlit Cloud (Miễn Phí)

1. Push code lên GitHub
2. Vào https://share.streamlit.io
3. Connect GitHub account
4. Deploy!

Bạn sẽ có link: `https://yourname-app-xxxxx.streamlit.app`

Chia sẻ link này với bạn bè! 🎉

## 🆘 Cần Giúp?

- 🔍 Google lỗi
- 💬 Stack Overflow
- 📚 Đọc README.md

---

**Thành công! 🚀** Bây giờ bạn có một ứng dụng AI chuyên nghiệp!

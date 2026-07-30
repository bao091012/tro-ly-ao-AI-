# 🛠️ Hướng Dẫn Cài Đặt Chi Tiết

Hướng dẫn cài đặt dự án "Trợ Lý AI" từ A đến Z.

## 📋 Yêu Cầu Trước Tiên

### Kiểm Tra Hệ Điều Hành
- **Windows:** Windows 7+ (khuyên dùng Windows 10+)
- **macOS:** macOS 10.12+ (khuyên dùng macOS 10.14+)
- **Linux:** Ubuntu 18.04+ hoặc tương đương

### Kết Nối Internet
- Cần để tải thư viện
- Cần để sử dụng API

---

## 🔧 BƯỚC 1: Cài Python

### Windows

1. Truy cập: https://python.org
2. Click "Downloads" → "Windows"
3. Chọn "Python 3.11" (hoặc mới nhất)
4. Download file `.exe`
5. Chạy file → **QUAN TRỌNG:** Tích ☑️ "Add Python to PATH"
6. Bấm "Install Now"
7. Chờ cài đặt (~2-3 phút)

**Kiểm Tra:**
```powershell
python --version
python -m pip --version
```

Nếu thấy version → Thành công! ✅

### macOS

```bash
# Nếu có Homebrew:
brew install python3

# Không có Homebrew:
# Download từ https://python.org (macOS installer)
```

**Kiểm Tra:**
```bash
python3 --version
python3 -m pip --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Kiểm Tra:**
```bash
python3 --version
pip3 --version
```

---

## 📁 BƯỚC 2: Tạo Folder Dự Án

### Windows (PowerShell)
```powershell
# Tạo folder
mkdir $HOME\Desktop\trợ-lý-ai
cd $HOME\Desktop\trợ-lý-ai
```

### macOS / Linux
```bash
mkdir ~/ai-assistant
cd ~/ai-assistant
```

---

## 🔒 BƯỚC 3: Tạo Virtual Environment (Tuỳ Chọn Nhưng Nên)

### Windows
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Nếu lỗi "cannot be loaded", chạy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

**Kiểm Tra:** Dòng lệnh sẽ có `(venv)` phía trước

---

## 📦 BƯỚC 4: Copy Files Dự Án

Sao chép **tất cả file** từ dự án vào folder `trợ-lý-ai`:

- ✅ `app.py`
- ✅ `tools.py`
- ✅ `requirements.txt`
- ✅ `.env.example`
- ✅ `.gitignore`
- ✅ Tất cả `.md` file
- ✅ `test_tools.py`
- ✅ Folder `.streamlit/`

---

## 📚 BƯỚC 5: Cài Đặt Thư Viện

### Cập Nhật pip (Tùy Chọn)
```bash
python -m pip install --upgrade pip
```

### Cài Requirements
```bash
pip install -r requirements.txt
```

**Chờ ~2-3 phút** cài đặt tất cả thư viện.

**Kiểm Tra:**
```bash
pip list
```

Nên thấy:
- streamlit
- google-generativeai
- python-dotenv
- requests

---

## 🔑 BƯỚC 6: Lấy Google API Key

### 6.1 Tạo API Key

1. Truy cập: https://aistudio.google.com/apikey
2. Nếu yêu cầu đăng nhập → Dùng tài khoản Google
3. Click nút xanh: **"Create API Key in new project"**
4. Sao chép key vào nơi an toàn (Notepad)

### 6.2 Cấu Hình

**Cách A: Dùng File .env (An Toàn & Khuyên Dùng)**

1. Mở file `.env.example`
2. Thay `your_api_key_here` bằng key thực tế
3. Đổi tên file thành `.env` (xóa phần `_example`)

```env
GOOGLE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

4. **Lưu file**

**Cách B: Nhập Trực Tiếp Trong App**

- Bỏ qua bước này
- Khi chạy app, nhập key vào sidebar

---

## 🚀 BƯỚC 7: Chạy Ứng Dụng

```bash
streamlit run app.py
```

**Kỳ Vọng:**
- Terminal hiển thị: `You can now view your Streamlit app...`
- Trình duyệt mở: `localhost:8501`
- Thấy giao diện app

**Nếu trình duyệt không mở:**
- Manual mở: http://localhost:8501

---

## ✅ KIỂM TRA HỆ THỐNG

Để chắc chắn mọi thứ hoạt động:

```bash
# Test Python
python --version

# Test pip
pip --version

# Test thư viện
python -c "import streamlit; import google.generativeai"

# Test công cụ
python test_tools.py
```

Tất cả nên thành công! ✅

---

## 🧪 BƯỚC 8: Test Ứng Dụng

1. Ứng dụng đã mở ở `localhost:8501`
2. Trong sidebar, nhập Google API Key (nếu chưa dùng .env)
3. Trong chat, gõ: `"2 + 2 bằng mấy?"`
4. Nên thấy AI trả lời: `"4"`

---

## 🐛 KHẮC PHỤC SỰ CỐ

### Lỗi: "Python not found"
```
❌ Nguyên nhân: Python không cài hoặc PATH sai
✅ Giải pháp:
   1. Cài lại Python
   2. ☑️ Tích "Add Python to PATH"
   3. Khởi động lại máy
   4. Thử lại
```

### Lỗi: "pip: command not found"
```
❌ Nguyên nhân: pip không được cài
✅ Giải pháp:
   python -m pip install --upgrade pip
```

### Lỗi: "venv không activate"
```
❌ Nguyên nhân: PowerShell execution policy
✅ Giải pháp (Windows):
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .\venv\Scripts\Activate.ps1
```

### Lỗi: "Module not found"
```
❌ Nguyên nhân: Thư viện chưa cài
✅ Giải pháp:
   pip install -r requirements.txt
```

### Lỗi: "API key not valid"
```
❌ Nguyên nhân: API key sai hoặc hết hạn
✅ Giải pháp:
   1. Lấy key mới từ https://aistudio.google.com/apikey
   2. Cập nhật .env hoặc nhập trong app
```

### Lỗi: "Port 8501 already in use"
```
❌ Nguyên nhân: Streamlit khác đã dùng port này
✅ Giải pháp:
   streamlit run app.py --server.port 8502
```

---

## 🎓 HIỂU VỀ VIRTUAL ENVIRONMENT

Virtual Environment (venv) là:
- 📦 Một "chiếc hộp" để cài thư viện riêng
- ✅ Không ảnh hưởng đến Python chính
- ✅ Dễ xóa/reset
- ✅ Tối ưu cho dự án

**Tại sao cần?**
- Dự án A cần `streamlit 1.40`
- Dự án B cần `streamlit 1.35`
- venv giải quyết xung đột!

---

## 🔄 KÍCH HOẠT/VÔ HIỆU HÓA VENV

**Kích Hoạt:**
```powershell
# Windows
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

**Vô Hiệu Hóa:**
```bash
deactivate
```

---

## 🧹 DỌN DẸP / RESET

### Xóa Virtual Environment
```bash
# Windows
rmdir /s /q venv

# macOS/Linux
rm -rf venv
```

Sau đó tạo lại:
```bash
python -m venv venv
```

### Xóa Thư Viện Cache
```bash
pip cache purge
```

---

## 📊 TỔNG HỢP LỆNH (Copy-Paste)

### Windows PowerShell
```powershell
# 1. Tạo folder
mkdir $HOME\Desktop\ai-app
cd $HOME\Desktop\ai-app

# 2. Tạo venv
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Chạy
streamlit run app.py
```

### macOS / Linux Bash
```bash
# 1. Tạo folder
mkdir ~/ai-app
cd ~/ai-app

# 2. Tạo venv
python3 -m venv venv
source venv/bin/activate

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Chạy
streamlit run app.py
```

---

## 🆘 CẦN GHI MÁY

Lưu danh sách này:

- **API Key:** [_______________________]
- **Python Version:** [_______________________]
- **Project Folder:** [_______________________]
- **Port:** 8501

---

## ✨ HOÀN TẤT!

Nếu cả các bước trên đều thành công:

✅ Python cài được
✅ Virtual environment hoạt động
✅ Thư viện cài được
✅ API key lấy được
✅ Ứng dụng chạy được

**Chúc mừng! Bạn sẵn sàng học AI! 🚀**

---

## 📞 CẦN GIÚP?

1. Đọc lại bước gặp lỗi
2. Google: `[Lỗi] + Python`
3. Stack Overflow: https://stackoverflow.com
4. Hỏi bạn hoặc thầy cô

---

**Chúc bạn cài đặt thành công! 💪**

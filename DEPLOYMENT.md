# 🚀 Hướng Dẫn Deploy - Chia Sẻ Ứng Dụng Với Bạn Bè

Hướng dẫn này giúp bạn deploy ứng dụng lên internet để bạn bè dùng được!

## 📋 Yêu Cầu

- ✅ Tài khoản GitHub (miễn phí)
- ✅ Tài khoản Streamlit Cloud (miễn phí)
- ✅ Google API Key

## 🎯 Các Bước

### Bước 1: Chuẩn Bị Dự Án (5 phút)

**1.1. Cập nhật `requirements.txt`**
```bash
pip freeze > requirements.txt
```

**1.2. Tạo file `streamlit.app`** (tuỳ chọn - để Streamlit Cloud tự detect)
```bash
# Không cần tạo, Streamlit Cloud tự detect app.py
```

**1.3. Kiểm tra code không có lỗi**
```bash
streamlit run app.py
```

---

### Bước 2: Đẩy Code Lên GitHub (10 phút)

**2.1. Tạo Repository GitHub**
- Truy cập: https://github.com/new
- Tên repo: `ai-assistant-app` (hoặc tên khác)
- Chọn "Public"
- Click "Create repository"

**2.2. Khởi Tạo Git Locally**
```bash
cd trợ-lý-ai
git init
git add .
git commit -m "Initial commit: AI Assistant with Streamlit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-assistant-app.git
git push -u origin main
```

**2.3. Kiểm Tra GitHub**
- Truy cập repo trên github.com
- Xem thấy file chưa?

---

### Bước 3: Deploy Lên Streamlit Cloud (5 phút)

**3.1. Đăng Nhập/Đăng Ký Streamlit Cloud**
- Truy cập: https://share.streamlit.io
- Click "Sign up"
- Chọn "Sign up with GitHub"
- Cấp quyền cho Streamlit

**3.2. Deploy New App**
- Click "New app"
- Chọn repo: `ai-assistant-app`
- Branch: `main`
- Main file path: `app.py`
- Click "Deploy"

**3.3. Chờ Deploy**
- Streamlit sẽ:
  1. Clone repo
  2. Cài `requirements.txt`
  3. Chạy `app.py`
- Mất ~2-3 phút

---

### Bước 4: Cấu Hình Secret (API Key) (5 phút)

⚠️ **QUAN TRỌNG:** Không nên để API key trong code!

**4.1. Streamlit Secrets**
- Truy cập: Settings → Secrets
- Thêm:
```toml
GOOGLE_API_KEY = "your_actual_key_here"
```

**4.2. Update `app.py` để đọc từ secrets**
Thay dòng này:
```python
st.session_state.api_key = os.getenv("GOOGLE_API_KEY", "")
```

Thành:
```python
try:
    st.session_state.api_key = st.secrets.get("GOOGLE_API_KEY", "")
except:
    st.session_state.api_key = os.getenv("GOOGLE_API_KEY", "")
```

**4.3. Push thay đổi lên GitHub**
```bash
git add app.py
git commit -m "Update to use Streamlit secrets"
git push
```

---

### Bước 5: Thử Nghiệm! (1 phút)

- Streamlit Cloud sẽ auto-redeploy sau khi push
- Truy cập link của bạn: `https://yourname-ai-assistant-app-xxxxx.streamlit.app`
- Test: Hỏi AI vài câu!

---

## ✅ Danh Sách Kiểm Tra

- [ ] Code chạy được trên máy tính
- [ ] Tất cả file đã thêm vào `.gitignore` (API key, venv)
- [ ] `requirements.txt` đã cập nhật
- [ ] GitHub repo đã tạo
- [ ] Code đã push lên GitHub
- [ ] Streamlit Cloud account đã tạo
- [ ] App đã deploy
- [ ] Secrets đã cấu hình
- [ ] Test app hoạt động
- [ ] Link đã chia sẻ với bạn bè

---

## 🎉 Xong! Giờ Bạn Có Thể:

✅ Chia sẻ link: "Hãy dùng trợ lý AI của tôi!"

✅ Bạn bè không cần cài gì, chỉ cần click link

✅ Mỗi lần update code, Streamlit tự deploy lại

---

## 🔄 Update App Sau Này

**Khi bạn thêm tính năng mới:**

```bash
# 1. Test trên máy
streamlit run app.py

# 2. Cập nhật requirements.txt (nếu cài thư viện mới)
pip freeze > requirements.txt

# 3. Push lên GitHub
git add .
git commit -m "Add new feature: [mô tả]"
git push

# 4. Streamlit Cloud tự động deploy! ✨
```

---

## 🚨 Khắc Phục Sự Cố

### App không load
```
✓ Kiểm tra GitHub repo - code đã push chưa?
✓ Kiểm tra requirements.txt - có thiếu thư viện?
✓ Xem logs: Settings → Manage app → View logs
```

### API key lỗi
```
✓ Kiểm tra secrets đã nhập đúng chưa
✓ API key còn valid không?
✓ Copy-paste lại key
```

### App chạy chậm
```
✓ API Google bị slow - chờ 1-2 phút
✓ Internet yếu - cơ bản thôi
✓ Quá nhiều request - chờ tí
```

---

## 📊 Cách Theo Dõi

Streamlit Cloud cho phép xem:
- 📈 Số lần người dùng truy cập
- 📊 CPU/Memory usage
- 📝 Logs (để debug)

Truy cập: Settings → Overview

---

## 💰 Chi Phí

| Dịch Vụ | Chi Phí |
|---------|--------|
| GitHub | Miễn phí |
| Streamlit Cloud | Miễn phí (3 app) |
| Google Gemini API | Miễn phí (500 request/phút) |
| **Tổng** | **Miễn phí** ✨ |

---

## 🎓 Bài Học

Qua quá trình deploy, bạn học được:
- ✅ Quản lý code với Git
- ✅ Quản lý secrets (API key)
- ✅ Triển khai ứng dụng
- ✅ Hợp tác với người khác (GitHub)

---

## 🆘 Cần Giúp?

1. Kiểm tra lại các bước
2. Google lỗi + "Streamlit Cloud"
3. Stack Overflow
4. Streamlit Docs: https://docs.streamlit.io/deploy

---

**Chúc bạn deploy thành công! 🚀**

---

### Mẹo Chia Sẻ

Khi chia sẻ với bạn bè:

**Làm sao?**
> "Hãy vào link này: [link] và hỏi AI tôi bất cứ điều gì!"

**Kèm ví dụ:**
> "Hỏi: 'Thời tiết ở Hà Nội?' hoặc 'Dịch Hello sang Việt'"

**Kèm ảnh:** (Screenshot hoặc GIF hoạt động)

Bạn bè sẽ ấn tượng: "Wow, bạn tự làm được cái này?!" 🤩

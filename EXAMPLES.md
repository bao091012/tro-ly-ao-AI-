# 💡 Những Ví Dụ Hay - Cách Dùng Trợ Lý AI

## 🧮 Ví Dụ Máy Tính

### Câu Hỏi Đơn Giản
```
👤 Bạn: 5 + 3 bằng mấy?
🤖 AI: Sử dụng công cụ: calculator
       Kết quả: 8
```

### Câu Hỏi Phức Tạp
```
👤 Bạn: Tính (10 + 5) * 2 - 3
🤖 AI: Sử dụng công cụ: calculator
       Kết quả: 27
```

### Câu Hỏi Với Hàm Toán
```
👤 Bạn: Căn bậc hai của 16 là bao nhiêu?
🤖 AI: Sử dụng công cụ: calculator (sqrt(16))
       Kết quả: 4.0
```

---

## 🌤️ Ví Dụ Thời Tiết

### Thành Phố Lớn
```
👤 Bạn: Thời tiết ở TP. Hồ Chí Minh hôm nay thế nào?
🤖 AI: Sử dụng công cụ: get_weather
       Nhiệt độ: 32°C
       Mô tả: Nắng
       Độ ẩm: 60%
       Vận tốc gió: 12 km/h
```

### Thành Phố Nhỏ
```
👤 Bạn: Bây giờ ở Đà Lạt trời thế nào?
🤖 AI: Sử dụng công cụ: get_weather
       Nhiệt độ: 18°C
       Mô tả: Mây
       Độ ẩm: 75%
```

### Nhiều Thành Phố
```
👤 Bạn: So sánh thời tiết Hà Nội và Hải Phòng
🤖 AI: Sẽ gọi get_weather 2 lần, rồi so sánh
```

---

## 🗣️ Ví Dụ Dịch Văn

### Dịch Tiếng Anh
```
👤 Bạn: Dịch "Good morning" sang Tiếng Việt
🤖 AI: Sử dụng công cụ: translate_text
       Kết quả: "Chào buổi sáng"
```

### Dịch Tiếng Pháp
```
👤 Bạn: "Bonjour" nghĩa là gì?
🤖 AI: Sử dụng công cụ: translate_text
       Kết quả: "Xin chào"
```

### Dịch Câu Dài
```
👤 Bạn: Dịch "I love learning programming" sang Tiếng Việt
🤖 AI: Sử dụng công cụ: translate_text
       Kết quả: "Tôi yêu học lập trình"
```

### Các Ngôn Ngữ Hỗ Trợ
- English (Anh)
- French (Pháp)
- Spanish (Tây Ban Nha)
- Chinese (Trung Quốc)
- Japanese (Nhật Bản)
- Korean (Hàn Quốc)
- German (Đức)
- Russian (Nga)

---

## ⏰ Ví Dụ Thời Gian

### Lấy Giờ Hiện Tại
```
👤 Bạn: Bây giờ mấy giờ?
🤖 AI: Sử dụng công cụ: get_current_time
       Giờ: 14:30:45
       Ngày: 18/07/2026
       Thứ: Thursday
```

### Hỏi Ngày
```
👤 Bạn: Hôm nay là thứ mấy?
🤖 AI: Sử dụng công cụ: get_current_time
       Kết quả: Thursday (Thứ Năm)
```

---

## 🔍 Ví Dụ Tìm Kiếm

### Tìm Nhân Vật Lịch Sử
```
👤 Bạn: Albert Einstein là ai?
🤖 AI: Sử dụng công cụ: search_information
       Kết quả:
       - Tiêu đề: Albert Einstein
       - Mô tả: Nhà vật lý nổi tiếng, tác giả thuyết tương đối...
```

### Tìm Địa Điểm
```
👤 Bạn: Tháp Eiffel ở đâu?
🤖 AI: Sử dụng công cụ: search_information
       Kết quả: Thông tin về tháp Eiffel ở Paris
```

### Tìm Thông Tin Khoa Học
```
👤 Bạn: Photosynthesis là gì?
🤖 AI: Sử dụng công cụ: search_information
       Kết quả: Giải thích về quá trình quang hợp
```

---

## 📋 Ví Dụ JSON

### Định Dạng JSON Đơn Giản
```
👤 Bạn: Giúp tôi định dạng: {"name":"John","age":30}
🤖 AI: Sử dụng công cụ: format_as_json
       Kết quả:
       {
         "name": "John",
         "age": 30
       }
```

### Kiểm Tra JSON Hợp Lệ
```
👤 Bạn: JSON này có đúng không: {name: "John"}
🤖 AI: Sử dụng công cụ: format_as_json
       Kết quả: JSON không hợp lệ (thiếu dấu ngoặc kép)
```

---

## 🎨 Ví Dụ Kết Hợp Nhiều Công Cụ

### Kết Hợp Tính Toán + Thời Tiết
```
👤 Bạn: Nếu nhiệt độ ở HCM là 32°C, chuyển sang Fahrenheit bao nhiêu?
🤖 AI: 
   1. Gọi: get_weather("Ho Chi Minh")
      → Lấy được 32°C
   2. Gọi: calculator("32 * 9/5 + 32")
      → Kết quả: 89.6°F
```

### Kết Hợp Dịch + Tìm Kiếm
```
👤 Bạn: Dịch tên của người phát minh ra bóng đèn sang Anh rồi tìm hiểu về ông ta
🤖 AI:
   1. Gọi: translate_text("Thomas Edison", "English")
   2. Gọi: search_information("Thomas Edison")
```

### Kết Hợp Tất Cả
```
👤 Bạn: Cho tôi biết thời gian bây giờ, thời tiết ở Hà Nội, và dịch 
        "What a beautiful day" sang Tiếng Việt
🤖 AI:
   1. get_current_time()
   2. get_weather("Hanoi")
   3. translate_text("What a beautiful day", "Vietnamese")
```

---

## 🎯 Câu Hỏi Khó Hơn - AI Sẽ Suy Luận

### Hỏi Mà Không Rõ Cần Công Cụ Nào
```
👤 Bạn: Nếu tôi muốn biết thời tiết ở Hà Nội, tôi sẽ sử dụng công cụ gì?
🤖 AI: (Không cần gọi công cụ)
   Bạn sẽ sử dụng công cụ "get_weather" và nhập thành phố là "Hanoi"
```

### Hỏi Lý Thuyết
```
👤 Bạn: AI là gì? Nó hoạt động như thế nào?
🤖 AI: (Trả lời trực tiếp, không cần công cụ)
   AI là... [giải thích chi tiết]
```

---

## 🚀 Những Thử Thách Vui

### Thử Thách 1: Tính Nhanh
```
👤 Bạn: Tính 123 * 456 - 789 + 321
🤖 AI: Sử dụng calculator
   Kết quả: 55560
👤 Bạn: Nhanh quá!
```

### Thử Thách 2: Dịch Cả Câu
```
👤 Bạn: Dịch "The quick brown fox jumps over the lazy dog" 
        sang nhiều ngôn ngữ
🤖 AI: Gọi translate_text 8 lần...
```

### Thử Thách 3: Tìm Kiếm Sâu
```
👤 Bạn: Tìm 5 người nổi tiếng và dịch tên họ sang Anh
🤖 AI: (Kết hợp search_information + translate_text)
```

---

## 📝 Mẹo Hỏi AI

✅ **Hỏi Cụ Thể:**
- ✓ "Thời tiết ở Hà Nội?"
- ✗ "Thời tiết ở đâu đó?"

✅ **Đưa Ví Dụ:**
- ✓ "Dịch 'Hello' sang Tiếng Việt"
- ✗ "Dịch cái gì đó?"

✅ **Nói Rõ Mục Đích:**
- ✓ "Tôi cần tính 2+2 để kiểm tra"
- ✗ "Tính 2+2"

✅ **Dùng Ngôn Ngữ Tự Nhiên:**
- ✓ "Hôm nay là thứ mấy?"
- ✗ "Day?"

---

## 🎓 Bài Học

**Qua những ví dụ trên, bạn học được:**

1. ✅ AI có thể giải quyết nhiều vấn đề khác nhau
2. ✅ AI biết khi nào cần dùng công cụ
3. ✅ Kết hợp nhiều công cụ → Giải pháp mạnh hơn
4. ✅ Cách hỏi AI quyết định kết quả

---

Hãy thử tất cả những ví dụ này! 🚀

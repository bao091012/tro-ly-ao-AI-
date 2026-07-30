"""
🤖 TRỢ LÝ AI ĐA NĂNG - Ứng Dụng Streamlit
Với ô nhập API Key (Google + OpenWeather)
"""

import streamlit as st
import os
from tools import AITools
import json

# Cấu hình trang
st.set_page_config(
    page_title="🤖 Trợ Lý AI Đa Năng",
    page_icon="🤖",
    layout="wide"
)

# CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🤖 Trợ Lý AI Đa Năng</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Cấu Hình API")
    
    # Ô nhập Google API Key
    api_key = st.text_input(
        "🔑 Google API Key (Tuỳ Chọn)",
        type="password",
        placeholder="Dán API key của bạn tại đây",
        help="Lấy từ: https://aistudio.google.com/apikey"
    )
    
    if api_key:
        st.success("✅ Google API Key đã nhập!")
    
    st.divider()
    
    # Ô nhập OpenWeather API Key
    openweather_key = st.text_input(
        "🌤️ OpenWeather API Key",
        type="password",
        placeholder="Dán OpenWeather API key tại đây",
        help="Lấy từ: https://openweathermap.org/api"
    )
    
    if openweather_key:
        st.success("✅ OpenWeather API Key đã nhập!")
    else:
        st.info("💡 Nhập OpenWeather API Key để dùng Thời Tiết")
    
    st.divider()
    
    st.header("� Công Cụ Có Sẵn")
    st.markdown("""
    ✅ **Máy Tính** - Tính toán
    
    ✅ **Thời Tiết** - Dự báo thời tiết
    
    ✅ **Dịch Văn** - Dịch 9 ngôn ngữ
    
    ✅ **Thời Gian** - Lấy giờ hiện tại
    
    ✅ **Tìm Kiếm** - Tìm Wikipedia
    
    ✅ **JSON** - Định dạng JSON
    """)
    
    st.divider()
    st.info("💡 Chọn công cụ ở trên để sử dụng")

# Main content
st.subheader("🔧 Chọn Công Cụ")

# Tabs cho từng công cụ
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📐 Máy Tính",
    "🌤️ Thời Tiết", 
    "🗣️ Dịch Văn",
    "⏰ Thời Gian",
    "🔍 Tìm Kiếm",
    "📋 JSON"
])

# Tab 1: Máy Tính
with tab1:
    st.write("### 📐 Máy Tính Toán Học")
    st.info("💡 Gõ biểu thức rồi nhấn Enter hoặc click nút Tính")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        expression = st.text_input("Nhập biểu thức:", placeholder="Ví dụ: 2 + 2, sqrt(16), 10 * 5", key="calc_input")
    with col2:
        calc_button = st.button("🔢 Tính", key="calc_btn", use_container_width=True)
    
    if expression and (calc_button or True):
        try:
            result = AITools.calculator(expression)
            if "status" in result and result["status"] == "success":
                st.success(f"✅ Kết quả: **{result['result']}**")
                st.markdown(f"```\n{expression} = {result['result']}\n```")
            else:
                st.error(f"❌ Lỗi: {result.get('error', 'Không biết')}")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")
    
    # Ví dụ
    st.divider()
    st.write("**Ví dụ:**")
    ex_cols = st.columns(3)
    with ex_cols[0]:
        if st.button("2 + 2"):
            st.session_state.calc_input = "2 + 2"
            st.rerun()
    with ex_cols[1]:
        if st.button("sqrt(16)"):
            st.session_state.calc_input = "sqrt(16)"
            st.rerun()
    with ex_cols[2]:
        if st.button("10 * 5"):
            st.session_state.calc_input = "10 * 5"
            st.rerun()

# Tab 2: Thời Tiết
with tab2:
    st.write("### 🌤️ Dự Báo Thời Tiết (OpenWeather)")
    st.info("💡 Nhập tên thành phố để xem thời tiết hiện tại")
    
    if not openweather_key:
        st.error("❌ Chưa nhập OpenWeather API Key!")
        st.warning("Vui lòng nhập API Key ở sidebar")
    else:
        col1, col2 = st.columns([3, 1])
        with col1:
            city = st.text_input("Nhập tên thành phố:", placeholder="Ví dụ: Hanoi, Ho Chi Minh City", key="weather_input")
        with col2:
            weather_button = st.button("🔍 Tìm", key="weather_btn", use_container_width=True)
        
        if city and (weather_button or True):
            try:
                result = AITools.get_weather(city, openweather_key)
                if "status" in result and result["status"] == "success":
                    st.success(f"✅ Thời tiết ở **{result['city']}**")
                    
                    # Hiển thị thông tin thời tiết
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("🌡️ Nhiệt độ", result['temperature'])
                    with col2:
                        st.metric("💧 Độ ẩm", result['humidity'])
                    with col3:
                        st.metric("💨 Gió", result['wind_speed'])
                    with col4:
                        st.metric("☁️ Tình trạng", result['description'].capitalize())
                    
                    # Hiển thị chi tiết dưới dạng card
                    st.write("---")
                    st.write(f"**📍 Chi tiết:**")
                    st.write(f"- 🌡️ Nhiệt độ: {result['temperature']}")
                    st.write(f"- 💧 Độ ẩm không khí: {result['humidity']}")
                    st.write(f"- 💨 Tốc độ gió: {result['wind_speed']}")
                    st.write(f"- ☁️ Điều kiện: {result['description'].capitalize()}")
                else:
                    st.error(f"❌ Lỗi: {result.get('error', 'Không tìm thấy thành phố')}")
                    st.warning("💡 Hãy thử lại với tên thành phố khác")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")
        
        # Ví dụ
        st.divider()
        st.write("**🏙️ Thành phố phổ biến:**")
        ex_cols = st.columns(4)
        
        with ex_cols[0]:
            if st.button("Hà Nội", key="hanoi", use_container_width=True):
                st.session_state.weather_input = "Hanoi"
                st.rerun()
        with ex_cols[1]:
            if st.button("TP.HCM", key="hcm", use_container_width=True):
               city = st.text_input("Nhập tên thành phố:", value="Ho Chi Minh City", key="weather_input")
                st.rerun()
        with ex_cols[2]:
            if st.button("Đà Nẵng", key="danang", use_container_width=True):
                st.session_state.weather_input = "Da Nang"
                st.rerun()
        with ex_cols[3]:
            if st.button("Cần Thơ", key="cantho", use_container_width=True):
                st.session_state.weather_input = "Can Tho"
                st.rerun()

# Tab 3: Dịch Văn
with tab3:
    st.write("### 🗣️ Dịch Văn Bản")
    st.info("💡 Dịch sang các ngôn ngữ khác nhau")
    
    text_to_translate = st.text_input("Văn bản cần dịch:", placeholder="Ví dụ: Hello", key="translate_input")
    target_lang = st.selectbox("Ngôn ngữ đích:", 
        ["Tiếng Việt", "English", "French", "Spanish", "Chinese", "Japanese", "Korean", "German", "Russian"],
        key="target_lang")
    
    if text_to_translate:
        try:
            result = AITools.translate_text(text_to_translate, target_lang)
            if "status" in result and result["status"] == "success":
                st.success(f"✅ Dịch sang {target_lang}:")
                st.write(f"**'{result['original']}'** → **'{result['translated']}'**")
            else:
                st.error(f"❌ {result.get('error', 'Lỗi')}")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")

# Tab 4: Thời Gian
with tab4:
    st.write("### ⏰ Thời Gian Hiện Tại")
    if st.button("Lấy Thời Gian", type="primary", use_container_width=True):
        result = AITools.get_current_time()
        if "status" in result and result["status"] == "success":
            st.success("✅ Thời gian hiện tại:")
            col1, col2, col3 = st.columns(3)
            col1.metric("⏰ Giờ", result['time'])
            col2.metric("📅 Ngày", result['date'])
            col3.metric("📆 Thứ", result['day_of_week'])
        else:
            st.error(f"❌ {result.get('error', 'Lỗi')}")

# Tab 5: Tìm Kiếm
with tab5:
    st.write("### 🔍 Tìm Kiếm Thông Tin")
    st.info("💡 Tìm kiếm trên Wikipedia")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("Từ khóa tìm kiếm:", placeholder="Ví dụ: Albert Einstein, Python", key="search_input")
    with col2:
        search_button = st.button("🔍 Tìm", key="search_btn", use_container_width=True)
    
    if query and (search_button or True):
        try:
            result = AITools.search_information(query)
            if "status" in result and result["status"] == "success":
                st.success(f"✅ Kết quả tìm kiếm cho **'{query}'**:")
                st.write(f"Tìm thấy {len(result['results'])} kết quả:")
                
                for i, item in enumerate(result['results'], 1):
                    with st.expander(f"📄 {i}. {item['title']}", expanded=(i==1)):
                        st.write(item['snippet'])
            else:
                st.error(f"❌ {result.get('error', 'Lỗi')}")
                st.info("💡 Thử từ khóa khác")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")
    
    # Ví dụ
    st.divider()
    st.write("**Tìm kiếm nhanh:**")
    ex_cols = st.columns(3)
    with ex_cols[0]:
        if st.button("Albert Einstein", key="ae"):
            st.session_state.search_input = "Albert Einstein"
            st.rerun()
    with ex_cols[1]:
        if st.button("Python", key="python"):
            st.session_state.search_input = "Python"
            st.rerun()
    with ex_cols[2]:
        if st.button("Việt Nam", key="vietnam"):
            st.session_state.search_input = "Vietnam"
            st.rerun()

# Tab 6: JSON
with tab6:
    st.write("### 📋 Định Dạng JSON")
    st.info("💡 Kiểm tra và định dạng JSON đẹp hơn")
    
    json_input = st.text_area("Nhập JSON:", placeholder='{"name": "John", "age": 30}', height=150, key="json_input")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        format_button = st.button("✨ Định Dạng", key="json_format", use_container_width=True)
    with col2:
        clear_button = st.button("🗑️ Xóa", key="json_clear", use_container_width=True)
    with col3:
        st.write("")  # Placeholder
    
    if clear_button:
        st.session_state.json_input = ""
        st.rerun()
    
    if json_input and (format_button or True):
        try:
            result = AITools.format_as_json(json_input)
            if "status" in result and result["status"] == "success":
                st.success("✅ JSON hợp lệ!")
                st.write("**Kết quả định dạng:**")
                st.code(result['formatted'], language="json")
                
                # Copy button
                st.write("**Copy JSON:**")
                st.text_area("", value=result['formatted'], height=150, disabled=True, key="json_output")
            else:
                st.error(f"❌ JSON không hợp lệ!")
                st.error(f"Lỗi: {result.get('error', 'Không biết')}")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")
    
    # Ví dụ
    st.divider()
    st.write("**Ví dụ JSON:**")
    ex_cols = st.columns(2)
    
    with ex_cols[0]:
        if st.button('{"name":"John","age":30}', key="json_ex1"):
            st.session_state.json_input = '{"name":"John","age":30}'
            st.rerun()
    
    with ex_cols[1]:
        if st.button('{"students":["Alice","Bob","Charlie"]}', key="json_ex2"):
            st.session_state.json_input = '{"students":["Alice","Bob","Charlie"]}'
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    🤖 Trợ Lý AI Đa Năng | Phiên bản 1.0 | Powered by Streamlit
</div>
""", unsafe_allow_html=True)

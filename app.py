"""
🤖 TRỢ LÝ AI ĐA NĂNG - Ứng Dụng Streamlit
"""

import streamlit as st
from tools import AITools

# Cấu hình trang
st.set_page_config(
    page_title="🤖 Trợ Lý AI Đa Năng",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Trợ Lý AI Đa Năng")
st.markdown("---")

# Sidebar - Nhập API Keys
with st.sidebar:
    st.header("⚙️ Cấu Hình API")
    
    google_api_key = st.text_input(
        "🔑 Google API Key",
        type="password",
        placeholder="Nhập Google API Key"
    )
    
    if google_api_key:
        st.success("✅ Google API Key đã nhập")
    
    st.divider()
    
    openweather_key = st.text_input(
        "🌤️ OpenWeather API Key",
        type="password",
        placeholder="Nhập OpenWeather API Key"
    )
    
    if openweather_key:
        st.success("✅ OpenWeather API Key đã nhập")
    else:
        st.info("💡 Nhập để sử dụng công cụ Thời Tiết")

# Main content
st.subheader("🔧 Chọn Công Cụ")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📐 Máy Tính",
    "🌤️ Thời Tiết",
    "🗣️ Dịch Văn",
    "⏰ Thời Gian",
    "🔍 Tìm Kiếm",
    "📋 JSON"
])

# Khởi tạo AITools
tools = AITools(google_api_key=google_api_key, openweather_key=openweather_key)

# Tab 1: Máy Tính
with tab1:
    st.header("📐 Máy Tính")
    expr = st.text_input("Nhập phép tính (vd: 2 + 2):")
    if expr:
        try:
            result = tools.calculator(expr)
            st.success(f"✅ Kết quả: {result}")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")

# Tab 2: Thời Tiết
with tab2:
    st.header("🌤️ Thời Tiết")
    if not openweather_key:
        st.warning("⚠️ Vui lòng nhập OpenWeather API Key ở sidebar")
    else:
        city = st.text_input("Nhập tên thành phố:")
        if city:
            try:
                weather = tools.weather(city)
                st.success(f"✅ {weather}")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

# Tab 3: Dịch Văn
with tab3:
    st.header("🗣️ Dịch Văn Bản")
    languages = ["Tiếng Anh", "Tiếng Pháp", "Tiếng Tây Ban Nha", "Tiếng Đức", 
                 "Tiếng Nhật", "Tiếng Trung", "Tiếng Hàn", "Tiếng Ấn Độ", "Tiếng Bồ Đào Nha"]
    lang = st.selectbox("Chọn ngôn ngữ:", languages)
    text = st.text_area("Nhập văn bản cần dịch:")
    if st.button("Dịch"):
        if text:
            try:
                translated = tools.translate(text, lang)
                st.success(f"✅ Kết quả dịch: {translated}")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

# Tab 4: Thời Gian
with tab4:
    st.header("⏰ Thời Gian Hiện Tại")
    if st.button("Lấy Thời Gian"):
        try:
            current_time = tools.get_time()
            st.info(f"🕐 {current_time}")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")

# Tab 5: Tìm Kiếm
with tab5:
    st.header("🔍 Tìm Kiếm Wikipedia")
    query = st.text_input("Nhập từ khóa tìm kiếm:")
    if query:
        try:
            result = tools.search(query)
            st.success(f"✅ {result}")
        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")

# Tab 6: JSON
with tab6:
    st.header("📋 Định Dạng JSON")
    json_input = st.text_area("Nhập JSON cần định dạng:")
    if st.button("Định Dạng"):
        if json_input:
            try:
                formatted = tools.format_json(json_input)
                st.success("✅ JSON đã định dạng:")
                st.code(formatted, language="json")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

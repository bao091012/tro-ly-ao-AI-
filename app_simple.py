"""
🤖 TRỢ LÝ AI ĐA NĂNG - Phiên Bản Đơn Giản
"""

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="🤖 Trợ Lý AI", page_icon="🤖", layout="wide")

st.markdown('<h1 style="text-align: center;">🤖 Trợ Lý AI Đa Năng</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Cấu Hình")
    default_key = os.getenv("GOOGLE_API_KEY", "AQ.Ab8RN6LasT9VWVMeub7XXB4VPt0v9X5qQAjEKOBMBLSNGxqIZA")
    api_key = st.text_input("Google API Key", value=default_key, type="password", help="https://aistudio.google.com/apikey")
    
    if api_key:
        st.success("✅ API Key nhập rồi!")
    else:
        st.warning("⚠️ Chưa nhập API Key")

# Main
if not api_key:
    st.error("❌ Vui lòng nhập Google API Key ở sidebar!")
else:
    try:
        genai.configure(api_key=api_key)
        
        # Chat interface
        st.subheader("💬 Hỏi AI")
        user_input = st.text_area("Nhập câu hỏi:", height=100)
        
        if st.button("Gửi", type="primary"):
            if user_input.strip():
                st.write("⏳ AI đang suy nghĩ...")
                
                try:
                    # Thử gemini-1.5-flash trước
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(user_input)
                    
                    st.success("✅ Trả lời từ AI:")
                    st.write(response.text)
                    
                except:
                    try:
                        # Thử gemini-pro nếu flash không được
                        model = genai.GenerativeModel("gemini-pro")
                        response = model.generate_content(user_input)
                        
                        st.success("✅ Trả lời từ AI:")
                        st.write(response.text)
                        
                    except Exception as e:
                        st.error(f"❌ Lỗi: {str(e)}")
                        st.info("💡 Hãy kiểm tra:\n1. API Key đúng không?\n2. Có kích hoạt Gemini API không?\n3. Internet có tốt không?")
            else:
                st.warning("⚠️ Nhập câu hỏi trước!")
        
        # Ví dụ
        st.divider()
        st.subheader("💡 Ví Dụ Câu Hỏi")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Xin chào"):
                st.session_state.input = "Xin chào"
        
        with col2:
            if st.button("2 + 2 = ?"):
                st.session_state.input = "2 + 2 bằng bao nhiêu?"
        
        with col3:
            if st.button("Mấy giờ rồi?"):
                st.session_state.input = "Bây giờ mấy giờ?"
    
    except Exception as e:
        st.error(f"❌ Lỗi: {str(e)}")

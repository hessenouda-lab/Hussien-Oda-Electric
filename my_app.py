import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 3. نافذة التأكيد (الديالوج)
@st.dialog("مراجعة رأيك قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1a1e24; padding: 20px; border-radius: 10px; border: 2px solid #d4af37; text-align: right;">
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-bottom: 5px;">👤 اسم العميل:</p>
            <p style="color: #ffffff; font-size: 18px; background: #0b0d11; padding: 10px; border-radius: 5px;">{name}</p>
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-top: 15px; margin-bottom: 5px;">💬 نص التعليق:</p>
            <p style="color: #ffffff; font-size: 18px; background: #0b0d11; padding: 10px; border-radius: 5px;">{text}</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("تأكيد ونشر على الموقع الآن ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.success("تم النشر بنجاح!")
        time.sleep(1)
        st.rerun()

# 4. التنسيق الفخم (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 12px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37; font-size: 32px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 26px; margin-top: 15px; }
    div.stButton > button { height: 85px !important; font-size: 26px !important; border-radius: 20px !important; font-weight: bold !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4

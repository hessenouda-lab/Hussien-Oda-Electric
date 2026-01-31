import streamlit as st
import time
import uuid

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. إنشاء هوية فريدة للمستخدم (عشان التعديل والحذف)
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# 3. مخزن التعليقات (مع حماية البيانات)
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "init_1", "user_id": "admin", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد.", "time": time.time() - 1000},
        {"id": "init_2", "user_id": "admin", "name": "أحمد علي", "text": "رجل محترم وأمين جداً.", "time": time.time() - 1000}
    ]

# 4. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: white !important; font-size: 20px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    .stButton>button {
        background-color: #ffde59 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار التواصل (اتصال + واتساب)
col_c, col_w = st.columns(2)
with col_c: st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:15px; border-radius:50px; text-align

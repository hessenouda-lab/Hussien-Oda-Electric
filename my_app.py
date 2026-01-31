import streamlit as st
import time
import uuid

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تأمين البيانات (منع KeyError)
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "1", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد."},
        {"id": "2", "name": "أحمد علي", "text": "رجل محترم وأمين جداً."}
    ]

# حالات المعاينة
if 'preview_mode' not in st.session_state:
    st.session_state.preview_mode = False
if 'temp_data' not in st.session_state:
    st.session_state.temp_data = {}

# 3. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    .preview-card { background-color: #1c1f26; border: 2px dashed #ffde59; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    
    /* تنسيق أزرار المعاينة */
    div.stButton > button {
        width: 100%;
        height: 55px;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 4. أزرار الاتصال (روابط مباشرة)
c_call, c_wa = st.columns(2)
with c_call:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:18px; border-radius:15px; text-align:center; font-size:20px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with c_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:18px; border-radius:15px; text-align:center; font

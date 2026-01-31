import streamlit as st
import time
import uuid

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. حفظ بيانات الجلسة
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "1", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد."},
        {"id": "2", "name": "أحمد علي", "text": "رجل محترم وأمين جداً."}
    ]

if 'preview_mode' not in st.session_state:
    st.session_state.preview_mode = False
if 'temp_review' not in st.session_state:
    st.session_state.temp_review = {}

# 3. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: white !important; font-size: 20px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    .preview-box { background-color: #1c1f26; border: 2px dashed #ffde59; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    
    div.stButton > button {
        font-weight: bold !important;
        width: 100%;
        height: 60px;
        font-size: 20px !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 4. روابط الاتصال والواتساب (روابط مباشرة)
c_call, c_wa = st.columns(2)
with c_call:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:20px; border-radius:15px; text-align:center; font-size:22px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with c_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:20px; border-radius:15px; text-align:center; font-size:22px; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 5. الخدمات
st.markdown("<h2>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>توزيع أحمال وتأسيس سمارت</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>ليد بروفايل ونجف حديث</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>لوحات توزيع ومفاتيح حماية</p></div>', unsafe_allow_html=True)

st.write("---")

# 6. الفيديوهات
st.markdown("<h2>🎬 كواليس العمل</h2>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
with v2:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.write("---")

# 7. عرض التعليقات
st.markdown("<h2>💬 آراء الناس في شغلنا</h2>", unsafe_allow_html=True)
for r in st.session_state.

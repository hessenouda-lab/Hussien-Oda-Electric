import streamlit as st
import time
import uuid

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# تأمين معرف المستخدم الفريد
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# قائمة التعليقات الأساسية
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "1", "user_id": "admin", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد.", "time": time.time() - 600},
        {"id": "2", "user_id": "admin", "name": "أحمد علي", "text": "رجل محترم وأمين جداً.", "time": time.time() - 600}
    ]

# تصميم الواجهة (CSS) لمنع تداخل الألوان وتوضيح الأزرار
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: white !important; font-size: 20px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    
    /* تصميم زرار التأكيد الضخم والواضح */
    div.stButton > button:first-child {
        background-color: #ffde59 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        border-radius: 12px;
        border: 2px solid #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار التواصل (اتصال + واتساب)
col_c, col_w = st.columns(2)
with col_c:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with col_w:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# الخدمات الاحترافية
st.markdown("<h2>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>تأسيس شقق وفيات بأحدث الأنظمة</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>ليد بروفايل ونجف وإضاءة حديثة</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>لوحات توزيع وحماية من الأعطال</p></div>', unsafe_allow_html=True)

st.write("---")

# قسم الفيديوهات
st.markdown("<h2>🎬 كواليس العمل</h2>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
with v2: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.write("---")

# عرض آراء العملاء
st.markdown("<h2>💬 آراء الناس في شغلنا</h2>", unsafe_allow_html=True)

for i, review in enumerate(st.session_state.reviews):
    u_id = review.get('user_id', '')
    r_time = review.get('time', 0)
    
    # التحقق: هل هذا تعليق المستخدم وهل متاح تعديله؟ (5 دقائق)
    is_me = u_id

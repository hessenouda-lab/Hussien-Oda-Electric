import streamlit as st
import uuid

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات (حل مشكلة KeyError)
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد."},
        {"name": "أحمد علي", "text": "رجل محترم وأمين جداً."}
    ]
if 'step' not in st.session_state:
    st.session_state.step = "write"  # لتنظيم عملية (كتابة -> مراجعة)
if 'temp_data' not in st.session_state:
    st.session_state.temp_data = {}

# 3. التصميم (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stApp { background: #0e1117; }
    h1, h2 { color: #ffde59 !important; text-align: center; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; }
    .preview-box { background: #1c1f26; border: 2px dashed #ffde59; padding: 20px; border-radius: 15px; }
    div.stButton > button { width: 100%; height: 50px; font-weight: bold; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء</h1>", unsafe_allow_html=True)

# 4. أزرار الاتصال المباشرة (حل مشكلة التوجيه)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background:#ff4b4b; color:white; padding:15px; border-radius:15px; text-align:center; font-weight:bold;">📞 اتصال مباشر</div></a>', unsafe_allow_html=True)
with c2:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:15px; border-radius:15px; text-align:center; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 5. عرض التعليقات
st.markdown("<h2>💬 آراء الناس في شغلنا</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><b>{r.get("name")}:</b> {r.get("text")}</div>', unsafe_allow_html=True)

st.write("---")

# 6. نظام التعليق المطور (كتابة -> مراجعة -> تأكيد)
st.markdown("### 📝 أضف تعليقك")

if st.session_state.step == "write":
    with st.form("comment_form", clear_on_submit=True):
        name = st.text_input("الاسم الكريم:")
        msg = st.text_area("رأيك في الخدمة:")
        submit = st.form_submit_button("عرض التعليق للمراجعة 👁️")
        if submit:
            if name and msg:
                st.session_state.temp_data = {"name": name, "text": msg}
                st.session_state.

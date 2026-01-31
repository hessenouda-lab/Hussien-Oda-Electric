import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات (حل مشكلة KeyError و SyntaxError)
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "شغل ممتاز وتسليم في الميعاد."},
        {"name": "محمد صلاح", "text": "رجل محترم وأمين جداً."}
    ]
if 'step' not in st.session_state:
    st.session_state.step = "writing"
if 'temp_msg' not in st.session_state:
    st.session_state.temp_msg = {}

# 3. التصميم (CSS) لمنع تداخل الألوان
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2 { color: #ffde59 !important; text-align: center; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    .preview-box { background-color: #1c1f26; border: 2px dashed #ffde59; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    div.stButton > button { width: 100%; height: 50px; font-weight: bold; border-radius: 12px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء</h1>", unsafe_allow_html=True)

# 4. أزرار الاتصال (روابط مباشرة بسيطة لمنع الأخطاء)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background:#ff4b4b; color:white; padding:15px; border-radius:15px; text-align:center; font-weight:bold; font-size:18px;">📞 اتصال مباشر</div></a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:15px; border-radius:15px; text-align:center; font-weight:bold; font-size:18px;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 5. عرض التعليقات
st.markdown("<h2>💬 آراء الناس في شغلنا</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><b>{r.get("name")}:</b> {r.get("text")}</div>', unsafe_allow_html=True)

st.write("---")

# 6. نظام التعليق (كتابة -> مراجعة -> نشر)
st.markdown("### 📝 اترك رأيك")

if st.session_state.step == "writing":
    with st.form("my_form", clear_on_submit=True):
        u_name = st.text_input("اسمك الكريم:")
        u_text = st.text_area("رأيك في الخدمة:")
        if st.form_submit_button("عرض التعليق للمراجعة 👁️"):
            if u_name and u_text:
                st.session_state.temp_msg = {"name": u_name, "text": u_text}
                st.session_state.step = "preview"
                st.rerun()
            else:
                st.error("من فضلك اكتب اسمك ورأيك")

elif st.session_state.step == "preview":
    st.markdown('<div class="preview-box">', unsafe_allow_html=True)
    st.info("🧐 هكذا سيظهر تعليقك للناس:")
    st.write(f"*الاسم:* {st.session_state.temp_msg['name']}")
    st.write(f"*الرسالة:* {st.session_state.temp_msg['text']}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    c_ok, c_edit = st.columns(2)
    with c_ok:
        if st.button("تأكيد ونشر ✅"):
            st.session_state.reviews.insert(0, st.session_state.temp_msg)
            st.session_state.step = "writing"
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()
    with c_edit:
        if st.button("تعديل الكلام ✏️"):
            st.session_state.step = "writing"
            st.rerun()

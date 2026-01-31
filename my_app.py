import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات الأساسية
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "شغل ممتاز وتسليم في الميعاد."},
        {"name": "محمد صلاح", "text": "رجل محترم وأمين جداً."}
    ]

# 3. وظيفة رسالة التأكيد (تظهر في وش الشاشة)
@st.dialog("تأكيد نشر التعليق ✅")
def confirm_dialog(name, text):
    st.write(f"*الاسم:* {name}")
    st.write(f"*التعليق:* {text}")
    st.write("---")
    st.info("هل تريد نشر هذا التعليق الآن أم تريد تعديله؟")
    
    col_ok, col_edit = st.columns(2)
    with col_ok:
        if st.button("تأكيد ونشر الآن 🚀"):
            st.session_state.reviews.insert(0, {"name": name, "text": text})
            st.success("تم النشر!")
            time.sleep(1)
            st.rerun()
    with col_edit:
        if st.button("رجوع للتعديل ✏️"):
            st.rerun()

# 4. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2 { color: #ffde59 !important; text-align: center; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    div.stButton > button { width: 100%; height: 50px; font-weight: bold; border-radius: 12px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال
c1, c2 = st.columns(2)
with c1:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background:#ff4b4b; color:white; padding:15px; border-radius:15px; text-align:center; font-weight:bold;">📞 اتصال مباشر</div></a>', unsafe_allow_html=True)
with c2:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:15px; border-radius:15px; text-align:center; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 6. عرض التعليقات المنشورة
st.markdown("<h2>💬 آراء الناس في شغلنا</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><b>{r.get("name")}:</b> {r.get("text")}</div>', unsafe_allow_html=True)

st.write("---")

# 7. منطقة إضافة التعليق
st.markdown("### 📝 اترك رأيك")
with st.form("main_form", clear_on_submit=True):
    u_name = st.text_input("اسمك الكريم:")
    u_text = st.text_area("رأيك في الخدمة:")
    submit = st.form_submit_button("إرسال التعليق 📤")
    
    if submit:
        if u_name and u_text:
            # استدعاء الرسالة اللي بتظهر في وش الشاشة
            confirm_dialog(u_name, u_text)
        else:
            st.error("من فضلك اكتب اسمك ورأيك")

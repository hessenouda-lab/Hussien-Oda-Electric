import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد
@st.dialog("تأكيد نشر رأيك ⚡")
def confirm_dialog(name, text):
    st.write(f"*العميل:* {name}")
    st.write(f"*الرأي:* {text}")
    if st.button("نشر الآن ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.rerun()

# 4. التنسيق الفخم
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; font-size: 40px !important; text-align: center; }
    .review-box { background: #161a21; padding: 25px; border-radius: 15px; border-right: 8px solid #d4af37; margin-bottom: 20px; }
    .client-name { color: #d4af37; font-size: 24px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 22px; }
    
    /* تنسيق الأزرار الأصلية لتكون ضخمة وفخمة */
    div.stButton > button {
        height: 80px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        border-radius: 20px !important;
    }
    /* زر الاتصال أحمر */
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    /* زر الواتساب أخضر */
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (باستخدام أزرار النظام الأصلية لضمان العمل على الماسنجر)
col1, col2 = st.columns(2)

with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        # كود جافا سكريبت لإجبار الموبايل على الاتصال
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)

with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        # كود جافا سكريبت لإجبار الموبايل على فتح الواتساب
        st.components.v1.html("""<script>window.open("https://api.whatsapp.com/send?phone=201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. التقييمات
st.markdown("<h2 style='color:#d4af37; text-align:center;'>🌟 آراء العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_

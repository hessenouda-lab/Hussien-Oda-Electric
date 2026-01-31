import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات (عشان م يحصلش KeyError)
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد (المودال)
@st.dialog("تأكيد نشر رأيك ⚡")
def confirm_dialog(name, text):
    st.write(f"*المرسل:* {name}")
    st.write(f"*الرأي:* {text}")
    if st.button("اعتماد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.rerun()

# 4. التنسيق (الفخامة والخطوط الكبيرة)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; font-size: 45px !important; text-align: center; }
    .review-box { 
        background: #161a21; padding: 30px; border-radius: 20px; 
        border-right: 10px solid #d4af37; margin-bottom: 25px;
    }
    .client-name { color: #d4af37; font-size: 28px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 24px; margin-top: 15px; }
    
    /* تنسيق أزرار الاتصال والواتساب */
    div.stButton > button {
        height: 75px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
    }
    /* لون زر الاتصال */
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    /* لون زر الواتساب */
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (الحل البرمجي لإجبار الماسنجر)
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://wa.me/201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. عرض التعليقات (السطر اللي كان فيه المشكلة صلحناه هنا)
st.markdown("<h2 style='color:#d4af37; text-align:center;'>🌟 آراء العملاء</h2>", unsafe_allow_html=True)

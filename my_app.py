import streamlit as st
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. حفظ التعليقات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد المنبثقة
@st.dialog("تأكيد نشر رأيك ⚡")
def confirm_dialog(name, text):
    st.markdown(f'<div style="text-align:right; color:white;"><b>المرسل:</b> {name}<br><b>الرأي:</b> {text}</div>', unsafe_allow_html=True)
    if st.button("تأكيد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.rerun()

# 4. التنسيق الفخم (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { background: #161a21; padding: 25px; border-radius: 15px; border-right: 10px solid #d4af37; margin-bottom: 20px; }
    .client-name { color: #d4af37; font-size: 26px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 22px; margin-top: 10px; }
    div.stButton > button { height: 75px !important; font-size: 24px !important; border-radius: 15px !important; font-weight: bold !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    .social-link { display: inline-block; padding: 12px 25px; margin: 5px; border-radius: 10px; text-decoration: none; font-weight: bold; color: white !important; font-size: 18px; }
    .fb { background-color: #1877F2; } .tt { background-color: #000000; border: 1px solid #fe2c55; } .yt { background-color: #FF0000; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (النسخة الذكية للماسنجر)
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://api.whatsapp.com/send?phone=201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. روابط السوشيال ميديا
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <a href="#" target="_blank" class="social-link fb">🔵 فيسبوك</a>
        <a href="#" target="_blank" class="social-link tt">⚫ تيك توك</a>
        <a href="#" target="_blank" class="social-link yt">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 7. معرض الأعمال

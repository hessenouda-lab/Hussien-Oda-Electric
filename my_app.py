import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد
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
    .review-box { background: #161a21; padding: 20px; border-radius: 15px; border-right: 8px solid #d4af37; margin-bottom: 15px; }
    .client-name { color: #d4af37; font-size: 22px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 18px; }
    
    /* تنسيق أزرار الاتصال */
    div.stButton > button { height: 70px !important; font-size: 22px !important; border-radius: 15px !important; font-weight: bold !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    
    /* تنسيق روابط السوشيال ميديا */
    .social-link {
        display: inline-block; padding: 10px 20px; margin: 5px;
        border-radius: 10px; text-decoration: none; font-weight: bold; color: white !important;
    }
    .fb { background-color: #1877F2; }
    .tt { background-color: #000000; border: 1px solid #fe2c55; }
    .yt { background-color: #FF0000; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال السريع
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://api.whatsapp.com/send?phone=201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. قسم السوشيال ميديا (حط روابطك هنا)
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <a href="رابط_صفحة_الفيسبوك_هنا" target="_blank" class="social-link fb">🔵 فيسبوك</a>
        <a href="رابط_تيك_توك_هنا" target="_blank" class="social-link tt">⚫ تيك توك</a>
        <a href="رابط_قناة_اليوتيوب_هنا" target="_blank" class="social-link yt">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 7. معرض الصور والفيديوهات (شغلك العملي)
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["🎥 فيديوهات", "🖼️ صور الشغل"])

with tab1:
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.video("https://www.youtube.com/watch?v=رابط_فيديو_1") # حط رابط يوتيوب هنا
    with v_col2:
        st.video("https://www.youtube.com/watch?v=رابط_فيديو_2") # حط رابط يوتيوب هنا

with tab2:
    img_col1, img_col2, img_col3 = st.columns(3)
    # ملاحظة: استبدل الروابط تحت بروابط صور حقيقية لشغلك
    with img_col1:
        st.image("https://via.placeholder.com/400x300", caption="تأسيس لوحة مفاتيح")
    with img_col2:
        st.image("https://via.placeholder.com/400x300", caption="تشطيب إضاءة حديثة")
    with img_col3:
        st.image("https://via.placeholder.com/400x300", caption="توزيع أحمال")

st.write("---")

# 8. التعليقات والفورم
st.markdown("<h2>🌟 آراء العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

with st.form("final_hussien_form", clear_on_submit=True):
    u_name = st.text_input("اسمك:")
    options = ["شغل احترافي ⚡", "أمان

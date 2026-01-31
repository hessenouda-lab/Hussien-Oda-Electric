import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات الأساسية
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

# 4. التنسيق الفخم
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; }
    .review-box { background: #161a21; padding: 20px; border-radius: 15px; border-right: 8px solid #d4af37; margin-bottom: 15px; }
    .client-name { color: #d4af37; font-size: 22px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 18px; }
    div.stButton > button { height: 70px !important; font-size: 20px !important; border-radius: 15px !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (نسخة الماسنجر المعتمدة)
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://api.whatsapp.com/send?phone=201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. قسم الفيديوهات الجديد (YouTube + Social Links)
st.markdown("<h2>🎥 معرض أعمالنا (فيديو)</h2>", unsafe_allow_html=True)
v_col1, v_col2 = st.columns(2)

with v_col1:
    # ضع رابط فيديو اليوتيوب الخاص بك هنا
    st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID") 
    st.markdown("""
        <div style="text-align:center;">
            <a href="https://facebook.com/YOUR_PAGE" target="_blank">🔵 الفيسبوك</a> | 
            <a href="https://tiktok.com/@YOUR_USER" target="_blank">⚫ تيك توك</a>
        </div>
    """, unsafe_allow_html=True)

with v_col2:
    st.info("💡 قريباً: فيديوهات أحدث المشاريع")

st.write("---")

# 7. التعليقات والفورم
st.markdown("<h2>🌟 آراء العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

with st.form("hussien_pro_form", clear_on_submit=True):
    u_name = st.text_input("اسمك الكريم:")
    options = ["شغل احترافي ⚡", "أمانة ودقة ✅", "تأسيس ممتاز ⭐"]
    selected = st.selectbox("رأي جاهز:", options)
    u_custom = st.text_area("رأيك الخاص:")
    if st.form_submit_button("نشر التقييم ✨"):
        final = u_custom if u_custom else selected
        if u_name and final: confirm_dialog(u_name, final)

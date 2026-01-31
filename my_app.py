import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات في الذاكرة
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي."}]
if 'gallery_videos' not in st.session_state:
    st.session_state.gallery_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'gallery_images' not in st.session_state:
    st.session_state.gallery_images = ["https://via.placeholder.com/400x300"]

# 3. نافذة التأكيد للعملاء
@st.dialog("مراجعة بيانات التعليق ⚡")
def confirm_dialog(name, text):
    st.markdown(f'<div style="text-align:right; color:white;"><b>المرسل:</b> {name}<br><b>الرأي:</b> {text}</div>', unsafe_allow_html=True)
    if st.button("تأكيد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.rerun()

# 4. التنسيق الفخم (CSS الماسي)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { background: #161a21; padding: 25px; border-radius: 15px; border-right: 10px solid #d4af37; margin-bottom: 15px; }
    .client-name { color: #d4af37; font-size: 24px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 20px; }
    div.stButton > button { height: 70px !important; font-size: 22px !important; border-radius: 15px !important; font-weight: bold !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    .social-link { display: inline-block; padding: 12px 25px; margin: 5px; border-radius: 10px; text-decoration: none; font-weight: bold; color: white !important; font-size: 18px; }
    .fb { background-color: #1877F2; } .tt { background-color: #000000; border: 1px solid #fe2c55; } .yt { background-color: #FF0000; }
    </style>
""", unsafe_allow_html=True)

# 5. لوحة التحكم (متاحة لك أنت فقط بكلمة سر)
with st.sidebar:
    st.markdown("### 🔐 إدارة المحتوى")
    password = st.text_input("كلمة السر للإضافة:", type="password")
    if password == "1234": # تقدر تغير كلمة السر دي براحتك
        st.success("مرحباً يا حسين! يمكنك الإضافة الآن")
        new_v = st.text_input("رابط فيديو يوتيوب جديد:")
        if st.button("إضافة فيديو 🎥"):
            st.session_state.gallery_videos.append(new_v)
        new_img = st.text_input("رابط صورة جديدة:")
        if st.button("إضافة صورة 🖼️"):
            st.session_state.gallery_images.append(new_img)
    else:
        st.info("هذا الجزء مخصص للمسؤول فقط")

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 6. أزرار الاتصال الذكية
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://api.whatsapp.com/send?phone=201123393030", "_blank");</script>""", height=0)

st.write("---")

# 7. روابط السوشيال ميديا الحقيقية (استبدل # بروابطك)
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="#" target="_blank" class="social-link fb">🔵 فيسبوك</a>
        <a href="#" target="_blank" class="social-link tt">⚫ تيك توك</a>
        <a href="#" target="_blank" class="social-link yt">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 8. معرض الأعمال (يعرض ما تضيفه أنت فقط)
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["🎥 الفيديوهات", "🖼️ الصور"])
with tab1:
    for vid in st.session_state.gallery_videos:
        st.video(vid)
with tab2:
    st.image(st.session_state.gallery_images, width=300)

st.write("---")

# 9. التعليقات والفورم
st.markdown("<h2>🌟 آراء العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

with st.form("hussien_diamond_v2", clear_on_submit=True):
    u_name = st.text_input("اسم العميل:")
    u_custom = st.text_area("رأيك الخاص:")
    if st.form_submit_button("إرسال التقييم ✨"):
        if u_name and u_custom:
            confirm_dialog(u_name, u_custom)

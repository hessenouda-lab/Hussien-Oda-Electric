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
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 3. نافذة التأكيد (المودال الماسي الأصلي)
@st.dialog("مراجعة بيانات التعليق ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #121212; padding: 25px; border-radius: 15px; border: 3px solid #d4af37; text-align: right; color: white;">
            <p style="color: #d4af37; font-weight: bold; font-size: 24px;">👤 المرسل: {name}</p>
            <p style="font-size: 22px;">💬 الرأي: "{text}"</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("اعتماد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.success("تم النشر بنجاح!")
        time.sleep(1)
        st.rerun()

# 4. التنسيق الفخم (CSS الماسي)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 12px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37; font-size: 32px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 26px; margin-top: 15px; line-height: 1.5; }
    div.stButton > button { height: 85px !important; font-size: 26px !important; border-radius: 20px !important; font-weight: bold !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    .social-link { display: inline-block; padding: 15px 35px; margin: 10px; border-radius: 15px; text-decoration: none; font-weight: bold; color: white !important; font-size: 22px; transition: 0.3s; }
    .fb { background-color: #1877F2; } .tt { background-color: #000000; border: 2px solid #fe2c55; } .yt { background-color: #FF0000; }
    </style>
""", unsafe_allow_html=True)

# 5. لوحة التحكم السرية
with st.sidebar.expander("🔐 لوحة تحكم حسين"):
    adm_pass = st.text_input("كلمة السر:", type="password")
    if adm_pass == "1234":
        v_url = st.text_input("رابط فيديو يوتيوب:")
        if st.button("حفظ الفيديو 🎥"): st.session_state.my_videos.append(v_url)
        i_url = st.text_input("رابط صورة:")
        if st.button("حفظ الصورة 🖼️"): st.session_state.my_images.append(i_url)

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

# 7. روابط السوشيال ميديا الحقيقية
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-link fb">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-link tt">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-link yt">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 8. معرض الأعمال
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
t1, t2 = st.tabs(["🎥 فيديوهات الشغل", "🖼️ صور المواقع"])
with t1:
    for v in st.session_state.my_videos:
        st.video(v)
with t2:
    for img in st.session_state.my_images:
        st.image(img, use_container_width=True)

st.write("---")

# 9. عرض التعليقات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'''
        <div class="review-box">
            <div class="client-name">👤 {r.get("name")}</div>
            <div class="client-text">{r.get("text

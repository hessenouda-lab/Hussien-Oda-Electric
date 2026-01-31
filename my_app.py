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

# 3. نافذة التأكيد (تم إصلاح ظهور النص)
@st.dialog("مراجعة رأيك قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1a1e24; padding: 20px; border-radius: 10px; border: 2px solid #d4af37; text-align: right;">
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-bottom: 5px;">👤 اسم العميل:</p>
            <p style="color: #ffffff; font-size: 18px; background: #0b0d11; padding: 10px; border-radius: 5px;">{name}</p>
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-top: 15px; margin-bottom: 5px;">💬 نص التعليق:</p>
            <p style="color: #ffffff; font-size: 18px; background: #0b0d11; padding: 10px; border-radius: 5px;">{text}</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("تأكيد ونشر على الموقع الآن ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.success("تم النشر بنجاح!")
        time.sleep(1)
        st.rerun()

# 4. التنسيق الفخم (CSS) - تم إصلاح علامات التنصيص هنا
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
    .client-text { color: #ffffff; font-size: 26px; margin-top: 15px; }
    div.stButton > button { height: 85px !important; font-size: 26px !important; border-radius: 20px !important; font-weight: bold !important; }
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    .social-link { display: inline-block; padding: 15px 35px; margin: 10px; border-radius: 15px; text-decoration: none; font-weight: bold; color: white !important; font-size: 22px; }
    .fb { background-color: #1877F2; } .tt { background-color: #000000; border: 2px solid #fe2c55; } .yt { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://wa.me/201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. السوشيال ميديا
st.markdown(f"""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-link fb">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-link tt">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-link yt">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 7. معرض الأعمال
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
t1, t2 = st.tabs(["🎥 فيديوهات الشغل", "🖼️ صور المواقع"])
with t1:
    for v in st.session_state.my_videos:
        st.video(v)
with t2:
    for img in st.session_state.my_images:
        st.image(img, use_container_width=True)

st.write("---")

# 8. عرض التعليقات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f"""
        <div class="review-box">
            <div class="client-name">👤 {r.get('name')}</div>
            <div class="client-text">{r.get('text')}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 9. فورم التعليق
with st.form("diamond_final_form", clear_on_submit=True):
    u_name = st.text_input("اسمك الكريم:")
    options = ["اختر رأياً جاهزاً...", "شغل احترافي وتسليم في الموعد ⚡", "أمانة ودقة في المواعيد ✅", "تأسيس كهرباء ممتاز ⭐"]
    selected = st.selectbox("رأيك في الخدمة:", options)
    u_custom = st.text_area("أو اكتب رأيك الخاص:")
    submit = st.form_submit_button("عرض التعليق للتأكيد ✨")
    if submit:
        final_msg = u_custom if u_custom.strip() != "" else (selected if selected != options[0] else "")
        if u_name and final_msg:
            confirm_dialog(u_name, final_msg)
        else:
            st.warning("⚠️ نرجو كتابة الاسم والتعليق")

# 10. لوحة التحكم
with st.sidebar.expander("🔐 إدارة المحتوى"):
    passw = st.text_input("كلمة السر:", type="password")
    if passw == "1234":
        new_v = st.text_input("رابط يوتيوب جديد:")
        if st.button("إضافة فيديو"):
            st.session_state.my_videos.append(new_v)
            st.rerun()

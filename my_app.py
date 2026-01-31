import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات الأساسية
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."}]
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 3. التنسيق (CSS) - الأزرار الآن أصبحت روابط بتنسيق أزرار
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { background: #161a21; padding: 35px; border-radius: 20px; border-right: 12px solid #d4af37; margin-bottom: 25px; }
    .client-name { color: #d4af37; font-size: 32px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 26px; margin-top: 15px; }
    
    /* تصميم الروابط لتظهر كأزرار ضخمة */
    .btn-link {
        display: block; width: 100%; height: 85px; line-height: 85px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; 
        color: white !important; margin-bottom: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .call-bg { background-color: #ff4b4b; }
    .wa-bg { background-color: #25d366; }
    
    .social-btn {
        display: inline-block; padding: 18px 35px; margin: 8px;
        border-radius: 15px; text-decoration: none !important;
        color: white !important; font-size: 22px; font-weight: bold;
    }
    .fb-bg { background-color: #1877F2; }
    .tt-bg { background-color: #000000; border: 2px solid #fe2c55; }
    .yt-bg { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 4. أزرار الاتصال (روابط مباشرة HTML - أقوى وسيلة للماسنجر)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="btn-link call-bg">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="btn-link wa-bg">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 5. روابط السوشيال ميديا (روابط مباشرة صريحة)
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-btn fb-bg">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-btn tt-bg">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-btn yt-bg">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 6. معرض الأعمال والتعليقات (باقي الكود الماسي كما هو)
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
t1, t2 = st.tabs(["🎥 فيديوهات الشغل", "🖼️ صور المواقع"])
with t1:
    for v in st.session_state.my_videos: st.video(v)
with t2:
    for img in st.session_state.my_images: st.image(img, use_container_width=True)

st.write("---")
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

st.write("---")
with st.form("diamond_final_form", clear_on_submit=True):
    u_name = st.text_input("اسمك الكريم:")
    u_custom = st.text_area("اكتب رأيك هنا:")
    if st.form_submit_button("نشر التعليق ✨"):
        if u_name and u_custom:
            st.session_state.reviews.insert(0, {"name": u_name, "text": u_custom})
            st.rerun()

with st.sidebar.expander("🔐 لوحة التحكم"):
    passw = st.text_input("كلمة السر:", type="password")
    if passw == "1234":
        new_v = st.text_input("رابط يوتيوب:")
        if st.button("إضافة"):
            st.session_state.my_videos.append(new_v)
            st.rerun()

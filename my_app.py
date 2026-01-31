import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."}]
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 3. التنسيق الماسي الفخم (العودة للأصل)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 15px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; }
    
    /* تصميم الأزرار الروابط */
    .btn-diamond {
        display: block; width: 100%; height: 85px; line-height: 85px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; 
        color: white !important; margin-bottom: 15px;
    }
    .call-bg { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .wa-bg { background: linear-gradient(45deg, #25d366, #128c7e); }
    
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

# 4. أزرار الاتصال (كود JS لاختراق الماسنجر)
def open_link(url):
    st.components.v1.html(f'<script>window.open("{url}", "_blank");</script>', height=0)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="btn-diamond call-bg">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="btn-diamond wa-bg">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 5. روابط السوشيال ميديا
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" class="social-btn fb-bg">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" class="social-btn tt-bg">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" class="social-btn yt-bg">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 6. معرض الأعمال
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
t1, t2 = st.tabs(["🎥 فيديوهات الشغل", "🖼️ صور المواقع"])
with t1:
    for v in st.session_state.my_videos: st.video(v)
with t2:
    for img in st.session_state.my_images: st.image(img, use_container_width=True)

st.write("---")

# 7. عرض التعليقات (بالتنسيق الضخم الأصلي)
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f"""
        <div class="review-box">
            <div class="client-name">👤 {r.get('name')}</div>
            <div class="client-text">{r.get('text')}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 8. فورم الإضافة
with st.form("final_diamond_v5", clear_on_submit=True):
    u_name = st.text_input("اسمك الكريم:")
    u_text = st.text_area("رأيك في الخدمة:")
    if st.form_submit_button("نشر التعليق ✨"):
        if u_name and u_text:
            st.session_state.reviews.insert(0, {"name": u_name, "text": u_text})
            st.rerun()

# 9. لوحة التحكم الجانبية
with st.sidebar.expander("🔐 إدارة الموقع"):
    if st.text_input("كلمة السر:", type="password") == "1234":
        new_v = st.text_input("رابط يوتيوب جديد:")
        if st.button("إضافة"):
            st.session_state.my_videos.append(new_v)
            st.rerun()

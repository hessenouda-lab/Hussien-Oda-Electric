import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. رسالة إرشادية راقية لعملاء الماسنجر
st.components.v1.html("""
<script>
    var isFB = /FBAN|FBAV|Messenger/i.test(navigator.userAgent);
    if (isFB) {
        alert("عميلنا العزيز، لضمان سهولة التواصل معنا عبر أزرار الاتصال والواتساب، يرجى الضغط على الثلاث نقاط في أعلى الشاشة واختيار 'الفتح في المتصفح' (Open in Browser).");
    }
</script>
""", height=0)

# 3. تهيئة البيانات الثابتة
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."}]
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 4. نافذة التأكيد (المودال الذهبي الفخم)
@st.dialog("مراجعة رأيك قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1a1e24; padding: 25px; border-radius: 15px; border: 3px solid #d4af37; text-align: right; color: white;">
            <p style="color: #d4af37; font-weight: bold; font-size: 24px;">👤 الاسم: {name}</p>
            <p style="font-size: 22px;">💬 التعليق: "{text}"</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("تأكيد ونشر التعليق ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.success("تم نشر رأيك بنجاح!")
        time.sleep(1)
        st.rerun()

# 5. التنسيق الماسي الأصلي (استعادة الأبعاد الفخمة)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    
    /* تصميم صندوق التعليق المعتمد */
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 15px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; display: block; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; display: block; }
    
    .diamond-btn {
        display: block; width: 100%; height: 85px; line-height: 85px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; 
        color: white !important; margin-bottom: 15px;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
    
    .social-btn {
        display: inline-block; padding: 18px 35px; margin: 8px;
        border-radius: 15px; text-decoration: none !important;
        color: white !important; font-size: 22px; font-weight: bold;
    }
    .fb-bg { background-color: #1877F2; } .tt-bg { background-color: #000000; border: 2px solid #fe2c55; } .yt-bg { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 6. أزرار التواصل المباشر
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 7. منصات التواصل الاجتماعي
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-btn fb-bg">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-btn tt-bg">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-btn yt-bg">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 8. معرض الأعمال
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
t1, t2 = st.tabs(["🎥 فيديوهات الشغل", "🖼️ صور المواقع"])
with t1:
    for v in st.session_state.my_videos: st.video(v)
with t2:
    for img in st.session_state.my_images: st.image(img, use_container_width=True)

st.write("---")

# 9. عرض التعليقات (بالتنسيق الضخم الأصلي)
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f"""
        <div class="review-box">
            <div class="client-name">👤 {r.get('name')}</div>
            <div class="client-text">{r.get('text')}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 10. نموذج إضافة تعليق
with st.form("diamond_final_v10", clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    u_custom = st.text_area("رأيك في جودة العمل:")
    if st.form_submit_button("عرض التعليق للتأكيد ✨"):
        if u_name and u_custom:
            confirm_dialog(u_name, u_custom)
        else:
            st.warning("⚠️ يرجى كتابة الاسم والتعليق أولاً")

# 11. لوحة التحكم
with st.sidebar.expander("🔐 إدارة المحتوى"):
    if st.text_input("كلمة السر:", type="password") == "1234":
        new_v = st.text_input("رابط يوتيوب جديد:")
        if st.button("إضافة فيديو"):
            st.session_state.my_videos.append(new_v)
            st.rerun()

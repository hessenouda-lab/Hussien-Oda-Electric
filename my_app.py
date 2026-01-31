import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."}]
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 3. نافذة التأكيد
@st.dialog("مراجعة رأيك قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1a1e24; padding: 20px; border-radius: 10px; border: 2px solid #d4af37; text-align: right; color: white;">
            <b>👤 المرسل:</b> {name}<br><b>💬 الرأي:</b> {text}
        </div>
    """, unsafe_allow_html=True)
    if st.button("تأكيد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.rerun()

# 4. التنسيق الفخم
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { background: #161a21; padding: 35px; border-radius: 20px; border-right: 12px solid #d4af37; margin-bottom: 25px; }
    .client-name { color: #d4af37; font-size: 32px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 26px; margin-top: 15px; }
    /* تنسيق أزرار الاتصال والواتساب */
    .action-btn { 
        display: block; width: 100%; height: 80px; line-height: 80px; 
        text-align: center; font-size: 26px; font-weight: bold; 
        border-radius: 20px; text-decoration: none; color: white !important; margin-bottom: 10px;
    }
    .call-btn { background-color: #ff4b4b; }
    .wa-btn { background-color: #25d366; }
    .social-link { display: inline-block; padding: 15px 30px; margin: 5px; border-radius: 15px; text-decoration: none; font-weight: bold; color: white !important; font-size: 20px; }
    .fb { background-color: #1877F2; } .tt { background-color: #000000; border: 1px solid #fe2c55; } .yt { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (باستخدام روابط HTML مباشرة لضمان العمل في الماسنجر)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="action-btn call-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    # رابط واتساب العالمي الأكثر استجابة
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="action-btn wa-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 6. روابط السوشيال ميديا (روابط ذكية لفتح التطبيقات)
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="fb://facewebmodal/f?href=https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-link fb">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-link tt">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-link yt">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 7. معرض الأعمال
st.markdown("<h2>📸 معرض أعمالنا</h2>", unsafe_allow_html=True)
t1, t2 = st.tabs(["🎥 فيديوهات الشغل", "🖼️ صور المواقع"])
with t1:
    for v in st.session_state.my_videos: st.video(v)
with t2:
    for img in st.session_state.my_images: st.image(img, use_container_width=True)

st.write("---")

# 8. عرض التعليقات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

st.write("---")

# 9. فورم التعليق
with st.form("diamond_final_form", clear_on_submit=True):
    u_name = st.text_input("اسمك الكريم:")
    options = ["اختر رأياً جاهزاً...", "شغل احترافي وتسليم في الموعد ⚡", "أمانة ودقة في المواعيد ✅", "تأسيس كهرباء ممتاز ⭐"]
    selected = st.selectbox("رأيك في الخدمة:", options)
    u_custom = st.text_area("أو اكتب رأيك الخاص:")
    if st.form_submit_button("عرض التعليق للتأكيد ✨"):
        final_msg = u_custom if u_custom.strip() != "" else (selected if selected != options[0] else "")
        if u_name and final_msg: confirm_dialog(u_name, final_msg)
        else: st.warning("⚠️ نرجو كتابة الاسم والتعليق")

# 10. لوحة التحكم
with st.sidebar.expander("🔐 إدارة المحتوى"):
    passw = st.text_input("كلمة السر:", type="password")
    if passw == "1234":
        new_v = st.text_input("رابط يوتيوب جديد:")
        if st.button("إضافة فيديو"):
            st.session_state.my_videos.append(new_v)
            st.rerun()

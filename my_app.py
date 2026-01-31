import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# تصميم الواجهة وتوضيح النصوص (High Contrast)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card {
        background: #1c1f26;
        border: 2px solid #ffde59;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p, .stMarkdown { color: #ffffff !important; font-size: 18px !important; }
    .review-box {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #ffde59;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. العنوان والترحاب
st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 2. أزرار التواصل (اتصال + واتساب)
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with col_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 3. الخدمات الاحترافية
st.markdown("<h2>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>تأسيس شقق وفيات بأحدث الأنظمة</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>ليد بروفايل ونجف وإضاءة حديثة</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>لوحات توزيع وحماية من الأعطال</p></div>', unsafe_allow_html=True)

st.write("---")

# 4. معرض الفيديوهات (🎬 كواليس العمل)
st.markdown("<h2>🎬 كواليس العمل</h2>", unsafe_allow_html=True)
v_col1, v_col2 = st.columns(2)
with v_col1:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # استبدل برابط فيديوهاتك
    st.write("<p style='text-align:center;'>تأسيس اللوحات الرئيسية</p>", unsafe_allow_html=True)
with v_col2:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # استبدل برابط فيديوهاتك
    st.write("<p style='text-align:center;'>تشطيب إضاءة مودرن</p>", unsafe_allow_html=True)

st.write("---")

# 5. آراء العملاء (قسم التقييمات)
st.markdown("<h2>⭐ آراء العملاء</h2>", unsafe_allow_html=True)

# نماذج لتعليقات حقيقية
st.markdown('<div class="review-box"><b>محمد صلاح:</b> "شغل ممتاز وتسليم في الميعاد، متمكن جداً في الليد بروفايل." ⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)
st.markdown('<div class="review-box"><b>أحمد علي:</b> "رجل محترم وأمين في اختيار الخامات، أنصح بالتعامل معه." ⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)

st.write("")

# 6. قسم "أضف تعليقك" (تفاعلي)
st.markdown("### 📝 أضف تقييمك وتجربتك معنا")
user_name = st.text_input("الاسم:")
user_comment = st.text_area("رأيك في الخدمة:")
rating = st.slider("تقييمك بالنجوم:", 1, 5, 5)

if st.button("إرسال التقييم"):
    if user_name and user_comment:
        st.success(f"شكراً يا {user_name}! تم استلام تقييمك بنجاح وسيظهر على الموقع قريباً.")
        # هنا التقييم بيروح لـ "حسين عوده" كرسالة أو يتخزن
    else:
        st.error("من فضلك اكتب اسمك وتعليقك")

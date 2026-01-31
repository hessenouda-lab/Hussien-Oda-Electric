import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# CSS التصميم الاحترافي
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: #ffffff !important; font-size: 18px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار التواصل
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with col_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# الخدمات
st.markdown("<h2>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>تأسيس شقق وفيات بأحدث الأنظمة</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>ليد بروفايل ونجف وإضاءة حديثة</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>لوحات توزيع وحماية من الأعطال</p></div>', unsafe_allow_html=True)

st.write("---")

# آراء العملاء (النظام التفاعلي الجديد)
st.markdown("<h2>⭐ آراء العملاء</h2>", unsafe_allow_html=True)

# استخدام session_state لتخزين التعليقات مؤقتاً في الصفحة
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد، متمكن جداً.", "stars": "⭐⭐⭐⭐⭐"},
        {"name": "أحمد علي", "text": "رجل محترم وأمين في اختيار الخامات.", "stars": "⭐⭐⭐⭐⭐"}
    ]

# عرض التعليقات
for review in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><b>{review["name"]}:</b> "{review["text"]}" {review["stars"]}</div>', unsafe_allow_html=True)

st.write("---")

# قسم "أضف تقييمك"
st.markdown("### 📝 اترك بصمتك (تقييمك يهمنا)")
u_name = st.text_input("الاسم الكريم:")
u_comment = st.text_area("رأيك في خدمة حسين عوده:")
u_rating = st.select_slider("اختر عدد النجوم:", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")

if st.button("انشر تقييمي الآن 🚀"):
    if u_name and u_comment:
        # إضافة التعليق الجديد للقائمة فوراً
        new_review = {"name": u_name, "text": u_comment, "stars": u_rating}
        st.session_state.reviews.append(new_review)
        st.success("تم نشر تقييمك فوراً على الصفحة! شكراً لثقتك.")
        st.rerun() # إعادة تشغيل الصفحة لعرض التعليق الجديد فوراً
    else:
        st.error("من فضلك املأ البيانات عشان تقييمك يظهر")

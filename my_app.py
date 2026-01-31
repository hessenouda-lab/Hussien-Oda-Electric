import streamlit as st

# اسم الصفحة اللي بيظهر فوق في المتصفح
st.set_page_config(page_title="حسين عوده للأعمال الكهربائية", layout="wide")

# التصميم الاحترافي بالألوان اللي اتفقنا عليها
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .big-button-red { background-color: #ff4b4b; color: white !important; padding: 25px; text-align: center; border-radius: 15px; font-size: 35px !important; font-weight: bold; text-decoration: none; display: block; margin-bottom: 20px; border: 3px solid white; }
    .big-button-green { background-color: #25d366; color: white !important; padding: 25px; text-align: center; border-radius: 15px; font-size: 35px !important; font-weight: bold; text-decoration: none; display: block; margin-bottom: 20px; border: 3px solid white; }
    .rating-box { text-align: center; color: #f1c40f; font-size: 25px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# التقييم والاسم الجديد بالهاء (عوده)
st.markdown('<div class="rating-box">⭐⭐⭐⭐⭐ (ثقة العملاء)</div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #f1c40f;'>⚡ حسين عوده لجميع الأعمال الكهربائية</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>خبرة 20 عاماً في خدمتكم</h3>", unsafe_allow_html=True)

st.divider()

# أزرار التواصل المباشر (توجيه تلقائي للاتصال والواتساب)
st.markdown('<a href="tel:01123393030" class="big-button-red">🚨 اتصل الآن: 01123393030</a>', unsafe_allow_html=True)
st.markdown('<a href="https://wa.me/201123393030?text=يا%20بشمهندس%20حسين%20محتاج%20شغل%20كهرباء" class="big-button-green">💬 واتساب: 01123393030</a>', unsafe_allow_html=True)

st.divider()

# معرض الفيديوهات التفاعلي
st.header("🎬 معرض الأعمال (شغل حسين عوده)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 ليد بروفايل وتشطيب")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # هنا مكان فيديوهاتك
    st.button("❤️ أعجبني", key="like_v1")

with col2:
    st.subheader("🏗️ تأسيس وصيانة قفلات")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # هنا مكان فيديوهاتك
    st.button("❤️ أعجبني", key="like_v2")

# كلمات البحث لضمان الظهور في جوجل (SEO)
st.caption("كهربائي الطالبية | حسين عوده كهرباء الهرم | فني كهرباء السيدة زينب | تأسيس كهرباء الجيزة")

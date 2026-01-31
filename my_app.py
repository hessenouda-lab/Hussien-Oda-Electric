import streamlit as st

# إضافة كلمات البحث بالعربي والإنجليزي لجوجل
st.set_page_config(
    page_title="حسين عوده - Hussien Oda Electric",
    page_icon="⚡",
    layout="wide"
)

# كلمات دليلية مخفية لجوجل (SEO)
st.markdown("""
    <meta name="description" content="حسين عوده لجميع الأعمال الكهربائية - Hussien Oda for Electrical Works. متخصص في الليد بروفايل والتأسيس.">
    <meta name="keywords" content="حسين عوده, كهربائي, Hussien Oda, Electrician, كهرباء الطالبية, الهرم">
    """, unsafe_allow_html=True)

# التصميم اللي اتفقنا عليه
st.markdown("""
    <style>
    .big-button-red { background-color: #ff4b4b; color: white !important; padding: 20px; text-align: center; border-radius: 15px; font-size: 25px; font-weight: bold; text-decoration: none; display: block; margin-bottom: 10px; }
    .big-button-green { background-color: #25d366; color: white !important; padding: 20px; text-align: center; border-radius: 15px; font-size: 25px; font-weight: bold; text-decoration: none; display: block; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ حسين عوده لجميع الأعمال الكهربائية")
st.subheader("Hussien Oda Electric Services")

# أزرار الاتصال المباشر
st.markdown('<a href="tel:01123393030" class="big-button-red">📞 اتصل الآن: 01123393030</a>', unsafe_allow_html=True)
st.markdown('<a href="https://wa.me/201123393030" class="big-button-green">💬 واتساب Hussien Oda</a>', unsafe_allow_html=True)

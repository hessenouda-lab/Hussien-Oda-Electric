import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="حسين عوده لخدمات الكهرباء", layout="centered")

# إضافة CSS لجعل الأزرار قابلة للضغط بشكل كامل في المتصفحات المقيدة
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        height: 80px;
        font-size: 25px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.write("# لجميع أعمال الكهرباء")
st.write("## Hussien Oda Electric Services")

# زر الاتصال المباشر مع خاصية التوجيه التلقائي
contact_html = """
    <div style="margin-bottom: 20px;">
        <a href="tel:01123393030" target="_self" style="text-decoration: none;">
            <div style="background-color: #ff4b4b; color: white; padding: 25px; text-align: center; border-radius: 15px; font-size: 28px; font-weight: bold; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
                📞 اتصل الآن <br> 01123393030
            </div>
        </a>
    </div>
"""
st.markdown(contact_html, unsafe_allow_html=True)

# زر الواتساب المباشر مع رابط عالمي يفتح في أي متصفح
whatsapp_html = """
    <div>
        <a href="https://wa.me/201123393030" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25d366; color: white; padding: 25px; text-align: center; border-radius: 15px; font-size: 28px; font-weight: bold; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
                💬 واتساب Hussien Oda
            </div>
        </a>
    </div>
"""
st.markdown(whatsapp_html, unsafe_allow_html=True)

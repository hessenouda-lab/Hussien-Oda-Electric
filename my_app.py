import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="حسين عوده لخدمات الكهرباء", layout="centered")

st.write("# لجميع أعمال الكهرباء")
st.write("## Hussien Oda Electric Services")

# زر الاتصال المباشر (تأكد من وجود tel: قبل الرقم)
st.markdown('''
    <a href="tel:01123393030" style="text-decoration: none;">
        <div style="background-color: #ff4b4b; color: white; padding: 20px; text-align: center; border-radius: 10px; font-size: 25px; font-weight: bold;">
            📞 اتصل الآن: <br> 01123393030
        </div>
    </a>
''', unsafe_allow_html=True)

st.write("") 

# زر الواتساب المباشر (تأكد من وجود الرابط الكامل)
st.markdown('''
    <a href="https://wa.me/201123393030" style="text-decoration: none;">
        <div style="background-color: #25d366; color: white; padding: 20px; text-align: center; border-radius: 10px; font-size: 25px; font-weight: bold;">
            💬 واتساب Hussien Oda
        </div>
    </a>
''', unsafe_allow_html=True)

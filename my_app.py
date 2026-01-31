import streamlit as stimport streamlit as st

# إعدادات الصفحة للظهور في محركات البحث
st.set_page_config(page_title="حسين عوده لخدمات الكهرباء - Hussien Oda Electric", layout="centered")

st.write("# لجميع أعمال الكهرباء")
st.write("## Hussien Oda Electric Services")

# زر الاتصال المباشر
# تم إضافة tel: قبل الرقم لتفعيل خاصية الاتصال
st.markdown(f'''
    <a href="tel:01123393030" style="text-decoration: none;">
        <div style="background-color: #ff4b4b; color: white; padding: 20px; text-align: center; border-radius: 10px; font-size: 25px; font-weight: bold;">
            📞 اتصل الآن: <br> 01123393030
        </div>
    </a>
''', unsafe_allow_html=True)

st.write("") # مسافة بين الأزرار

# زر الواتساب المباشر
# تم استخدام رابط api.whatsapp لتوجيه المستخدم للتطبيق فوراً
st.markdown(f'''
    <a href="https://api.whatsapp.com/send?phone=201123393030" style="text-decoration: none;">
        <div style="background-color: #25d366; color: white; padding: 20px; text-align: center; border-radius: 10px; font-size: 25px; font-weight: bold;">
            💬 واتساب Hussien Oda
        </div>
    </a>
''', unsafe_allow_html=True)


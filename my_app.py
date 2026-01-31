import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="centered")

# الربط بجدول البيانات
conn = st.connection("gsheets", type=GSheetsConnection)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)

# قسم إضافة تعليق
with st.form(key="comment_form", clear_on_submit=True):
    user_name = st.text_input("الأسم الكريم:")
    user_text = st.text_area("رأيك في الخدمة:")
    submit_button = st.form_submit_button("تأكيد ونشر التعليق الآن ✅")

if submit_button:
    if user_name and user_text:
        try:
            # قراءة البيانات بدون تحديد اسم الورقة (سيأخذ الأولى تلقائياً)
            df = conn.read(ttl=0)
            new_data = pd.DataFrame([{"name": user_name, "text": user_text}])
            updated_df = pd.concat([df, new_data], ignore_index=True)
            # التحديث المباشر
            conn.update(data=updated_df)
            st.success("تم النشر بنجاح!")
            st.balloons()
        except Exception as e:
            st.error(f"حدث خطأ في الاتصال. يرجى التأكد من الـ Secrets.")
    else:
        st.warning("املأ الخانات أولاً.")

# عرض التعليقات بالتنسيق الذهبي
st.markdown("---")
try:
    data = conn.read(ttl=0)
    for index, row in data.iterrows():
        # استخدام try لتجنب خطأ أسماء الأعمدة
        try:
            n = row.iloc[0] # العمود الأول (الاسم)
            t = row.iloc[1] # العمود الثاني (التعليق)
            st.markdown(f"""
            <div style="border: 8px solid #FFD700; padding: 20px; border-radius: 20px; margin-bottom: 25px; text-align: right;">
                <p style="font-size: 32px; color: #FFD700; font-weight: bold; direction: rtl;">{n}</p>
                <p style="font-size: 26px; color: white; direction: rtl;">{t}</p>
            </div>
            """, unsafe_allow_html=True)
        except:
            continue
except:
    st.info("التعليقات ستظهر هنا فور الربط.")

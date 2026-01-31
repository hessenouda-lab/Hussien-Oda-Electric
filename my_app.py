import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# إعدادات الصفحة الملكية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="centered")

# الربط بجدول بيانات جوجل
conn = st.connection("gsheets", type=GSheetsConnection)

# عنوان الموقع
st.markdown("<h1 style='text-align: center; color: #FFD700;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>قسم التعليقات والآراء</h3>", unsafe_allow_html=True)

# صندوق كتابة التعليق
with st.container():
    st.markdown("---")
    name = st.text_input("الأسم:")
    comment = st.text_area("أكتب تعليقك هنا:")
    
    if st.button("تأكيد ونشر التعليق الآن ✅"):
        if name and comment:
            try:
                # قراءة البيانات الحالية
                existing_data = conn.read(worksheet="Sheet1", usecols=[0, 1], ttl=0)
                # إضافة التعليق الجديد
                new_entry = pd.DataFrame([{"name": name, "text": comment}])
                updated_df = pd.concat([existing_data, new_entry], ignore_index=True)
                # تحديث الجدول
                conn.update(worksheet="Sheet1", data=updated_df)
                st.success("تم النشر بنجاح! شكراً لثقتك.")
                st.balloons()
            except Exception as e:
                st.error("حدث خطأ في الاتصال بالجدول. تأكد من إعدادات الـ Secrets.")
        else:
            st.warning("يرجى كتابة الاسم والتعليق أولاً.")

# عرض التعليقات السابقة
st.markdown("---")
st.markdown("<h2 style='color: #FFD700;'>آراء العملاء:</h2>", unsafe_allow_html=True)

try:
    df = conn.read(worksheet="Sheet1", ttl=0)
    for index, row in df.iterrows():
        st.markdown(f"""
        <div style="border: 5px solid #FFD700; padding: 15px; border-radius: 15px; margin-bottom: 10px; background-color: rgba(255, 215, 0, 0.1);">
            <p style="font-size: 32px; color: #FFD700; font-weight: bold; margin-bottom: 5px;">{row['name']}</p>
            <p style="font-size: 26px; color: white;">{row['text']}</p>
        </div>
        """, unsafe_allow_html=True)
except:
    st.info("كن أول من يضيف تعليقاً!")

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. إعدادات الصفحة والتصميم الملكي
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="centered")

# 2. إنشاء الاتصال بجدول البيانات
conn = st.connection("gsheets", type=GSheetsConnection)

# 3. عنوان الموقع
st.markdown("<h1 style='text-align: center; color: #FFD700;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 24px;'>أهلاً بكم في موقع المهندس حسين عوده للخدمات الكهربائية</p>", unsafe_allow_html=True)

# 4. قسم إضافة تعليق جديد
st.markdown("---")
st.markdown("<h3 style='color: #FFD700;'>أضف رأيك الخاص:</h3>", unsafe_allow_html=True)

with st.form(key="comment_form", clear_on_submit=True):
    user_name = st.text_input("الأسم الكريم:")
    user_text = st.text_area("رأيك في الخدمة:")
    submit_button = st.form_submit_button("تأكيد ونشر التعليق الآن ✅")

if submit_button:
    if user_name and user_text:
        try:
            # قراءة البيانات - نحدد اسم الورقة Sheet1
            df = conn.read(worksheet="Sheet1", ttl=0)
            # إضافة السطر الجديد
            new_data = pd.DataFrame([{"name": user_name, "text": user_text}])
            updated_df = pd.concat([df, new_data], ignore_index=True)
            # تحديث الجدول
            conn.update(worksheet="Sheet1", data=updated_df)
            st.success("تم نشر تعليقك بنجاح! شكراً لك.")
            st.balloons()
        except Exception as e:
            st.error("خطأ: يرجى التأكد أن اسم التبويب أسفل الجدول هو Sheet1 بالضبط.")
    else:
        st.warning("فضلاً، املأ جميع الخانات.")

# 5. عرض التعليقات بالتنسيق المطلوب (خط كبير، اسم ذهبي، برواز سميك)
st.markdown("---")
st.markdown("<h2 style='color: #FFD700;'>آراء العملاء:</h2>", unsafe_allow_html=True)

try:
    data = conn.read(worksheet="Sheet1", ttl=0)
    for index, row in data.iterrows():
        if pd.notna(row['name']) and pd.notna(row['text']):
            st.markdown(f"""
            <div style="border: 8px solid #FFD700; padding: 20px; border-radius: 20px; margin-bottom: 25px; background-color: rgba(0,0,0,0.2); text-align: right;">
                <p style="font-size: 32px; color: #FFD700; font-weight: bold; margin-bottom: 10px; direction: rtl;">{row['name']}</p>
                <p style="font-size: 26px; color: white; direction: rtl;">{row['text']}</p>
            </div>
            """, unsafe_allow_html=True)
except:
    st.info("التعليقات ستظهر هنا فور تفعيل الربط.")

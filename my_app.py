import streamlit as st
import pandas as pd
from shillelagh.backends.apsw.db import connect
import time

# 1. إعدادات الصفحة والظهور (SEO)
st.set_page_config(page_title="حسين عوده للكهرباء الحديثة", page_icon="⚡", layout="wide")

# 2. رابط جدول البيانات (Google Sheets) الخاص بك
SHEET_URL = "https://docs.google.com/spreadsheets/d/1z9Hb0qCyWzAykrZlPOSjb4Pup4JeAB6c-C5RmaY7_H0/edit#gid=0"

# 3. وظيفة الاتصال بالجدول وجلب البيانات
def load_data():
    conn = connect(":memory:")
    query = f'SELECT * FROM "{SHEET_URL}"'
    df = pd.read_sql(query, conn)
    return df

# 4. وظيفة إضافة تعليق جديد للجدول
def add_review(name, text):
    conn = connect(":memory:")
    cursor = conn.cursor()
    insert_query = f'INSERT INTO "{SHEET_URL}" (name, text) VALUES (?, ?)'
    cursor.execute(insert_query, (name, text))
    conn.commit()

# 5. رسالة إرشادية راقية
st.components.v1.html("""
<script>
    var isFB = /FBAN|FBAV|Messenger/i.test(navigator.userAgent);
    if (isFB) { alert("عميلنا العزيز، لضمان سهولة التواصل، يرجى اختيار 'الفتح في المتصفح' من الـ 3 نقط بالأعلى."); }
</script>
""", height=0)

# 6. التنسيق الماسي الفخم (المقاسات المعتمدة)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 15px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; display: block; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; display: block; }
    .diamond-btn {
        display: block; width: 100%; height: 85px; line-height: 85px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; 
        color: white !important; margin-bottom: 15px;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 7. أزرار التواصل
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 8. نموذج إضافة تعليق (يُحفظ في جوجل شيت)
st.markdown("<h2 style='text-align: right;'>✍️ أضف رأيك (يُحفظ تلقائياً)</h2>", unsafe_allow_html=True)

with st.form("main_feedback_form", clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    u_custom = st.text_area("رأيك في جودة العمل:")
    
    if st.form_submit_button("تأكيد ونشر التعليق ✅"):
        if u_name and u_custom:
            with st.spinner('جاري الحفظ في قاعدة البيانات...'):
                add_review(u_name, u_custom)
                st.success("تم الحفظ بنجاح!")
                time.sleep(1)
                st.rerun()
        else:
            st.warning("⚠️ يرجى كتابة الاسم والتعليق")

st.write("---")

# 9. عرض التعليقات من جدول البيانات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)

try:
    df = load_data()
    for index, row in df.iloc[::-1].iterrows(): # عرض الأحدث أولاً
        st.markdown(f"""
            <div class="review-box">
                <div class="client-name">👤 {row['name']}</div>
                <div class="client-text">{row['text']}</div>
            </div>
        """, unsafe_allow_html=True)
except:
    st.info("بانتظار أول تعليق ليتم عرضه هنا.. ✨")

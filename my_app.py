import streamlit as st
import pandas as pd
from shillelagh.backends.apsw.db import connect
import time

# 1. إعدادات الصفحة والظهور (SEO)
st.set_page_config(page_title="حسين عوده للكهرباء الحديثة", page_icon="⚡", layout="wide")

# رابط الجدول الخاص بك (المأخوذ من صورتك)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1z9Hb0qCyWzAykrZlPOSjb4Pup4JeAB6c-C5RmaY7_H0/edit#gid=0"

# 2. وظائف قاعدة البيانات
def load_data():
    conn = connect(":memory:")
    query = f'SELECT * FROM "{SHEET_URL}"'
    df = pd.read_sql(query, conn)
    return df

def add_review(name, text):
    conn = connect(":memory:")
    cursor = conn.cursor()
    insert_query = f'INSERT INTO "{SHEET_URL}" (name, text) VALUES (?, ?)'
    cursor.execute(insert_query, (name, text))
    conn.commit()

# 3. التنسيق الماسي الفخم (32px و 26px والبرواز الذهبي)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    
    /* تنسيق صندوق التعليق */
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 15px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; display: block; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; display: block; line-height: 1.4; }
    
    /* تنسيق أزرار الاتصال الضخمة */
    .diamond-btn {
        display: block; width: 100%; height: 85px; line-height: 85px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; 
        color: white !important; margin-bottom: 15px;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
    
    /* تنسيق أزرار السوشيال ميديا */
    .social-btn {
        display: inline-block; padding: 18px 35px; margin: 8px;
        border-radius: 15px; text-decoration: none !important;
        color: white !important; font-size: 22px; font-weight: bold;
    }
    .fb-bg { background-color: #1877F2; } 
    .tt-bg { background-color: #000000; border: 2px solid #fe2c55; } 
    .yt-bg { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 4. أزرار التواصل المباشر (عادت كما كانت)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 5. منصات التواصل الاجتماعي (عادت كما كانت)
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-btn fb-bg">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-btn tt-bg">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-btn yt-bg">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 6. نموذج إضافة تعليق (يُحفظ في جوجل شيت)
st.markdown("<h2 style='text-align: right;'>✍️ أضف رأيك الخاص</h2>", unsafe_allow_html=True)
with st.form("main_feedback_form", clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    u_custom = st.text_area("رأيك في جودة العمل:")
    if st.form_submit_button("تأكيد ونشر التعليق ✅"):
        if u_name and u_custom:
            add_review(u_name, u_custom)
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("⚠️ يرجى كتابة الاسم والتعليق")

st.write("---")

# 7. عرض التعليقات من جوجل شيت (بالتنسيق الفخم المعتمد)
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
try:
    df = load_data()
    for index, row in df.iloc[::-1].iterrows():
        st.markdown(f"""
            <div class="review-box">
                <div class="client-name">👤 {row['name']}</div>
                <div class="client-text">{row['text']}</div>
            </div>
        """, unsafe_allow_html=True)
except:
    st.info("بانتظار أول تعليق ليتم عرضه هنا.. ✨")

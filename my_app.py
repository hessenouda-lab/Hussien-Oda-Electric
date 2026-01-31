import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

# إعدادات الصفحة الفخمة
st.set_page_config(page_title="حسين عوده للكهرباء الحديثة", page_icon="⚡", layout="wide")

# الربط بجدول البيانات (المصداقية)
conn = st.connection("gsheets", type=GSheetsConnection)

# التنسيق الماسي (الأسماء 32px ذهبي - التعليق 26px أبيض - برواز ذهبي تخين)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; text-align: center; font-size: 50px !important; font-weight: bold; }
    h2 { color: #d4af37 !important; text-align: center; font-size: 35px !important; }
    
    /* برواز التعليق الماسي */
    .review-box { 
        background: #161a21; 
        padding: 30px; 
        border-radius: 15px; 
        border: 5px solid #d4af37; /* برواز ذهبي تخين */
        margin-bottom: 25px; 
        text-align: right;
    }
    
    /* اسم العميل (32px ذهبي) */
    .client-name { 
        color: #d4af37 !important; 
        font-size: 32px !important; 
        font-weight: bold; 
        margin-bottom: 10px;
    }
    
    /* نص التعليق (26px أبيض) */
    .client-text { 
        color: #ffffff !important; 
        font-size: 26px !important; 
        line-height: 1.6;
    }

    .diamond-btn {
        display: block; width: 100%; height: 75px; line-height: 75px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 15px; text-decoration: none !important; color: white !important;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار التواصل السريع
c1, c2 = st.columns(2)
with c1: st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا</a>', unsafe_allow_html=True)
with c2: st.markdown('<a href="https://wa.me/201123393030" class="diamond-btn green-btn">💬 واتساب</a>', unsafe_allow_html=True)

st.write("---")

# نظام إضافة التعليقات (المصداقية)
st.markdown("<h2>✍️ أضف رأيك الموثق</h2>", unsafe_allow_html=True)
with st.form("new_review", clear_on_submit=True):
    name = st.text_input("الاسم الكريم:")
    comment = st.text_area("رأيك في جودة العمل:")
    submit = st.form_submit_button("نشر التعليق الماسي ✅")
    
    if submit and name and comment:
        df = conn.read()
        new_row = pd.DataFrame([{"name": name, "text": comment}])
        updated_df = pd.concat([df, new_row], ignore_index=True)
        conn.update(data=updated_df)
        st.success("تم الحفظ في جدول البيانات بنجاح!")
        time.sleep(1)
        st.rerun()

st.write("---")
st.markdown("<h2>🌟 آراء العملاء الحقيقية</h2>", unsafe_allow_html=True)

# عرض التعليقات من الجدول أولاً
try:
    existing_data = conn.read()
    for _, row in existing_data.iloc[::-1].iterrows():
        st.markdown(f'''
            <div class="review-box">
                <div class="client-name">👤 {row["name"]}</div>
                <div class="client-text">{row["text"]}</div>
            </div>
        ''', unsafe_allow_html=True)
except:
    pass

# التعليقات الخمسة الذهبية الثابتة
initial_reviews = [
    {"n": "م/ محمد إبراهيم", "t": "تسليم في الموعد ودقة متناهية في توزيع الأحمال."},
    {"n": "أستاذ عصام", "t": "أفضل تعامل جربته في الطالبية، احترافية وأمان."},
    {"n": "الحاج محمود", "t": "شغل هندسي بجد، الله يبارك لك في رزقك يا حسين."},
    {"n": "د/ مروة", "t": "شكراً جزيلاً على الأمانة في اختيار الخامات والدقة."},
    {"n": "أحمد سمير", "t": "تأسيس ممتاز للشقة بالكامل وبأحدث الطرق الهندسية."}
]

for r in initial_reviews:
    st.markdown(f'''
        <div class="review-box">
            <div class="client-name">👤 {r["n"]}</div>
            <div class="client-text">{r["t"]}</div>
        </div>
    ''', unsafe_allow_html=True)

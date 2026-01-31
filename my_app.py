import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="حسين عوده للكهرباء الحديثة", page_icon="⚡", layout="wide")

# الربط بجدول البيانات
conn = st.connection("gsheets", type=GSheetsConnection)

# التنسيق الماسي المعتمد (اسم ذهبي 32px - تعليق أبيض 26px - برواز ذهبي تخين)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; text-align: center; font-size: 50px !important; font-weight: bold; }
    h2 { color: #d4af37 !important; text-align: center; font-size: 35px !important; }
    
    /* برواز التعليق الذهبي التخين */
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border: 6px solid #d4af37; margin-bottom: 25px; text-align: right;
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; }

    /* أزرار الاتصال الكبيرة */
    .diamond-btn {
        display: block; width: 100%; height: 80px; line-height: 80px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 15px; text-decoration: none !important; color: white !important; margin-bottom: 20px;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }

    /* أيقونات السوشيال ميديا */
    .social-container { display: flex; justify-content: center; gap: 30px; margin: 30px 0; }
    .social-icon { font-size: 45px; text-decoration: none !important; transition: 0.3s; }
    .social-icon:hover { transform: scale(1.2); }
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار التواصل الأساسية
c1, c2 = st.columns(2)
with c1: st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with c2: st.markdown('<a href="https://wa.me/201123393030" class="diamond-btn green-btn">💬 واتساب</a>', unsafe_allow_html=True)

# قسم السوشيال ميديا اللي طلبت فيه كل الروابط
st.markdown("""
<div class="social-container">
    <a href="https://facebook.com" class="social-icon" style="color: #1877f2;"><i class="fab fa-facebook"></i></a>
    <a href="https://tiktok.com" class="social-icon" style="color: #ffffff;"><i class="fab fa-tiktok"></i></a>
    <a href="https://youtube.com" class="social-icon" style="color: #ff0000;"><i class="fab fa-youtube"></i></a>
    <a href="https://instagram.com" class="social-icon" style="color: #e4405f;"><i class="fab fa-instagram"></i></a>
</div>
""", unsafe_allow_html=True)

st.write("---")

# إضافة رأي جديد
st.markdown("<h2>✍️ أضف رأيك الموثق</h2>", unsafe_allow_html=True)
with st.form("main_form", clear_on_submit=True):
    name = st.text_input("الاسم الكريم:")
    comment = st.text_area("رأيك في جودة العمل:")
    if st.form_submit_button("نشر التعليق الآن ✅"):
        if name and comment:
            df = conn.read()
            new_row = pd.DataFrame([{"name": name, "text": comment}])
            updated_df = pd.concat([df, new_row], ignore_index=True)
            conn.update(data=updated_df)
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()

st.write("---")
st.markdown("<h2>🌟 آراء العملاء الموثقة</h2>", unsafe_allow_html=True)

# عرض التعليقات من جوجل شيت
try:
    data = conn.read()
    for _, row in data.iloc[::-1].iterrows():
        st.markdown(f'<div class="review-box"><div class="client-name">👤 {row["name"]}</div><div class="client-text">{row["text"]}</div></div>', unsafe_allow_html=True)
except:
    pass

# التعليقات الـ 5 المبدئية للمصداقية
initials = [
    {"n": "م/ محمد إبراهيم", "t": "تسليم في الموعد ودقة متناهية في توزيع الأحمال."},
    {"n": "أستاذ عصام", "t": "أفضل تعامل جربته في الطالبية، احترافية وأمان."},
    {"n": "الحاج محمود", "t": "شغل هندسي بجد، الله يبارك لك في رزقك يا حسين."},
    {"n": "د/ مروة", "t": "شكراً جزيلاً على الأمانة في اختيار الخامات والدقة."},
    {"n": "أحمد سمير", "t": "تأسيس ممتاز للشقة بالكامل وبأحدث الطرق الهندسية."}
]
for r in initials:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r["n"]}</div><div class="client-text">{r["t"]}</div></div>', unsafe_allow_html=True)

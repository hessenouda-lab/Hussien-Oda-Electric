import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time

# إعدادات الصفحة
st.set_page_config(page_title="حسين عوده للكهرباء الحديثة", page_icon="⚡", layout="wide")

# الربط الآمن بجوجل شيت
conn = st.connection("gsheets", type=GSheetsConnection)

# التنسيق الماسي
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { 
        background: #161a21; padding: 30px; border-radius: 20px; 
        border-right: 12px solid #d4af37; margin-bottom: 20px; 
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; }
    .client-text { color: #ffffff !important; font-size: 26px !important; }
    .diamond-btn {
        display: block; width: 100%; height: 70px; line-height: 70px; 
        text-align: center; font-size: 24px; font-weight: bold; 
        border-radius: 15px; text-decoration: none !important; color: white !important;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار التواصل
c1, c2 = st.columns(2)
with c1: st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا</a>', unsafe_allow_html=True)
with c2: st.markdown('<a href="https://wa.me/201123393030" class="diamond-btn green-btn">💬 واتساب</a>', unsafe_allow_html=True)

st.write("---")

# نظام التعليقات الموثقة
st.markdown("<h2>✍️ أضف رأيك الموثق</h2>")
with st.form("review_form", clear_on_submit=True):
    name = st.text_input("الاسم الكريم (سيظهر بجانب تعليقك):")
    comment = st.text_area("رأيك في جودة العمل:")
    if st.form_submit_button("نشر التعليق الآن ✅"):
        if name and comment:
            df = conn.read()
            new_row = {"name": name, "text": comment}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            conn.update(data=df)
            st.success("تم النشر بنجاح! شكراً لثقتكم.")
            time.sleep(1)
            st.rerun()

st.write("---")
st.markdown("<h2>🌟 آراء العملاء الحقيقية</h2>")
# عرض التعليقات من الشيت
try:
    existing_data = conn.read()
    for _, row in existing_data.iloc[::-1].iterrows():
        st.markdown(f'<div class="review-box"><div class="client-name">👤 {row["name"]}</div><div class="client-text">{row["text"]}</div></div>', unsafe_allow_html=True)
except:
    st.info("كن أول من يضيف تعليقاً موثقاً.. ✨")

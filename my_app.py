import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

# 1. الإعدادات والظهور
st.set_page_config(page_title="حسين عوده للكهرباء الحديثة", page_icon="⚡", layout="wide")

# 2. الربط مع جوجل شيت (اللمسة الأخيرة اللي عملناها)
conn = st.connection("gsheets", type=GSheetsConnection)

# 3. رسالة التنبيه لعملاء الماسنجر
st.components.v1.html("""
<script>
    var isFB = /FBAN|FBAV|Messenger/i.test(navigator.userAgent);
    if (isFB) { alert("عميلنا العزيز، لضمان عمل أزرار الاتصال بشكل صحيح، يرجى اختيار 'الفتح في المتصفح' من الـ 3 نقط بالأعلى."); }
</script>
""", height=0)

# 4. التنسيق الذهبي المعتمد (الأسماء 32px والتعليق 26px)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border: 3px solid #d4af37; margin-bottom: 25px; 
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; display: block; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; display: block; }
    .diamond-btn {
        display: block; width: 100%; height: 80px; line-height: 80px; 
        text-align: center; font-size: 26px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; color: white !important; margin-bottom: 15px;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار التواصل
col1, col2 = st.columns(2)
with col1: st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2: st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 5. نظام التعليقات بالاختيارات الجاهزة والربط بالجدول
st.markdown("<h2 style='text-align: right;'>✍️ شاركنا رأيك الموثق</h2>", unsafe_allow_html=True)
with st.form("diamond_form", clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    u_quick = st.selectbox("اختر رأياً جاهزاً:", ["لم يتم الاختيار...", "شغل ممتاز وتسليم في الموعد.", "دقة واحترافية عالية.", "تأسيس هندسي محترم جداً."])
    u_custom = st.text_area("أو اكتب رأيك الخاص:")
    
    if st.form_submit_button("نشر التعليق الآن ✅"):
        final_text = u_custom.strip() if u_custom.strip() else (u_quick if u_quick != "لم يتم الاختيار..." else "")
        if u_name and final_text:
            # حفظ في جوجل شيت
            df = conn.read()
            new_data = pd.DataFrame([{"name": u_name, "text": final_text}])
            updated_df = pd.concat([df, new_data], ignore_index=True)
            conn.update(data=updated_df)
            st.success("تم النشر بنجاح! شكراً لثقتكم.")
            time.sleep(1)
            st.rerun()

st.write("---")
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)

# عرض التعليقات (من الجدول + الخمسة المبدئية للمصداقية)
try:
    data = conn.read()
    for _, row in data.iloc[::-1].iterrows():
        st.markdown(f'<div class="review-box"><div class="client-name">👤 {row["name"]}</div><div class="client-text">{row["text"]}</div></div>', unsafe_allow_html=True)
except:
    pass

# التعليقات الخمسة المبدئية (للمصداقية الدائمة)
initials = [
    {"n": "م/ محمد إبراهيم", "t": "تسليم في الموعد ودقة متناهية في توزيع الأحمال."},
    {"n": "أستاذ عصام", "t": "أفضل تعامل جربته في الطالبية، احترافية وأمان."},
    {"n": "الحاج محمود", "t": "شغل هندسي بجد، الله يبارك لك في رزقك يا حسين."},
    {"n": "د/ مروة", "t": "شكراً جزيلاً على الأمانة في اختيار الخامات والدقة."},
    {"n": "أحمد سمير", "t": "تأسيس ممتاز للشقة بالكامل وبأحدث الطرق الهندسية."}
]
for r in initials:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r["n"]}</div><div class="client-text">{r["t"]}</div></div>', unsafe_allow_html=True)

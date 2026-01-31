import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. رسالة إرشادية راقية لعملاء الماسنجر
st.components.v1.html("""
<script>
    var isFB = /FBAN|FBAV|Messenger/i.test(navigator.userAgent);
    if (isFB) {
        alert("عميلنا العزيز، لضمان سهولة التواصل معنا، يرجى الضغط على الثلاث نقاط في أعلى الشاشة واختيار 'الفتح في المتصفح' (Open in Browser).");
    }
</script>
""", height=0)

# 3. تهيئة البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."}]

# 4. نافذة التأكيد (المودال الذهبي المعتمد)
@st.dialog("مراجعة رأيك قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1a1e24; padding: 25px; border-radius: 15px; border: 3px solid #d4af37; text-align: right; color: white;">
            <p style="color: #d4af37; font-weight: bold; font-size: 32px; margin-bottom: 10px;">👤 الاسم: {name}</p>
            <div style="border-top: 2px solid #d4af37; padding-top: 15px;">
                <p style="font-size: 26px; color: #ffffff; line-height: 1.6;">💬 الرأي: "{text}"</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("تأكيد ونشر التعليق الآن ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})

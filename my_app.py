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
        st.success("تم النشر بنجاح! شكراً لثقتكم.")
        time.sleep(1)
        st.rerun()

# 5. التنسيق الماسي الفخم (تم إصلاح قفلة الـ CSS هنا)
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
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; display: block; line-height: 1.4; }
    
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

# 6. أزرار التواصل
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 7. عرض التعليقات (بالتنسيق الضخم المعتمد)
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f"""
        <div class="review-box">
            <div class="client-name">👤 {r.get('name')}</div>
            <div class="client-text">{r.get('text')}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 8. نموذج التعليق المطور مع خيارات سريعة
st.markdown("<h2 style='text-align: right;'>✍️ أضف رأيك الخاص</h2>", unsafe_allow_html=True)

with st.form("diamond_feedback_v13", clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    
    st.markdown("<p style='color: #d4af37; text-align: right; font-weight: bold;'>اختر رأياً جاهزاً (اختياري):</p>", unsafe_allow_html=True)
    quick_options = [
        "لم يتم الاختيار...",
        "شغل ممتاز وتسليم في الموعد المحدد. شكراً جزيلاً.",
        "دقة في المواعيد واحترافية عالية في التنفيذ.",
        "أفضل فني كهرباء تعاملت معه، ذوق وأدب وشغل نظيف.",
        "خامات ممتازة وتأسيس هندسي على أعلى مستوى."
    ]
    u_quick = st.selectbox("اضغط هنا لاختيار جملة جاهزة:", quick_options)
    
    u_custom = st.text_area("أو اكتب رأيك الخاص بالتفصيل:")
    
    submit = st.form_submit_button("عرض التعليق للتأكيد ✨")
    
    if submit:
        # تحديد النص النهائي
        final_text = u_custom.strip() if u_custom.strip() else (u_quick if u_quick != "لم يتم الاختيار..." else "")
            
        if u_name and final_text:
            confirm_dialog(u_name, final_text)
        else:
            st.warning("⚠️ يرجى كتابة الاسم وتحديد الرأي المطلوب")

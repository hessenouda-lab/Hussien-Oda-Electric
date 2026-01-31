import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات (لحفظ التعليقات)
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد (التي تظهر في وسط الشاشة)
@st.dialog("تأكيد نشر رأيك ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #121212; padding: 20px; border-radius: 10px; border: 2px solid #d4af37; text-align: right;">
            <p style="color: #d4af37; font-size: 18px; font-weight: bold;">👤 اسم العميل: {name}</p>
            <p style="color: #ffffff; font-size: 20px;">💬 الرأي: {text}</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("تأكيد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.success("تم النشر بنجاح!")
        time.sleep(1)
        st.rerun()

# 4. التنسيق الفخم (الأسود والذهبي والخط الكبير)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; font-size: 45px !important; text-align: center; }
    h2 { color: #d4af37 !important; font-size: 35px !important; text-align: center; }
    .review-box { 
        background: #161a21; padding: 25px; border-radius: 20px; 
        border-right: 10px solid #d4af37; margin-bottom: 20px;
    }
    .client-name { color: #d4af37; font-size: 26px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 22px; margin-top: 10px; }
    label { font-size: 20px !important; color: #d4af37 !important; }
    
    /* تنسيق أزرار الاتصال لتكون ضخمة */
    div.stButton > button {
        height: 80px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
    }
    /* زر الاتصال أحمر */
    div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
    /* زر الواتساب أخضر */
    div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (التي تعمل من داخل الماسنجر)
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html("""<script>window.location.href = "tel:01123393030";</script>""", height=0)
with col2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html("""<script>window.open("https://api.whatsapp.com/send?phone=201123393030", "_blank");</script>""", height=0)

st.write("---")

# 6. عرض التعليقات السابقة
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f"""
        <div class="review-box">
            <div class="client-name">👤 {r.get('name')}</div>
            <div class="client-text">{r.get('text')}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 7. فورم إضافة التعليق (مع التعليقات الجاهزة)
st.markdown("### ✍️ أضف تقييمك بضغطة واحدة")
with st.form("complete_form", clear_on_submit=True):
    u_name = st.text_input("اسم العميل بالكامل:")
    
    # قرارات جاهزة يختار منها العميل
    options = [
        "اختر تقييماً جاهزاً...",
        "شغل احترافي وتسليم في الموعد ⚡",
        "أمانة ودقة في المواعيد والخامات ✅",
        "تأسيس كهرباء ممتاز، أنصح بالتعامل معه ⭐",
        "رجل محترم جداً وفاهم شغله بالتفصيل 👌"
    ]
    selected_option = st.selectbox("اختر من هذه الآراء الشائعة:", options)
    u_text_custom = st.text_area("أو اكتب رأيك الخاص هنا:")
    
    if st.form_submit_button("إرسال للمراجعة والاعتماد ✨"):
        final_text = u_text_custom if u_text_custom else (selected_option if selected_option != options[0] else "")
        if u_name and final_text:
            confirm_dialog(u_name, final_text)
        else:
            st.warning("⚠️ نرجو كتابة الاسم واختيار أو كتابة التعليق")

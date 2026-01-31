import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات الأساسية
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد المنبثقة
@st.dialog("تأكيد نشر رأيك ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #121212; padding: 25px; border-radius: 15px; border: 3px solid #d4af37; text-align: right;">
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-bottom: 5px;">👤 اسم العميل:</p>
            <p style="color: #ffffff; font-size: 24px; font-weight: bold; margin-bottom: 20px; background: #1a1a1a; padding: 10px; border-radius: 8px;">{name}</p>
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-bottom: 5px;">💬 الرأي المختار:</p>
            <p style="color: #ffffff; font-size: 22px; line-height: 1.6; background: #1a1a1a; padding: 10px; border-radius: 8px;">{text}</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("تأكيد ونشر ✅", use_container_width=True, type="primary"):
            st.session_state.reviews.insert(0, {"name": name, "text": text})
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()
    with c2:
        if st.button("تعديل ✏️", use_container_width=True):
            st.rerun()

# 4. تصميم الواجهة (الألوان والخطوط الكبيرة)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; font-size: 45px !important; text-align: center; }
    h2 { color: #d4af37 !important; font-size: 35px !important; text-align: center; }
    .review-box { 
        background: #161a21; padding: 30px; border-radius: 20px; 
        border-right: 10px solid #d4af37; margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37; font-size: 28px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 24px; margin-top: 15px; line-height: 1.5; }
    label { font-size: 22px !important; color: #d4af37 !important; font-weight: bold !important; }
    div.stButton > button { height: 65px !important; font-size: 22px !important; font-weight: bold !important; border-radius: 15px !important; }
    input, textarea, .stSelectbox { background-color: #1c2129 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال الذكية (روابط مباشرة ومختصرة لضمان العمل من الماسنجر)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" target="_blank" style="text-decoration:none;"><div style="background: #ff4b4b; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:24px; box-shadow: 0 4px 15px rgba(255,75,75,0.4);">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" style="text-decoration:none;"><div style="background: #25d366; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:24px; box-shadow: 0 4px 15px rgba(37,211,102,0.4);">💬 راسلنا واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 6. عرض التعليقات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

st.write("---")

# 7. فورم إضافة التعليق (الذكية)
st.markdown("### ✍️ أضف تقييمك بضغطة واحدة")
with st.form("hussien_final_fix_form", clear_on_submit=True):
    u_name = st.text_input("اسم العميل بالكامل:")
    options = ["اختر رأياً جاهزاً...", "شغل احترافي وتسليم في الموعد ⚡", "أمانة ودقة في المواعيد والخامات ✅", "تأسيس كهرباء ممتاز، أنصح بالتعامل معه ⭐", "رجل محترم جداً وفاهم شغله بالتفصيل 👌"]
    selected_option = st.selectbox("اختر من هذه الآراء:", options)
    u_text_custom = st.text_area("أو اكتب رأيك الخاص هنا:")
    
    if st.form_submit_button("إرسال للمراجعة ✨"):
        final_text = u_text_custom if u_text_custom else (selected_option if selected_option != options[0] else "")
        if u_name and final_text:
            confirm_dialog(u_name, final_text)
        else:
            st.warning("⚠️ نرجو كتابة الاسم واختيار أو كتابة التعليق")

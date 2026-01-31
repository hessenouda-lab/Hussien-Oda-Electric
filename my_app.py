import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد
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
    if st.button("تأكيد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.success("تم النشر بنجاح!")
        time.sleep(1)
        st.rerun()

# 4. التنسيق (الفخامة والخطوط الكبيرة)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1 { color: #d4af37 !important; font-size: 45px !important; text-align: center; }
    h2 { color: #d4af37 !important; font-size: 35px !important; text-align: center; }
    .review-box { 
        background: #161a21; padding: 30px; border-radius: 20px; 
        border-right: 10px solid #d4af37; margin-bottom: 25px;
    }
    .client-name { color: #d4af37; font-size: 28px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 24px; margin-top: 15px; }
    label { font-size: 22px !important; color: #d4af37 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (حل نهائي لإجبار الماسنجر)
col1, col2 = st.columns(2)
with col1:
    # استخدام رابط tel المباشر مع تنسيق HTML قوي
    st.markdown('''
        <a href="tel:01123393030" style="text-decoration:none;">
            <div style="background: #ff4b4b; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:26px; box-shadow: 0 4px 15px rgba(255,75,75,0.4);">
                📞 اتصل بنا الآن
            </div>
        </a>
    ''', unsafe_allow_html=True)

with col2:
    # استخدام رابط WhatsApp API الرسمي اللي بيجبر التطبيق يفتح
    st.markdown('''
        <a href="https://api.whatsapp.com/send?phone=201123393030" target="_blank" style="text-decoration:none;">
            <div style="background: #25d366; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:26px; box-shadow: 0 4px 15px rgba(37,211,102,0.4);">
                💬 راسلنا واتساب
            </div>
        </a>
    ''', unsafe_allow_html=True)

st.write("---")

# 6. التقييمات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r.get("name")}</div><div class="client-text">{r.get("text")}</div></div>', unsafe_allow_html=True)

st.write("---")

# 7. الفورم الذكية
st.markdown("### ✍️ أضف تقييمك بضغطة واحدة")
with st.form("final_pro_form", clear_on_submit=True):
    u_name = st.text_input("اسم العميل بالكامل:")
    options = ["اختر رأياً جاهزاً...", "شغل احترافي وتسليم في الموعد ⚡", "أمانة ودقة في المواعيد ✅", "تأسيس كهرباء ممتاز ⭐"]
    selected_option = st.selectbox("اختر من هذه الآراء:", options)
    u_text_custom = st.text_area("أو اكتب رأيك الخاص هنا:")
    if st.form_submit_button("إرسال للمراجعة ✨"):
        final_text = u_text_custom if u_text_custom else (selected_option if selected_option != options[0] else "")
        if u_name and final_text:
            confirm_dialog(u_name, final_text)
        else:
            st.warning("⚠️ نرجو كتابة الاسم والتعليق")

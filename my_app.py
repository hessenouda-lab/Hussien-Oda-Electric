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

# 3. نافذة التأكيد المنبثقة (تصميم مريح للعين وكبار السن)
@st.dialog("تأكيد نشر رأيك ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #121212; padding: 25px; border-radius: 15px; border: 3px solid #d4af37; text-align: right;">
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-bottom: 5px;">👤 اسم العميل:</p>
            <p style="color: #ffffff; font-size: 24px; font-weight: bold; margin-bottom: 20px; background: #1a1a1a; padding: 10px; border-radius: 8px;">{name}</p>
            <p style="color: #d4af37; font-size: 20px; font-weight: bold; margin-bottom: 5px;">💬 تفاصيل الرأي:</p>
            <p style="color: #ffffff; font-size: 22px; line-height: 1.6; background: #1a1a1a; padding: 10px; border-radius: 8px;">{text}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        # زرار أخضر واضح جداً للتأكيد
        if st.button("نشر التعليق الآن ✅", use_container_width=True, type="primary"):
            st.session_state.reviews.insert(0, {"name": name, "text": text})
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()
    with c2:
        # زرار رمادي واضح للتعديل
        if st.button("رجوع لتغيير الكلام ✏️", use_container_width=True):
            st.rerun()

# 4. تصميم الواجهة (CSS الفخامة والوضوح)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    
    /* تكبير عناوين الموقع */
    h1 { color: #d4af37 !important; font-size: 45px !important; text-align: center; }
    h2 { color: #d4af37 !important; font-size: 35px !important; text-align: center; }
    
    /* صناديق التعليقات (خطوط كبيرة وواضحة) */
    .review-box { 
        background: #161a21;
        padding: 30px; 
        border-radius: 20px; 
        border-right: 10px solid #d4af37; 
        margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .client-name { color: #d4af37; font-size: 28px; font-weight: bold; }
    .client-text { color: #ffffff; font-size: 24px; margin-top: 15px; line-height: 1.5; }

    /* تكبير خطوط الفورم (المدخلات) */
    label { font-size: 22px !important; color: #d4af37 !important; font-weight: bold !important; }
    input, textarea { font-size: 20px !important; background-color: #1c2129 !important; color: white !important; }

    /* أزرار السيستم الضخمة */
    div.stButton > button {
        height: 65px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال (ألوان نيون قوية)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background: #ff4b4b; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:24px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background: #25d366; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:24px;">💬 راسلنا واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 6. عرض التعليقات (بخطوط كبيرة)
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'''
        <div class="review-box">
            <div class="client-name">👤 {r.get("name")}</div>
            <div class="client-text">{r.get("text")}</div>
        </div>
    ''', unsafe_allow_html=True)

st.write("---")

# 7. فورم إضافة التعليق (مسميات واضحة)
st.markdown("### ✍️ يسعدنا تقييمك لخدمتنا")
with st.form("hussien_final_form", clear_on_submit=True):
    u_name = st.text_input("اسم العميل بالكامل:")
    u_text = st.text_area("ما هو رأيك في الخدمة التي قدمناها لك؟")
    
    if st.form_submit_button("إرسال للمراجعة والاعتماد ✨"):
        if u_name and u_text:
            confirm_dialog(u_name, u_text)
        else:
            st.warning("⚠️ نرجو كتابة الاسم والتعليق بوضوح أولاً")

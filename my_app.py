import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تهيئة البيانات وحل مشاكل KeyError السابقة
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "تأسيس كهرباء على أعلى مستوى."},
        {"name": "محمد صلاح", "text": "رجل محترف ومواعيده دقيقة جداً."}
    ]

# 3. نافذة التأكيد المنبثقة (بستايل فخم شبابي)
@st.dialog("مراجعة بيانات التعليق ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #121212; padding: 25px; border-radius: 15px; border: 2px solid #d4af37; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <p style="color: #d4af37; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">المرسل:</p>
            <p style="color: #ffffff; font-size: 20px; font-weight: bold; margin-bottom: 20px;">{name}</p>
            <p style="color: #d4af37; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">نص الرأي:</p>
            <p style="color: #e0e0e0; font-size: 17px; line-height: 1.6; font-style: italic;">"{text}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("اعتماد ونشر ✅", use_container_width=True):
            st.session_state.reviews.insert(0, {"name": name, "text": text})
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()
    with c2:
        if st.button("تعديل ✏️", use_container_width=True):
            st.rerun()

# 4. تصميم الواجهة (CSS الفخامة)
st.markdown("""
    <style>
    /* الخلفية الأساسية */
    .stApp { background-color: #0b0d11; }
    
    /* العناوين */
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: 800 !important; letter-spacing: -1px; }
    
    /* صناديق التعليقات (ستايل شبابي فخم) */
    .review-box { 
        background: linear-gradient(145deg, #161a21, #0f1218);
        padding: 25px; 
        border-radius: 20px; 
        border-left: 8px solid #d4af37; 
        margin-bottom: 20px; 
        box-shadow: 10px 10px 20px #080a0d, -10px -10px 20px #14181f;
    }
    
    /* أزرار الاتصال (تأثير النيون الخافت) */
    .btn-call { background: linear-gradient(90deg, #b91d1d, #ef4444); color: white; padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; font-size: 20px; box-shadow: 0 4px 20px rgba(239,68,68,0.2); transition: 0.3s; }
    .btn-wa { background: linear-gradient(90deg, #15803d, #22c55e); color: white; padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; font-size: 20px; box-shadow: 0 4px 20px rgba(34,197,94,0.2); transition: 0.3s; }
    
    /* أزرار السيستم */
    div.stButton > button {
        background-color: #d4af37 !important;
        color: #000 !important;
        border-radius: 12px !important;
        height: 55px;
        font-weight: 900 !important;
        border: none !important;
    }
    
    /* الحقول */
    input, textarea { background-color: #161a21 !important; color: white !important; border: 1px solid #2d343f !important; border-radius: 10px !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء والخدمات الحديثة</h1>", unsafe_allow_html=True)

# 5. الاتصال السريع (تعديل الروابط لمنع أخطاء الصور)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div class="btn-call">📞 اتصال هاتفي مباشر</div></a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div class="btn-wa">💬 محادثة واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 6. عرض التعليقات
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'''
        <div class="review-box">
            <div style="color: #d4af37; font-size: 14px; font-weight: bold; margin-bottom: 8px;">عميلنا العزيز:</div>
            <div style="color: #ffffff; font-size: 22px; font-weight: 700;">{r.get("name")}</div>
            <div style="color: #a0a0a0; margin-top: 12px; font-size: 18px; line-height: 1.5;">{r.get("text")}</div>
        </div>
    ''', unsafe_allow_html=True)

st.write("---")

# 7. فورم إضافة التعليق (تعديل المسميات)
st.markdown("### ✍️ أضف تقييمك وتجربتك معنا")
with st.form("pro_feedback_form", clear_on_submit=True):
    u_name = st.text_input("اسم العميل:")
    u_text = st.text_area("تفاصيل رأيك في الخدمة:")
    
    if st.form_submit_button("إرسال للمراجعة والاعتماد ✨"):
        if u_name and u_text:
            confirm_dialog(u_name, u_text)
        else:
            st.warning("⚠️ نرجو كتابة الاسم والتعليق أولاً")

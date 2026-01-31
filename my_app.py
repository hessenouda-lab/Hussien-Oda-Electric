import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات الأساسية
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "أحمد علي", "text": "شغل ممتاز وتأسيس احترافي."},
        {"name": "محمد صلاح", "text": "رجل محترم وأمين جداً في الخامات."}
    ]

# 3. وظيفة رسالة التأكيد المنبثقة (بألوان محسنة)
@st.dialog("مراجعة التعليق قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1c1f26; padding: 20px; border-radius: 15px; border: 1px solid #ffde59;">
            <p style="color: #ffde59; font-size: 18px; font-weight: bold; margin-bottom: 5px;">👤 الاسم:</p>
            <p style="color: white; font-size: 16px; margin-bottom: 15px;">{name}</p>
            <p style="color: #ffde59; font-size: 18px; font-weight: bold; margin-bottom: 5px;">💬 رأيك:</p>
            <p style="color: white; font-size: 16px; line-height: 1.6;">{text}</p>
        </div>
        <div style="margin-top: 20px; text-align: center;">
            <p style="color: #ccc; font-size: 14px;">هل تريد اعتماد هذا الكلام ونشره على الموقع؟</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_ok, col_edit = st.columns(2)
    with col_ok:
        if st.button("تأكيد ونشر ✅", use_container_width=True):
            st.session_state.reviews.insert(0, {"name": name, "text": text})
            st.success("تم النشر بنجاح!")
            time.sleep(1)
            st.rerun()
    with col_edit:
        if st.button("تعديل ✏️", use_container_width=True):
            st.rerun()

# 4. تصميم الواجهة بالكامل (CSS)
st.markdown("""
    <style>
    /* خلفية الموقع */
    .stApp { background-color: #0e1117; }
    
    /* العناوين */
    h1, h2 { color: #ffde59 !important; text-align: center; font-family: 'Arial'; }
    
    /* صناديق التعليقات */
    .review-box { 
        background-color: #1c1f26; 
        padding: 20px; 
        border-radius: 12px; 
        border-right: 6px solid #ffde59; 
        margin-bottom: 15px; 
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    
    /* أزرار Streamlit */
    div.stButton > button {
        background-color: #ffde59 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 50px;
        border: none !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        background-color: #fff !important;
    }
    
    /* تنسيق المدخلات */
    .stTextInput input, .stTextArea textarea {
        background-color: #1c1f26 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء</h1>", unsafe_allow_html=True)

# 5. أزرار الاتصال السريع
c1, c2 = st.columns(2)
with c1:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background: linear-gradient(90deg, #ff4b4b, #ff6b6b); color:white; padding:18px; border-radius:15px; text-align:center; font-weight:bold; font-size:20px; box-shadow: 0 4px 15px rgba(255,75,75,0.3);">📞 اتصال مباشر</div></a>', unsafe_allow_html=True)
with c2:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background: linear-gradient(90deg, #25d366, #2efd77); color:white; padding:18px; border-radius:15px; text-align:center; font-weight:bold; font-size:20px; box-shadow: 0 4px 15px rgba(37,211,102,0.3);">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# 6. عرض التعليقات
st.markdown("<h2>💬 ما يقوله زبائننا</h2>", unsafe_allow_html=True)
for r in st.session_state.reviews:
    st.markdown(f'''
        <div class="review-box">
            <span style="color: #ffde59; font-weight: bold; font-size: 18px;">{r.get("name")}</span><br>
            <p style="color: white; margin-top: 10px;">{r.get("text")}</p>
        </div>
    ''', unsafe_allow_html=True)

st.write("---")

# 7. إضافة تعليق جديد
st.markdown("### 📝 أضف تقييمك للخدمة")
with st.form("hussien_pro_form", clear_on_submit=True):
    u_name = st.text_input("اسمك الموقر:")
    u_text = st.text_area("رسالتك لنا:")
    submit = st.form_submit_button("إرسال للمراجعة ✨")
    
    if submit:
        if u_name and u_text:
            confirm_dialog(u_name, u_text)
        else:
            st.warning("⚠️ من فضلك املأ جميع الخانات")

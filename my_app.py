import streamlit as st
import time
import uuid

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# بصمة الجهاز الفريدة
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# قائمة التعليقات الأساسية
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "1", "user_id": "admin", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد.", "time": time.time() - 600},
        {"id": "2", "user_id": "admin", "name": "أحمد علي", "text": "رجل محترم وأمين جداً.", "time": time.time() - 600}
    ]

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: white !important; font-size: 20px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    .stButton>button {
        background-color: #ffde59 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء</h1>", unsafe_allow_html=True)

# أزرار التواصل
col1, col2 = st.columns(2)
with col1: st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:15px; border-radius:50px; text-align:center; font-size:20px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with col2: st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; border-radius:50px; text-align:center; font-size:20px; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")
st.markdown("<h2>🎬 كواليس العمل</h2>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
with v2: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.write("---")
st.markdown("<h2>⭐ آراء العملاء</h2>", unsafe_allow_html=True)

# عرض التعليقات مع حماية من الخطأ اللي ظهر في الصورة
for i, review in enumerate(st.session_state.reviews):
    # التأكد من وجود المفاتيح قبل المقارنة لمنع KeyError
    user_id_in_review = review.get('user_id', 'unknown')
    review_time = review.get('time', 0)
    
    is_owner = user_id_in_review == st.session_state.user_id
    can_edit = is_owner and (time.time() - review_time) < 300 # 5 دقائق
    
    st.markdown(f'<div class="review-box"><b>{review.get("name", "عميل")}:</b> {review.get("text", "")}</div>', unsafe_allow_html=True)
    
    if can_edit:
        ce1, ce2, ce3 = st.columns([1, 1, 4])
        with ce1:
            if st.button("تعديل 📝", key=f"e_{review.get('id', i)}"):
                st.session_state.edit_id = review.get('id')
        with ce2:
            if st.button("حذف 🗑️", key=f"d_{review.get('id', i)}"):
                st.session_state.reviews.pop(i)
                st.rerun()

st.write("---")

# منطقة الإضافة أو التعديل
if 'edit_id' in st.session_state:
    st.markdown("### 📝 تعديل تعليقك")
    idx = next((i for i, r in enumerate(st.session_state.reviews) if r['id'] == st.session_state.edit_id), None)
    if idx is not None:
        new_txt = st.text_area("الكلام الجديد:", value=st.session_state.reviews[idx]['text'])
        if st.button("حفظ التعديل ✅"):
            st.session_state.reviews[idx]['text'] = new_txt
            st.session_state.reviews[idx]['time'] = time.time() # تصفير الـ 5 دقائق
            del st.session_state.edit_id
            st.rerun()
else:
    st.markdown("### 📝 اكتب تعليقك")
    with st.form(key='review_f', clear_on_submit=True):
        u_name = st.text_input("الاسم الكريم:")
        u_choice = st.selectbox("ر

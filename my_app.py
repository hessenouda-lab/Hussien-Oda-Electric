import streamlit as st
import time
import uuid

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# إنشاء معرف فريد لجهاز المستخدم (عشان الموقع يعرف إن ده تعليقك أنت)
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# قائمة التعليقات في الذاكرة
if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "1", "user_id": "admin", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد.", "time": time.time() - 600},
        {"id": "2", "user_id": "admin", "name": "أحمد علي", "text": "رجل محترم وأمين جداً.", "time": time.time() - 600}
    ]

# CSS التصميم
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .review-box { background-color: #1c1f26; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; }
    .my-review { border: 2px solid #ffde59 !important; }
    .stButton>button { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ حسين عوده لخدمات الكهرباء")

# عرض التعليقات مع ميزة التعديل والحذف
st.header("⭐ آراء العملاء")
for i, review in enumerate(st.session_state.reviews):
    is_owner = review['user_id'] == st.session_state.user_id
    time_passed = (time.time() - review['time']) / 60  # بالدقائق
    
    # تحديد إذا كان التعليق خاص بي وهل لسه مكملش 5 دقائق
    can_edit = is_owner and time_passed < 5
    
    box_class = "review-box my-review" if is_owner else "review-box"
    
    with st.container():
        st.markdown(f'<div class="{box_class}"><b>{review["name"]}:</b> {review["text"]}</div>', unsafe_allow_html=True)
        
        if can_edit:
            col_edit, col_del, col_space = st.columns([1, 1, 8])
            with col_edit:
                if st.button(f"تعديل 📝", key=f"edit_{review['id']}"):
                    st.session_state.editing_id = review['id']
            with col_del:
                if st.button(f"حذف 🗑️", key=f"del_{review['id']}"):
                    st.session_state.reviews.pop(i)
                    st.rerun()

st.write("---")

# منطقة الكتابة أو التعديل
if 'editing_id' in st.session_state:
    st.subheader("📝 تعديل تعليقك")
    # البحث عن التعليق المراد تعديله
    edit_idx = next(i for i, r in enumerate(st.session_state.reviews) if r['id'] == st.session_state.editing_id)
    new_text = st.text_area("عدل كلامك هنا:", value=st.session_state.reviews[edit_idx]['text'])
    if st.button("حفظ التعديلات ✅"):
        st.session_state.reviews[edit_idx]['text'] = new_text
        del st.session_state.editing_id
        st.success("تم التعديل بنجاح!")
        st.rerun()
else:
    st.subheader("📝 أضف تعليقك")
    with st.form(key='review_form', clear_on_submit=True):
        u_name = st.text_input("الاسم:")
        u_comment = st.selectbox("رأي سريع:", ["ممتاز", "مواعيد دقيقة", "شغل نظيف", "كتابة تعليق آخر..."])
        u_custom = st.text_area("تفاصيل أخرى (اختياري):")
        submit = st.form_submit_button("تأكيد ونشر التعليق ✅")
        
        if submit and u_name:
            final_text = u_custom if u_comment == "كتابة تعليق آخر..." else u_comment
            new_review = {
                "id": str(uuid.uuid4()),
                "user_id": st.session_state.user_id,
                "name": u_name,
                "text": final_text,
                "time": time.time()
            }
            st.session_state.reviews.insert(0, new_review)
            st.rerun()

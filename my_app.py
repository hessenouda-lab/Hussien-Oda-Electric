import streamlit as st
import time
import uuid

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. حفظ بيانات الجلسة (التعليقات وبصمة المستخدم)
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"id": "1", "user_id": "admin", "name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد."},
        {"id": "2", "user_id": "admin", "name": "أحمد علي", "text": "رجل محترم وأمين جداً في الخامات."}
    ]

# 3. تصميم الواجهة والوضوح العالي
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: white !important; font-size: 20px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    
    /* ستايل زرار التأكيد الضخم */
    div.stButton > button {
        background-color: #ffde59 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        border-radius: 12px;
        border: 2px solid #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# 4. العنوان والاتصال المباشر
st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# روابط الاتصال المباشرة (تعمل داخل الماسنجر والواتساب)
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown(f'''
        <a href="tel:01123393030" target="_blank" style="text-decoration: none;">
            <div style="background-color: #ff4b4b; color: white; padding: 20px; border-radius: 15px; text-align: center; font-size: 22px; font-weight: bold;">
                📞 اتصل الآن
            </div>
        </a>
    ''', unsafe_allow_html=True)

with col_wa:
    st.markdown(f'''
        <a href="https://api.whatsapp.com/send?phone=201123393030" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25d366; color: white; padding: 20px; border-radius: 15px; text-align: center; font-size: 22px; font-weight: bold;">
                💬 واتساب
            </div>
        </a>
    ''', unsafe_allow_html=True)

st.write("---")

# 5. الخدمات الاحترافية (محفوظة)
st.markdown("<h2>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>توزيع أحمال وتأسيس سمارت</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>ليد بروفايل ونجف حديث</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>لوحات توزيع ومفاتيح حماية</p></div>', unsafe_allow_html=True)

st.write("---")

# 6. كواليس العمل (الفيديوهات)
st.markdown("<h2>🎬 كواليس العمل</h2>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
with v2: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.write("---")

# 7. نظام التعليقات (إتاحة التعليق للجميع)
st.markdown("<h2>💬 آراء الناس في شغلنا</h2>", unsafe_allow_html=True)

for i, review in enumerate(st.session_state.reviews):
    st.markdown(f'<div class="review-box"><b>{review.get("name")}:</b> {review.get("text")}</div>', unsafe_allow_html=True)

st.write("---")

# 8. منطقة إضافة التعليق (متاحة للرد والتعليق)
st.markdown("### 📝 اترك رأيك هنا")
with st.form(key='hussien_final_form', clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    u_choice = st.selectbox("رأي سريع:", ["ممتاز جداً.. تسلم إيدك", "مواعيد دقيقة وشغل نظيف", "كتابة تعليق آخر..."])
    u_custom = st.text_area("رأيك بالتفصيل:")
    
    submit_btn = st.form_submit_button("تأكيد ونشر التعليق ✅")
    
    if submit_btn:
        if u_name:
            final_txt = u_custom if u_choice == "كتابة تعليق آخر..." else u_choice
            new_rev = {
                "id": str(uuid.uuid4()),
                "user_id": st.session_state.user_id,
                "name": u_name,
                "text": final_txt
            }
            st.session_state.reviews.insert(0, new_rev)
            st.success("تم نشر تعليقك بنجاح!")
            st.rerun()
        else:
            st.error("من فضلك اكتب اسمك أولاً")

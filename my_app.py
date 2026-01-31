import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# CSS التصميم
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .card { background: #1c1f26; border: 2px solid #ffde59; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffde59 !important; text-align: center; }
    p { color: #ffffff !important; font-size: 18px !important; }
    .review-box { background-color: #262730; padding: 15px; border-radius: 10px; border-right: 5px solid #ffde59; margin-bottom: 10px; color: white; }
    /* ستايل خاص لزرار النشر */
    .stButton>button {
        background-color: #ffde59 !important;
        color: black !important;
        font-weight: bold !important;
        font-size: 20px !important;
        height: 50px !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده لخدمات الكهرباء</h1>", unsafe_allow_html=True)

# أزرار التواصل السريع
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with col_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; border-radius:50px; text-align:center; font-size:22px; font-weight:bold;">💬 واتساب</div></a>', unsafe_allow_html=True)

st.write("---")

# آراء العملاء المعروضة
st.markdown("<h2>⭐ آراء العملاء</h2>", unsafe_allow_html=True)

if 'reviews' not in st.session_state:
    st.session_state.reviews = [
        {"name": "محمد صلاح", "text": "شغل ممتاز وتسليم في الميعاد.", "stars": "⭐⭐⭐⭐⭐"},
        {"name": "أحمد علي", "text": "رجل محترم وأمين جداً.", "stars": "⭐⭐⭐⭐⭐"}
    ]

for review in st.session_state.reviews:
    st.markdown(f'<div class="review-box"><b>{review["name"]}:</b> "{review["text"]}" {review["stars"]}</div>', unsafe_allow_html=True)

st.write("---")

# قسم إضافة التقييم الجديد
st.markdown("### 📝 اكتب رأيك هنا")

# فورم لاستقبال البيانات وتنظيفها تلقائياً
with st.form(key='review_form', clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    
    # اراء جاهزة للاختيار
    u_choice = st.selectbox("اختر رأيك السريع:", 
                             ["ممتاز جداً.. تسلم إيدك", 
                              "مواعيد دقيقة وشغل نظيف", 
                              "رجل أمين وخلوق ومتمكن", 
                              "كتابة رأي آخر..."])
    
    # خانة للكتابة لو اختار رأي آخر
    u_custom = ""
    if u_choice == "كتابة رأي آخر...":
        u_custom = st.text_area("اكتب رأيك بالتفصيل:")
    
    u_rating = st.select_slider("تقييمك بالنجوم:", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
    
    # الزرار الواضح
    submit_button = st.form_submit_button(label='✅ اضغط هنا لنشر تعليقك')

    if submit_button:
        if u_name:
            final_text = u_custom if u_choice == "كتابة رأي آخر..." else u_choice
            new_review = {"name": u_name, "text": final_text, "stars": u_rating}
            st.session_state.reviews.insert(0, new_review) # يظهر في الأول
            st.success(f"تم نشر تعليقك يا {u_name} بنجاح! شكراً لك.")
            # الصفحة هتعمل ريفريش تلقائي والبيانات هتتمسح بسبب clear_on_submit
        else:
            st.error("من فضلك اكتب الاسم أولاً")

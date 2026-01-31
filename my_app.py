import streamlit as st

# إعدادات احترافية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# تصميم "الوضوح العالي" لراحة العين
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background: #0e1117; }
    
    /* تصميم الكروت بوضوح عالي */
    .card {
        background: #1c1f26; /* خلفية داكنة ثابتة */
        border: 2px solid #ffde59; /* حدود صفراء واضحة */
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 15px;
    }
    
    /* توضيح العناوين والكلمات */
    h1, h2, h3 { color: #ffde59 !important; }
    p { 
        color: #ffffff !important; /* أبيض صريح للنصوص */
        font-size: 20px !important; /* تكبير الخط */
        font-weight: 500;
    }
    
    .emergency-btn {
        background: #ff4b4b;
        color: white !important;
        padding: 20px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: block;
        text-align: center;
        font-size: 22px;
    }
    </style>
""", unsafe_allow_html=True)

# الجزء العلوي
st.markdown("<h1 style='text-align: center;'>⚡ حسين عوده لخدمات الكهرباء الحديثة</h1>", unsafe_allow_html=True)

# أزرار الفعل السريع
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown('<a href="tel:01123393030" class="emergency-btn">🆘 اتصل الآن (للطوارئ)</a>', unsafe_allow_html=True)
with col_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:20px; border-radius:50px; text-align:center; font-size:20px; font-weight:bold;">💬 واتساب (حجز ومعاينة)</div></a>', unsafe_allow_html=True)

st.write("---")

# الخدمات بوضوح عالي جداً
st.markdown("<h2 style='text-align: center;'>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>توزيع أحمال وتأسيس شقق سمارت بأحدث الأكواد</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>تركيب ليد بروفايل، ونجف، وإضاءة مخفية حديثة</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>تركيب لوحات توزيع ومفاتيح حماية أوتوماتيكية</p></div>', unsafe_allow_html=True)

# قسم الفيديوهات والتقييمات يكمل هنا بنفس الترتيب...

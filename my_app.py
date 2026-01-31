import streamlit as st

# إعدادات احترافية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# تصميم "الخيال الرقمي" باستخدام CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #ffde59;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .card:hover { transform: translateY(-10px); box-shadow: 0 10px 20px rgba(255, 222, 89, 0.2); }
    h1, h2, h3 { color: #ffde59 !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
    .emergency-btn {
        background: linear-gradient(90deg, #ff4b4b, #a50000);
        color: white !important;
        padding: 20px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: block;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% {box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.7);} 70% {box-shadow: 0 0 0 20px rgba(255, 75, 75, 0);} 100% {box-shadow: 0 0 0 0 rgba(255, 75, 75, 0);} }
    </style>
""", unsafe_allow_html=True)

# الجزء العلوي (العالمي)
st.markdown("<h1 style='text-align: center;'>⚡ حسين عوده لخدمات الكهرباء الحديثة ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>نحن لا نركب أسلاكاً.. نحن نضيء مستقبلك</p>", unsafe_allow_html=True)

# أزرار الفعل السريع (Call to Action)
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown('<a href="tel:01123393030" class="emergency-btn" style="text-align:center;">🆘 حالة طوارئ؟ اتصل فوراً</a>', unsafe_allow_html=True)
with col_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:20px; border-radius:50px; text-align:center; font-size:20px; font-weight:bold;">💬 اطلب معاينة مجانية (واتساب)</div></a>', unsafe_allow_html=True)

st.write("---")

# الخدمات بشكل "كروت" فخمة
st.markdown("<h2>🛠️ خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>🏠 تأسيس ذكي</h3><p>توزيع أحمال وتأسيس شقق سمارت بأحدث الأكواد العالمية</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>💡 ديكورات إضاءة</h3><p>تركيب ليد بروفايل، ونجف، وإضاءة مخفية تبرز جمال بيتك</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>🛡️ أمان وحماية</h3><p>تركيب مفاتيح أتوماتيك ولوحات توزيع تحمي أجهزتك من التلف</p></div>', unsafe_allow_html=True)

# الفيديوهات (قسم الواقع)
st.write("---")
st.markdown("<h2>🎬 كواليس العمل (الدقة في التنفيذ)</h2>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1:
    st.video("https://www.youtube.com/watch?v=your_video_id_1")
    st.caption("فن ترتيب اللوحات")
with v2:
    st.video("https://www.youtube.com/watch?v=your_video_id_2")
    st.caption("تسليم أحد المواقع الكبرى")

# التقييمات (كلام الناس)
st.write("---")
st.markdown("<h2>⭐ ثقة عملائنا هي رأسمالنا</h2>", unsafe_allow_html=True)
st.success("المهندس حسين فنان، حقيقي الشقة اختلفت تماماً بعد لمساته في الإضاءة. (د. سامي - التجمع)")
st.info("سرعة في الرد وأمانة في الخامات، أنصح به بشدة. (م. هبة - المعادي)")

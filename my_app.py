import streamlit as st

# إعدادات الصفحة المتقدمة
st.set_page_config(page_title="حسين عوده لخدمات الكهرباء", page_icon="⚡", layout="wide")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    .service-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# الهيدر (العنوان الرئيسي)
st.title("⚡ حسين عوده لخدمات الكهرباء")
st.subheader("خبرة، أمان، وسرعة في التنفيذ")

# القسم الأول: فيديوهات العمل (الواقع)
st.write("### 🎬 من مواقع العمل")
col1, col2 = st.columns(2)
with col1:
    st.info("تركيب لوحات التوزيع")
    # هنا تقدر تحط رابط فيديو من اليوتيوب أو رابط مباشر
    st.video("https://www.youtube.com/watch?v=your_video_id_1") 
with col2:
    st.info("تأسيس المنشآت الحديثة")
    st.video("https://www.youtube.com/watch?v=your_video_id_2")

# القسم الثاني: الطلب السريع والخدمات
st.write("---")
st.write("### 🛠️ خدماتنا والطلب السريع")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="service-card"><h4>صيانة منزلية</h4><p>إصلاح جميع أعطال الكهرباء فوراً</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="service-card"><h4>تأسيس شقق</h4><p>تخطيط وتنفيذ بأعلى جودة</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="service-card"><h4>تركيب إضاءة</h4><p>ديكورات ونجف وليد بروفايل</p></div>', unsafe_allow_html=True)

# القسم الثالث: الأزرار التفاعلية (الاتصال والواتساب)
st.write("---")
col_call, col_wa = st.columns(2)
with col_call:
    st.markdown('<a href="tel:01123393030" style="text-decoration:none;"><div style="background-color:#ff4b4b; color:white; padding:20px; border-radius:15px; text-align:center; font-size:22px; font-weight:bold;">📞 اتصل الآن</div></a>', unsafe_allow_html=True)
with col_wa:
    st.markdown('<a href="https://wa.me/201123393030" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:20px; border-radius:15px; text-align:center; font-size:22px; font-weight:bold;">💬 واتساب سريع</div></a>', unsafe_allow_html=True)

# القسم الرابع: التقييمات
st.write("---")
st.write("### ⭐ تقييمات العملاء")
st.success("⭐⭐⭐⭐⭐ - 'شغل نظيف جداً ومواعيد دقيقة' (أحمد محمد)")
st.success("⭐⭐⭐⭐⭐ - 'أفضل فني تعاملت معه في التأسيس' (محمود علي)")

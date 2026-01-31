import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. رسالة إرشادية لعملاء الماسنجر (للمحافظة على الأداء)
st.components.v1.html("""
<script>
    var isFB = /FBAN|FBAV|Messenger/i.test(navigator.userAgent);
    if (isFB) {
        alert("عميلنا العزيز، لضمان أفضل تجربة للموقع، يرجى الضغط على الثلاث نقاط بالأعلى واختيار 'الفتح في المتصفح'.");
    }
</script>
""", height=0)

# 3. التنسيق الماسي الفخم (الاسم 32px والتعليق 26px)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 15px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        text-align: right;
    }
    .client-name { color: #d4af37 !important; font-size: 32px !important; font-weight: bold; display: block; }
    .client-text { color: #ffffff !important; font-size: 26px !important; margin-top: 15px; display: block; line-height: 1.4; }
    
    .diamond-btn {
        display: block; width: 100%; height: 85px; line-height: 85px; 
        text-align: center; font-size: 28px; font-weight: bold; 
        border-radius: 20px; text-decoration: none !important; 
        color: white !important; margin-bottom: 15px;
    }
    .red-btn { background: linear-gradient(45deg, #ff4b4b, #b22222); }
    .green-btn { background: linear-gradient(45deg, #25d366, #128c7e); }
    
    .social-btn {
        display: inline-block; padding: 18px 35px; margin: 8px;
        border-radius: 15px; text-decoration: none !important;
        color: white !important; font-size: 22px; font-weight: bold;
    }
    .fb-bg { background-color: #1877F2; } 
    .tt-bg { background-color: #000000; border: 2px solid #fe2c55; } 
    .yt-bg { background-color: #FF0000; }
    
    .announcement-box {
        background-color: rgba(212, 175, 55, 0.1);
        border: 2px dashed #d4af37;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 4. رسالة التوجيه للسوشيال ميديا (بديلة لنموذج التعليقات)
st.markdown("""
<div class="announcement-box">
    <h3 style="color: #d4af37; margin-bottom: 10px;">عائلتنا الكبيرة.. رأيكم يهمنا! ✨</h3>
    <p style="color: white; font-size: 24px;">
        لإضافة تعليق جديد أو تسجيل إعجابكم بأعمالنا، يسعدنا تواصلكم عبر منصاتنا الرسمية. <br>
        شكراً على ثقتكم الغالية ومشاركتكم مسيرة نجاحنا.
    </p>
</div>
""", unsafe_allow_html=True)

# 5. أزرار التواصل المباشر (التصميم الأصلي)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 6. منصات التواصل الاجتماعي (الروابط الكاملة)
st.markdown("<h2>🔗 تابعونا لمشاهدة أحدث الفيديوهات</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="

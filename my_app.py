import streamlit as st

# 1. إعدادات الصفحة الملكية والخطوط
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. عنوان الموقع الفخم (النسخة الأصلية)
st.markdown("<h1 style='text-align: center; color: #FFD700; font-size: 50px;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 26px;'>الاحترافية والدقة في عالم الخدمات الكهربائية</p>", unsafe_allow_html=True)

# 3. رسالة إيقاف التعليقات (بتصميم بارز)
st.markdown("---")
st.warning("⚠️ تم إيقاف استقبال التعليقات عبر الموقع مؤقتاً.")
st.markdown("""
    <div style="text-align: center; padding: 20px; border: 2px solid #FFD700; border-radius: 10px; background-color: rgba(255, 215, 0, 0.1);">
        <h3 style="color: white;">للتعليق، إضافة إعجاب، أو تقديم الشكر</h3>
        <p style="font-size: 22px; color: #FFD700;">يرجى زيارة صفحاتنا الرسمية على السوشيال ميديا</p>
        <p style="font-size: 24px;"> 
            <a href="https://www.facebook.com" style="color: #1877F2; text-decoration: none;">Facebook</a> | 
            <a href="https://wa.me/yournumber" style="color: #25D366; text-decoration: none;">WhatsApp</a>
        </p>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# 4. قائمة الـ 30 تعليق (بتصميم البرواز الذهبي والخطوط الكبيرة)
st.markdown("<h2 style='color: #FFD700; text-align: center;'>آراء عملائنا الكرام ✨</h2>", unsafe_allow_html=True)

comments = [
    ("حسين عوده", "مهندس

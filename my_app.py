import streamlit as st

# 1. إعدادات الصفحة الملكية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. عنوان الموقع الفخم (النسخة اللي حبيتها)
st.markdown("<h1 style='text-align: center; color: #FFD700;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 26px; font-weight: bold;'>المهندس حسين عوده للخدمات الكهربائية المتكاملة</p>", unsafe_allow_html=True)

# 3. رسالة إيقاف التعليقات وتوجيه العملاء
st.markdown("---")
st.warning("⚠️ تم إيقاف استقبال التعليقات عبر الموقع مؤقتاً.")
st.markdown("""
<div style="text-align: center; background-color: rgba(255, 215, 0, 0.1); padding: 20px; border-radius: 15px; border: 2px solid #FFD700;">
    <h3 style="color: white;">لإضافة رأيك أو التواصل معنا، يسعدنا انضمامكم لصفحاتنا:</h3>
    <p style="font-size: 22px;">
        <a href="https://www.facebook.com" target="_blank" style="color: #FFD700; text-decoration: none;">🔵 فيسبوك</a> | 
        <a href="https://wa.me/yournumber" target="_blank" style="color: #25D366; text-decoration: none;">🟢 واتساب</a>
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# 4. قائمة التعليقات الـ 30 المتنوعة (بالتنسيق الملكي)
st.markdown("<h2 style='color: #FFD700; text-align: center;'>أبرز آراء عملائنا</h2>", unsafe_allow_html=True)

comments = [
    ("أحمد رأفت", "شغل تسليم مفتاح ومواعيد دقيقة جداً."),
    ("محمد السيد", "المهندس حسين مثال للأمانة والشطارة في الشغل."),
    ("الحاج محمود", "تأسيس الشقة بالكامل كان ممتاز وبأفضل الخامات."),
    ("كريم علي", "أسرع استجابة للأعطال الطارئة، شكراً جزيلاً."),
    ("ياسر جلال", "فن وتنسيق في توزيع الإضاءة، تسلم إيدك."),
    ("م/ هاني يوسف", "مهندس محترف وع

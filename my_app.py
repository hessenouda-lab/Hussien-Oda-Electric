import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تصميم الواجهة (CSS) لضمان الشكل الفخم
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMarkdown { font-family: 'Arial'; }
    .social-box {
        text-align: center; 
        background-color: rgba(255, 215, 0, 0.1); 
        padding: 25px; 
        border-radius: 20px; 
        border: 3px solid #FFD700;
        margin: 20px 0;
    }
    .comment-box {
        border: 6px solid #FFD700; 
        padding: 18px; 
        border-radius: 20px; 
        margin-bottom: 22px; 
        background-color: rgba(255, 215, 0, 0.05); 
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# 3. رأس الصفحة (العنوان الأصلي)
st.markdown("<h1 style='text-align: center; color: #FFD700;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 28px; font-weight: bold;'>المهندس حسين عوده للخدمات الكهربائية المتكاملة</p>", unsafe_allow_html=True)

# 4. رسالة السوشيال ميديا بكلمات "من القلب"
st.markdown("---")
st.markdown("""
<div class="social-box">
    <h2 style="color: #FFD700;">عائلتنا الكبيرة.. نحن نكبر بكم! ✨</h2>
    <p style="color: white; font-size: 22px;">
        لأن رأيكم هو سر نجاحنا، وبسبب ضغط التحديثات، تم إيقاف التعليقات هنا مؤقتاً. <br>
        <b>لكننا دائماً معكم!</b> شاركونا إعجاباتكم وآراءكم وتابعوا أقوى فيديوهات الشغل العملي على منصاتنا:
    </p>
    <p style="font-size: 26px;">
        <a href="#" style="color: #1877F2; text-decoration: none;">🔵 Facebook</a> &nbsp;&nbsp; | &nbsp;&nbsp;
        <a href="#" style="color: #FF0000; text-decoration: none;">🔴 YouTube</a> &nbsp;&nbsp; | &nbsp;&nbsp;
        <a href="#" style="color: #FFFFFF; text-decoration: none;">⚫ TikTok</a>
    </p>
    <p style="color: #FFD700; font-size: 18px; margin-top: 10px;">ننتظركم هناك لنستمر في تقديم الأفضل دائماً ⚡</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# 5. عرض الصور والمحتوى (هنا يظهر شكل الموقع الأصلي)
# ملاحظة: تأكد من وضع روابط صورك الأصلية هنا في مكان "URL"
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='color: #FFD700; text-align: center;'>أحدث أعمالنا</h3>", unsafe_allow_html=True)
    st.image("https://via.placeholder.com/600x400/000000/FFD700?text=Work+Image+1", use_container_width=True) # ضع رابط صورتك هنا

with col2:
    st.markdown("<h3 style='color: #FFD700; text-align: center;'>دقة في التنفيذ</h3>", unsafe_allow_html=True)
    st.image("https://via.placeholder.com/600x400/000000/FFD700?text=Work+Image+2", use_container_width=True) # ضع رابط صورتك هنا

# 6. قسم التعليقات الـ 30 (بالتنسيق الملكي)
st.markdown("<br><h2 style='color: #FFD700; text-align: center;'>أبرز آراء عملائنا</h2>", unsafe_allow_html=True)

comments = [
    ("أحمد رأفت", "شغل تسليم مفتاح ومواعيد دقيقة جداً."),
    ("محمد السيد", "المهندس حسين مثال للأمانة والشطارة في الشغل."),
    ("الحاج محمود", "تأسيس الشقة بالكامل كان ممتاز وبأفضل الخامات."),
    ("كريم علي", "أسرع استجابة للأعطال الطارئة، شكراً جزيلاً."),
    ("ياسر جلال", "فن وتنسيق في توزيع الإضاءة، تسلم إيدك."),
    ("م/ هاني يوسف", "مهندس محترف وعارف بيعمل إيه كويس."),
    ("أحمد عبد الله", "الأسعار مناسبة جداً مقارنة بجودة التنفيذ."),
    ("سامح شكري", "شغل نظيف جداً وتشطيبات فاخرة."),
    ("عصام حلمي", "تم حل مشكلة الرعشة في الكهرباء نهائياً."),
    ("إبراهيم فوزي", "دقة في تنفيذ المخططات الهندسية."),
    ("

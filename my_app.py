import streamlit as st

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تصميم الواجهة الاحترافية (CSS)
st.markdown("""
    <style>
    .main { background: linear-gradient(to bottom, #0e1117, #1a1c23); }
    .social-section {
        background: rgba(255, 215, 0, 0.07);
        padding: 40px;
        border-radius: 25px;
        border: 4px solid #FFD700;
        text-align: center;
        margin: 30px auto;
        max-width: 900px;
    }
    .social-link {
        display: inline-block;
        margin: 15px 25px;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 24px;
        transition: 0.3s;
    }
    .comment-card {
        border: 6px solid #FFD700; 
        padding: 25px; 
        border-radius: 20px; 
        margin-bottom: 25px; 
        background: rgba(0, 0, 0, 0.3);
        text-align: right;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 3. رأس الصفحة (البراند الأصلي)
st.markdown("<h1 style='text-align: center; color: #FFD700; font-size: 55px;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 30px; font-weight: bold;'>الاحترافية في عالم الكهرباء.. دقة، أمان، وتميز</p>", unsafe_allow_html=True)

# 4. رسالة التوجيه الذهبية للسوشيال ميديا (بناءً على طلبك)
st.markdown("""
<div class="social-section">
    <h2 style="color: #FFD700; font-size: 38px; margin-bottom: 20px;">عائلتنا الكبيرة.. رأيكم هو نبض نجاحنا! ✨</h2>
    <p style="color: #ffffff; font-size: 26px; line-height: 1.6;">
        لأننا نسعى دائماً لتقديم أفضل تجربة لكم، وبسبب تحديثات الأنظمة الجارية، <br>
        تم نقل قسم استقبال الآراء إلى منصاتنا التفاعلية لنكون أقرب إليكم دائماً.
    </p>
    <div style="margin-top: 30px;">
        <a href="https://m.me/your_id" class="social-link" style="background: #0084FF; color: white;">💬 ماسنجر</a>
        <a href="#" class="social-link" style="background: #1877F2; color: white;">🔵 فيسبوك</a>
        <a href="#" class="social-link" style="background: #000000; color: white; border: 1px solid #fff;">⚫ تيك توك</a>
        <a href="#" class="social-link" style="background: #FF0000; color: white;">🔴 يوتيوب</a>
    </div>
    <p style="color: #FFD700; font-size: 22px; margin-top: 25px; font-weight: bold;">
        ننتظر رسائلكم وإبداعاتكم هناك.. شكراً لثقتكم الغالية ⚡
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 5. عرض آراء العملاء الـ 30 (التنسيق الملكي الأصلي)
st.markdown("<h2 style='color: #FFD700; text-align: center; font-size: 40px; margin-bottom: 40px;'>أبرز ما قاله عملاؤنا عنا</h2>", unsafe_allow_html=True)

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
    ("خالد السعدني", "تعامل راقي جداً والتزام بكلمته."),
    ("مصطفى كامل", "أفضل فني كهرباء في المنطقة بلا منازع."),
    ("وائل منصور", "تنسيق اللوحة الرئيسية كان

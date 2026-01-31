import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. التنسيق الجمالي (CSS) - ده اللي بيعمل "شكل" الموقع
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMarkdown { font-family: 'Arial'; }
    .hero-section {
        text-align: center;
        padding: 50px;
        background: linear-gradient(145deg, #1a1c23, #0e1117);
        border-bottom: 5px solid #FFD700;
        margin-bottom: 40px;
    }
    .social-box {
        text-align: center; 
        background-color: rgba(255, 215, 0, 0.08); 
        padding: 40px; 
        border-radius: 25px; 
        border: 4px solid #FFD700;
        margin: 30px auto;
        max-width: 900px;
    }
    .social-btn {
        display: inline-block;
        margin: 10px;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none;
        color: white !important;
        font-weight: bold;
        font-size: 22px;
        transition: 0.3s;
    }
    .comment-card {
        border: 6px solid #FFD700; 
        padding: 25px; 
        border-radius: 20px; 
        margin-bottom: 30px; 
        background-color: rgba(255, 215, 0, 0.03); 
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# 3. رأس الصفحة (العنوان الملكي)
st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
st.markdown("<h1 style='color: #FFD700; font-size: 60px; margin-bottom: 10px;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: white; font-size: 30px;'>التميز في التنفيذ.. والاحترافية في كل تفصيلة</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 4. رسالة السوشيال ميديا والماسنجر (بأسلوبنا الجديد)
st.markdown("""
<div class="social-box">
    <h2 style="color: #FFD700; font-size: 40px; margin-bottom: 20px;">عائلتنا الكبيرة.. رأيكم هو سر تميزنا! ✨</h2>
    <p style="color: white; font-size: 26px; line-height: 1.6;">
        لأننا نكبر بكلمتكم الطيبة، وبسبب تحديثات الموقع الجارية، <br>
        تم نقل قسم استقبال الآراء إلى منصاتنا التفاعلية لنكون معكم لحظة بلحظة.
    </p>
    <div style="margin-top: 30px;">
        <a href="https://m.me/YOUR_ID" class="social-btn" style="background: #0084FF;">💬 ماسنجر</a>
        <a href="#" class="social-btn" style="background: #1877F2;">🔵 فيسبوك</a>
        <a href="#" class="social-btn" style="background: #000000; border: 1px solid white;">⚫ تيك توك</a>
        <a href="#" class="social-btn" style="background: #FF0000;">🔴 يوتيوب</a>
    </div>
    <p style="color: #FFD700; font-size: 22px; margin-top: 25px; font-weight: bold;">
        شكر وتقدير لكل عميل ساهم في نجاحنا بكلمة طيبة.. ننتظركم هناك! ⚡
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 2px solid #FFD700;'>", unsafe_allow_html=True)

# 5. عرض الـ 30 تعليق (بالتنسيق اللي حبيته)
st.markdown("<h2 style='color: #FFD700; text-align: center; font-size: 45px; margin-bottom: 50px;'>أبرز ما قاله عملاؤنا عنا</h2>", unsafe_allow_html=True)

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
    ("وائل منصور", "تنسيق اللوحة الرئيسية كان مبهراً ومنظماً."),
    ("تامر يحيى", "شكراً على النصائح في اختيار كشافات الموفرة."),
    ("مجدي عبد الغني", "شغل يشرف وأي حد يسألني هرشحك فوراً."),
    ("ياسين التهامي", "بارك الله في رزقك يا هندسة حسين."),
    ("سعيد الهواري", "دائماً مبدع ومنفرد بلمساتك الخاصة."),
    ("حسين الشحات", "الفيلا نورت وشغلك فخر لينا كلنا."),
    ("رامي جمال", "خدمة مابعد التنفيذ والمتابعة ممتازة."),
    ("شريف عامر", "حلول ذكية جداً لتوفير استهلاك الكهرباء."),
    ("باسم مرسي", "التزام تام بالخامات الأصلية والأسلاك المعتمدة."),
    ("أشرف عبد العزيز", "بصمة مميزة في كل ركن من أركان الشقة."),
    ("صلاح محسن", "توزيع برايز الكهرباء كان مدروساً ومريحاً."),
    ("بيومي فؤاد", "يا بخت اللي يتعامل معاك يا حسين، فنان!"),
    ("طارق حامد", "شغل احترافي وسرعة في الإنجاز."),
    ("أيمن أشرف", "تصحيح أخطاء الصنايعية القدام كان ببراعة."),
    ("محمود الونش", "ترتيب الشغل ونظافة المكان بعد العمل ممتازة."),
    ("عمرو السولية", "نظام سمارت هوم تم تركيبه بمنتهى السهولة."),
    ("محمد الشناوي", "سد ثغرات الكهرباء القديمة كان تحدي ونجحت فيه."),
    ("أفشة", "القاضية ممكن في شغلك، تسلم إيدك يا بطل.")
]

for name, text in comments:
    st.markdown(f"""
    <div class="comment-card">
        <p style="font-size: 32px; color: #FFD700; font-weight: bold; margin-bottom: 10px; direction: rtl;">{name}</p>
        <p style="font-size: 26px; color: white; direction: rtl;">{text}</p>
    </div>
    """, unsafe_allow_html=True)

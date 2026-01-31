import streamlit as st

# 1. إعدادات الصفحة الملكية
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. تصميم الواجهة (الخلفية والتنسيقات)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMarkdown { font-family: 'Arial'; }
    .social-card {
        text-align: center; 
        background-color: rgba(255, 215, 0, 0.1); 
        padding: 30px; 
        border-radius: 20px; 
        border: 4px solid #FFD700;
        margin: 20px 0;
    }
    .comment-card {
        border: 6px solid #FFD700; 
        padding: 20px; 
        border-radius: 20px; 
        margin-bottom: 25px; 
        background-color: rgba(255, 215, 0, 0.03); 
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# 3. عنوان الموقع (النسخة الأصلية)
st.markdown("<h1 style='text-align: center; color: #FFD700;'>⚡ Hussien Oda Electric ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 28px; font-weight: bold;'>المهندس حسين عوده للخدمات الكهربائية المتكاملة</p>", unsafe_allow_html=True)

# 4. رسالة السوشيال ميديا (الكلمات اللي طلبتها بلمسة جمالية)
st.markdown("---")
st.markdown("""
<div class="social-card">
    <h2 style="color: #FFD700;">عائلتنا الكبيرة.. رأيكم هو سر تميزنا! ✨</h2>
    <p style="color: white; font-size: 24px;">
        لتحسين جودة الخدمة وضمان وصول آرائكم للجميع، تم نقل قسم التعليقات إلى منصاتنا الرسمية. <br>
        <b>نسعد بمتابعتكم وتفاعلكم معنا عبر الروابط التالية:</b>
    </p>
    <div style="font-size: 30px; margin-top: 20px;">
        <a href="#" style="color: #1877F2; text-decoration: none; margin: 0 15px;">🔵 فيسبوك</a> 
        <a href="#" style="color: #FF0000; text-decoration: none; margin: 0 15px;">🔴 يوتيوب</a> 
        <a href="#" style="color: #FFFFFF; text-decoration: none; margin: 0 15px;">⚫ تيك توك</a>
    </div>
    <p style="color: #FFD700; font-size: 20px; margin-top: 15px;">شكر وتقدير لكل عميل ساهم في نجاحنا بكلمة طيبة ⚡</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# 5. قسم التعليقات الـ 30 (تنسيق ملكي وبدون أخطاء)
st.markdown("<h2 style='color: #FFD700; text-align: center;'>أبرز آراء عملائنا الكرام</h2>", unsafe_allow_html=True)

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
        <p style="font-size: 32px; color: #FFD700; font-weight: bold; margin-bottom: 8px; direction: rtl;">{name}</p>
        <p style="font-size: 26px; color: white; direction: rtl;">{text}</p>
    </div>
    """, unsafe_allow_html=True)

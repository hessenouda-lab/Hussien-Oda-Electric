import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. رسالة إرشادية لعملاء الماسنجر
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
        border: 6px solid #d4af37; margin-bottom: 25px; 
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
        border: 3px solid #d4af37;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 4. رسالة التوجيه الذهبية للسوشيال ميديا
st.markdown("""
<div class="announcement-box">
    <h2 style="color: #d4af37; margin-bottom: 15px;">عائلتنا الكبيرة.. رأيكم هو سر نجاحنا! ✨</h2>
    <p style="color: white; font-size: 26px; line-height: 1.6;">
        لإضافة تعليق جديد أو الإعجاب بأعمالنا، نتشرف بانضمامكم إلينا عبر منصاتنا الرسمية. <br>
        شكراً على ثقتكم الغالية ومشاركتكم الدائمة لنا.
    </p>
</div>
""", unsafe_allow_html=True)

# 5. أزرار التواصل المباشر (الأحمر والأخضر)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 6. أزرار السوشيال ميديا (فيسبوك، تيك توك، يوتيوب)
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-btn fb-bg">فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-btn tt-bg">تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-btn yt-bg">يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 7. قسم آراء العملاء (20 تعليق ثابت بتنسيق فخم)
st.markdown("<h2>🌟 آراء وشهادات العملاء</h2>", unsafe_allow_html=True)

fixed_reviews = [
    ("م/ أحمد رأفت", "شغل تسليم مفتاح ومواعيد دقيقة جداً. تأسيس احترافي."),
    ("محمد السيد", "المهندس حسين مثال للأمانة والشطارة في الشغل، برافو."),
    ("الحاج محمود", "تأسيس الشقة بالكامل كان ممتاز وبأفضل الخامات المعتمدة."),
    ("كريم علي", "أسرع استجابة للأعطال الطارئة، فني متمكن جداً."),
    ("ياسر جلال", "فن وتنسيق في توزيع الإضاءة والسمارت هوم، تسلم إيدك."),
    ("هاني يوسف", "مهندس محترف وعارف بيعمل إيه كويس، أنصح به بشدة."),
    ("عبد الله محمد", "الأسعار مناسبة جداً مقارنة بجودة التنفيذ العالية."),
    ("سامح شكري", "شغل نظيف جداً وتشطيبات فاخرة للوحات الكهرباء."),
    ("عصام حلمي", "تم حل مشكلة الرعشة وتوزيع الأحمال نهائياً بفضلك."),
    ("إبراهيم فوزي", "دقة متناهية في تنفيذ المخططات الهندسية المعقدة."),
    ("خالد السعدني", "تعامل راقي جداً والتزام تام بالكلمة والموعد."),
    ("مصطفى كامل", "أفضل فني كهرباء تعاملت معه، ذوق وأدب وإتقان."),
    ("وائل منصور", "تنسيق اللوحة الرئيسية كان مبهراً ومنظماً كأنه لوحة فنية."),
    ("تامر يحيى", "شكراً على الأمانة في اختيار الكابلات والمواسير الأصلية."),
    ("مجدي عبد الغني", "شغل يشرف وأي حد يسألني هرشح المهندس حسين فوراً."),
    ("ياسين التهامي", "بارك الله في رزقك، دقة وأمانة وإتقان في العمل."),
    ("سعيد الهواري", "دائماً مبدع ومنفرد بلمساتك الخاصة في التشطيب."),
    ("حسين الشحات", "الفيلا نورت وشغلك فخر لينا، بالتوفيق دائماً."),
    ("رامي جمال", "خدمة ما بعد التنفيذ والمتابعة ممتازة، شكراً لك."),
    ("شريف عامر", "حلول ذكية جداً لتوفير استهلاك الكهرباء وتأمين البيت.")
]

for name, text in fixed_reviews:
    st.markdown(f"""
        <div class="review-box">
            <div class="client-name">👤 {name}</div>
            <div class="client-text">{text}</div>
        </div>
    """, unsafe_allow_html=True)

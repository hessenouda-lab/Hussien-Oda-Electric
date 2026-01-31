import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. الربط بجدول البيانات (عشان المصداقية ومنع العشوائية)
conn = st.connection("gsheets", type=GSheetsConnection)

# 3. رسالة إرشادية لعملاء الماسنجر
st.components.v1.html("""
<script>
    var isFB = /FBAN|FBAV|Messenger/i.test(navigator.userAgent);
    if (isFB) {
        alert("عميلنا العزيز، لضمان سهولة التواصل معنا، يرجى الضغط على الثلاث نقاط في أعلى الشاشة واختيار 'الفتح في المتصفح' (Open in Browser).");
    }
</script>
""", height=0)

# 4. نافذة التأكيد (المودال الذهبي المعتمد)
@st.dialog("مراجعة رأيك قبل النشر ⚡")
def confirm_dialog(name, text):
    st.markdown(f"""
        <div style="background-color: #1a1e24; padding: 25px; border-radius: 15px; border: 3px solid #d4af37; text-align: right; color: white;">
            <p style="color: #d4af37; font-weight: bold; font-size: 32px; margin-bottom: 10px;">👤 الاسم: {name}</p>
            <div style="border-top: 2px solid #d4af37; padding-top: 15px;">
                <p style="font-size: 26px; color: #ffffff; line-height: 1.6;">💬 الرأي: "{text}"</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    if st.button("تأكيد ونشر التعليق الآن ✅", use_container_width=True, type="primary"):
        # حفظ في جوجل شيت فوراً
        try:
            df = conn.read()
            new_row = pd.DataFrame([{"name": name, "text": text}])
            updated_df = pd.concat([df, new_row], ignore_index=True)
            conn.update(data=updated_df)
            st.success("تم النشر بنجاح! شكراً لثقتكم.")
            time.sleep(1)
            st.rerun()
        except:
            st.error("عذراً، حدث خطأ في الاتصال بالجدول. تأكد من إعدادات الـ Secrets.")

# 5. التنسيق الماسي الفخم (الاسم 32px والتعليق 26px)
st.markdown("""
<style>
    .stApp { background-color: #0b0d11; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
    
    .review-box { 
        background: #161a21; padding: 35px; border-radius: 20px; 
        border-right: 15px solid #d4af37; margin-bottom: 25px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
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
    .fb-bg { background-color: #1877F2; } .tt-bg { background-color: #000000; border: 2px solid #fe2c55; } .yt-bg { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 6. أزرار التواصل المباشر
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="tel:01123393030" class="diamond-btn red-btn">📞 اتصل بنا الآن</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://wa.me/201123393030" target="_blank" class="diamond-btn green-btn">💬 راسلنا واتساب</a>', unsafe_allow_html=True)

st.write("---")

# 7. منصات التواصل الاجتماعي
st.markdown("<h2>🔗 تابعونا على منصاتنا</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center;">
        <a href="https://www.facebook.com/profile.php?id=61573193272647" target="_blank" class="social-btn fb-bg">🔵 فيسبوك</a>
        <a href="https://www.tiktok.com/@hessenouda1" target="_blank" class="social-btn tt-bg">⚫ تيك توك</a>
        <a href="https://www.youtube.com/channel/UCKF5VXyc5Uma_X4X_S5ld8w" target="_blank" class="social-btn yt-bg">🔴 يوتيوب</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 8. عرض التعليقات الحقيقية من الجدول
st.markdown("<h2>🌟 آراء وشهادات العملاء الحقيقية</h2>", unsafe_allow_html=True)
try:
    # جلب البيانات من الجدول وعرضها من الأحدث للأقدم
    data = conn.read()
    for _, r in data.iloc[::-1].iterrows():
        st.markdown(f"""
            <div class="review-box">
                <div class="client-name">👤 {r["name"]}</div>
                <div class="client-text">{r["text"]}</div>
            </div>
        """, unsafe_allow_html=True)
except:
    st.info("اكتب أول رأي موثق ليظهر هنا.. ✨")

# عرض التعليقات الخمسة المبدئية للمصداقية
initials = [
    {"n": "م/ محمد إبراهيم", "t": "تسليم في الموعد ودقة متناهية في توزيع الأحمال."},
    {"n": "أستاذ عصام", "t": "أفضل تعامل جربته في الطالبية، احترافية وأمان."},
    {"n": "الحاج محمود", "t": "شغل هندسي بجد، الله يبارك لك في رزقك يا حسين."},
    {"n": "د/ مروة", "t": "شكراً جزيلاً على الأمانة في اختيار الخامات والدقة."},
    {"n": "أحمد سمير", "t": "تأسيس ممتاز للشقة بالكامل وبأحدث الطرق الهندسية."}
]
for r in initials:
    st.markdown(f'<div class="review-box"><div class="client-name">👤 {r["n"]}</div><div class="client-text">{r["t"]}</div></div>', unsafe_allow_html=True)

st.write("---")

# 9. نموذج التعليق المطور
st.markdown("<h2 style='text-align: right;'>✍️ أضف رأيك الخاص الموثق</h2>", unsafe_allow_html=True)

with st.form("diamond_feedback_final_safe", clear_on_submit=True):
    u_name = st.text_input("الاسم الكريم:")
    
    st.markdown("<p style='color: #d4af37; text-align: right; font-weight: bold;'>اختر رأياً جاهزاً (اختياري):</p>", unsafe_allow_html=True)
    quick_options = [
        "لم يتم الاختيار...",
        "شغل ممتاز وتسليم في الموعد المحدد. شكراً جزيلاً.",
        "دقة في المواعيد واحترافية عالية في التنفيذ.",
        "أفضل فني كهرباء تعاملت معه، ذوق وأدب وشغل نظيف.",
        "خامات ممتازة وتأسيس هندسي على أعلى مستوى."
    ]
    u_quick = st.selectbox("اضغط هنا لاختيار جملة جاهزة:", quick_options)
    u_custom = st.text_area("أو اكتب رأيك الخاص بالتفصيل:")
    
    submit = st.form_submit_button("عرض التعليق للتأكيد ✨")
    
    if submit:
        final_text = u_custom.strip() if u_custom.strip() else (u_quick if u_quick != "لم يتم الاختيار..." else "")
        if u_name and final_text:
            confirm_dialog(u_name, final_text)
        else:
            st.warning("⚠️ يرجى كتابة الاسم وتحديد الرأي المطلوب")s

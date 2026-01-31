import streamlit as st
import time

# 1. الإعدادات
st.set_page_config(page_title="Hussien Oda Electric", page_icon="⚡", layout="wide")

# 2. البيانات
if 'reviews' not in st.session_state:
    st.session_state.reviews = [{"name": "أحمد علي", "text": "تأسيس كهرباء احترافي وخامات ممتازة."}]
if 'my_videos' not in st.session_state:
    st.session_state.my_videos = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
if 'my_images' not in st.session_state:
    st.session_state.my_images = ["https://via.placeholder.com/600x400"]

# 3. نافذة التأكيد
@st.dialog("مراجعة بيانات التعليق ⚡")
def confirm_dialog(name, text):
    st.markdown(f'<div style="background-color:#121212;padding:25px;border-radius:15px;border:3px solid #d4af37;text-align:right;color:white;"><p style="color:#d4af37;font-weight:bold;font-size:24px;">👤 المرسل: {name}</p><p style="font-size:22px;">💬 الرأي: "{text}"</p></div>', unsafe_allow_html=True)
    if st.button("اعتماد ونشر ✅", use_container_width=True, type="primary"):
        st.session_state.reviews.insert(0, {"name": name, "text": text})
        st.rerun()

# 4. التنسيق الفخم
st.markdown("""
<style>
.stApp { background-color: #0b0d11; }
h1, h2 { color: #d4af37 !important; text-align: center; font-weight: bold; }
.review-box { background: #161a21; padding: 35px; border-radius: 20px; border-right: 12px solid #d4af37; margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
.client-name { color: #d4af37; font-size: 32px; font-weight: bold; }
.client-text { color: #ffffff; font-size: 26px; margin-top: 15px; line-height: 1.5; }
div.stButton > button { height: 85px !important; font-size: 26px !important; border-radius: 20px !important; font-weight: bold !important; }
div[data-testid="stColumn"]:nth-child(1) button { background-color: #ff4b4b !important; color: white !important; }
div[data-testid="stColumn"]:nth-child(2) button { background-color: #25d366 !important; color: white !important; }
.social-link { display: inline-block; padding: 15px 35px; margin: 10px; border-radius: 15px; text-decoration: none; font-weight: bold; color: white !important; font-size: 22px; }
.fb { background-color: #1877F2; } .tt { background-color: #000000; border: 2px solid #fe2c55; } .yt { background-color: #FF0000; }
</style>
""", unsafe_allow_html=True)

# 5. لوحة التحكم (السايد بار)
with st.sidebar.expander("🔐 لوحة تحكم حسين"):
    adm_pass = st.text_input("كلمة السر:", type="password")
    if adm_pass == "1234":
        v_url = st.text_input("رابط فيديو يوتيوب:")
        if st.button("حفظ الفيديو 🎥"): st.session_state.my_videos.append(v_url)
        i_url = st.text_input("رابط صورة:")
        if st.button("حفظ الصورة 🖼️"): st.session_state.my_images.append(i_url)

st.markdown("<h1>⚡ حسين عوده للكهرباء الحديثة</h1>", unsafe_allow_html=True)

# 6. أزرار الاتصال
c1, c2 = st.columns(2)
with c1:
    if st.button("📞 اتصل بنا الآن", use_container_width=True):
        st.components.v1.html('<script>window.location.href="tel:01123393030";</script>', height=0)
with c2:
    if st.button("💬 راسلنا واتساب", use_container_width=True):
        st.components.v1.html('<script>window.open("https://wa.me/201123393030", "_blank");</script>', height=0)

st.write("---")

# 7.

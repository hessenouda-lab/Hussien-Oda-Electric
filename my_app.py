# 5. أزرار الاتصال السريع (تعديل احترافي للماسنجر)
col1, col2 = st.columns(2)
with col1:
    # رابط الاتصال المباشر
    st.markdown('''
        <a href="tel:01123393030" target="_blank" style="text-decoration:none;">
            <div style="background: #ff4b4b; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:24px; box-shadow: 0 4px 15px rgba(255,75,75,0.4);">
                📞 اتصل بنا الآن
            </div>
        </a>
    ''', unsafe_allow_html=True)

with col2:
    # رابط الواتساب مع كود الإجبار على فتح التطبيق
    st.markdown('''
        <a href="https://api.whatsapp.com/send?phone=201123393030" target="_blank" style="text-decoration:none;">
            <div style="background: #25d366; color:white; padding:25px; border-radius:15px; text-align:center; font-weight:bold; font-size:24px; box-shadow: 0 4px 15px rgba(37,211,102,0.4);">
                💬 راسلنا واتساب
            </div>
        </a>
    ''', unsafe_allow_html=True)

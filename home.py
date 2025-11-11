import streamlit as st

def render(user):
    st.title("لوحة التحكم")
    st.write(f"مرحبًا {user} 👋")
    st.info("اختر تبويب من القائمة الجانبية لعرض التفاصيل")

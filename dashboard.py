import streamlit as st
from auth import تسجيل_الدخول

user = تسجيل_الدخول()
if not user:
    st.stop()

# القائمة الجانبية
st.sidebar.title("القائمة")
tabs = [
    "لوحة التحكم", "المشرفين", "المناديب", "التطبيقات", "حسب القسم",
    "نقل المندوبين", "طلبات الاستثناء", "حالات التشغيل", "المالية", "السجلات"
]
choice = st.sidebar.radio("اختر التبويب", tabs)

# عرض محتوى التبويب المختار
st.title(f"📁 {choice}")
import home
import agents
import supervisors
import apps
import departments
import transfers
import exceptions
import operations
import finance

tab_functions = {
    "لوحة التحكم": home.render,
    "المشرفين": supervisors.render,
    "المناديب": agents.render,
    "التطبيقات": apps.render,
    "حسب القسم": departments.render,
    "نقل المندوبين": transfers.render,
    "طلبات الاستثناء": exceptions.render,
    "حالات التشغيل": operations.render,
    "المالية": finance.render,
    "السجلات": logs.render
}

tab_functions[choice](user)

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
import tabs.home as home
import tabs.supervisors as supervisors
import tabs.agents as agents
import tabs.apps as apps
import tabs.departments as departments
import tabs.transfers as transfers
import tabs.exceptions as exceptions
import tabs.operations as operations
import tabs.finance as finance
import tabs.logs as logs

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

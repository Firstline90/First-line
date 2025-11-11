import streamlit as st

# قائمة المستخدمين المسموح لهم بالدخول
المستخدمين = {
    "admin": {"كلمة_المرور": "123", "الدور": "مسؤول"},
    "user1": {"كلمة_المرور": "456", "الدور": "مندوب"},
    "user2": {"كلمة_المرور": "789", "الدور": "مشرف"}
}

def تسجيل_الدخول():
    if "user" in st.session_state and "role" in st.session_state:
        if st.session_state["role"] == "مسؤول":
            return st.session_state["user"]
        else:
            st.warning("هذا التبويب مخصص للمسؤول فقط")
            st.stop()

    st.title("تسجيل الدخول")
    username = st.text_input("اسم المستخدم")
    password = st.text_input("كلمة المرور", type="password")
    if st.button("تسجيل الدخول"):
        if username in المستخدمين and المستخدمين[username]["كلمة_المرور"] == password:
            الدور = المستخدمين[username]["الدور"]
            if الدور == "مسؤول":
                st.session_state["user"] = username
                st.session_state["role"] = الدور
                st.success("تم تسجيل الدخول بنجاح")
                return username
            else:
                st.warning("هذا التبويب مخصص للمسؤول فقط")
                st.stop()
        else:
            st.error("فشل تسجيل الدخول")
            return None
    return None

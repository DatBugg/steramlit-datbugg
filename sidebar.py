import streamlit as st

def sidebar_menu():
    st.sidebar.title("Menú")
    menu = st.sidebar.radio("Selecciona una opción:", ["Home", "Cloud", "Programación", "Utilidades"])

    submenu = None
    if menu == "Cloud":
        submenu = st.sidebar.selectbox("Selecciona un curso en Cloud:", ["Curso 1", "Curso 2"])
    elif menu == "Programación":
        submenu = st.sidebar.selectbox("Selecciona un curso en Programación:", ["Streamlit", "Curso 2"])
    elif menu == "Utilidades":
        submenu = st.sidebar.selectbox("Selecciona un curso en Utilidades:", ["Curso 1", "Curso 2"])

    return menu, submenu

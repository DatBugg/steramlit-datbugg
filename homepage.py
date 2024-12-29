import streamlit as st

def show_home():
    """Función para mostrar la página de inicio en Streamlit."""
    st.title("Welcome to DatBugg")

    # Distribuir los botones en una sola fila usando columnas de Streamlit
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("LinkedIn"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://www.linkedin.com/in/gonzalo-galante/" />', unsafe_allow_html=True)
    with col2:
        if st.button("Medium"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://medium.com/@gonzagalante" />', unsafe_allow_html=True)
    with col3:
        if st.button("Sitio"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://datbugg.com" />', unsafe_allow_html=True)
    with col4:
        if st.button("Streamlit"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://share.streamlit.io/user/datbugg" />', unsafe_allow_html=True)

    # Caja de descripción del sitio
    st.subheader("De qué trata este sitio")
    st.write("Este sitio está dedicado a compartir contenido útil sobre tecnología, programación, y herramientas para potenciar tu productividad.")

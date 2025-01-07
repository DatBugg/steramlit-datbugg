import streamlit as st

def show_home():
    """Function to show the home page in Streamlit."""
    st.title("Welcome to DatBugg Streamlit")

    # Using columns to distribute buttons horizontally
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<a href="https://www.linkedin.com/in/gonzalo-galante/" target="_blank"><button style="all: unset; cursor: pointer;">LinkedIn</button></a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<a href="https://medium.com/@gonzagalante" target="_blank"><button style="all: unset; cursor: pointer;">Medium</button></a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<a href="https://datbugg.com" target="_blank"><button style="all: unset; cursor: pointer;">Sitio</button></a>', unsafe_allow_html=True)
    with col4:
        st.markdown('<a href="https://share.streamlit.io/user/datbugg" target="_blank"><button style="all: unset; cursor: pointer;">Streamlit</button></a>', unsafe_allow_html=True)

    

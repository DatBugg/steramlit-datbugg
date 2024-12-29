import streamlit as st

def e1_streamlit_introduction():
    # Page configuration (title and description)
    st.title("🚀 Streamlit introduction")
    st.write("Learn how to build interactive applications with **Streamlit** in Python.")

    # Column layout (adjusting sizes)
    col1, col2 = st.columns([0.8, 3])  # Columna izquierda más chica

    # Left column: bassics commands
    with col1:
        st.subheader("📋 Commands")
        st.code("$ pip install streamlit", language='bash')
        st.write("**Streamlit Installation**")

        st.code("import streamlit as st", language='python')
        st.write("**Import the library into your code**")

        st.code("st.title('Mi título')", language='python')
        st.write("**Main title in your app**")

        st.code("st.write('¡Hola Mundo!')", language='python')
        st.write("**Basic text in your app**")

        st.code("st.sidebar.radio('Choose:', ['Opción 1', 'Opción 2'])", language='python')
        st.write("**Radio button in the sidebar**")

    # Right column: Sample codes
    with col2:
        st.subheader("🛠 Code Examples")

        # Sample 1: Title and text
        st.write("### 1. Title and Text")
        st.code("""
import streamlit as st

st.title("My first App")
st.write("Hello workd from Streamlit!")
        """, language='python')
        st.success("Result: A title with simple text.")

        # Sample 2: Widgets
        st.write("### 2. Using Widgets")
        st.code("""
import streamlit as st

opcion = st.radio("Choose an option:", ["Option 1", "Option 2"])
st.write("You have chosen:", opcion)
        """, language='python')
        st.success("Result: Displays an interactive radio button.")

        # Sample 3: Show data
        st.write("### 3. Show Data")
        st.code("""
import streamlit as st
import pandas as pd

data = {'Columna 1': [1, 2, 3], 'Columna 2': [4, 5, 6]}
df = pd.DataFrame(data)

st.write("### Data Table")
st.dataframe(df)
        """, language='python')
        st.success("Result: An interactive table of data.")

        # Sample 4: Sidebar
        st.write("### 4. Sidebar")
        st.code("""
import streamlit as st

st.sidebar.title("Menú Lateral")
opcion = st.sidebar.radio("Navegación:", ["Inicio", "Acerca de"])
st.write("You have selected:", opcion)
        """, language='python')
        st.success("Result: A sidebar with basic navigation.")

    # Final message
    st.info("Congratulations! 🚀 You have now learned the basics of Streamlit. You can combine these elements to create more complex applications.")

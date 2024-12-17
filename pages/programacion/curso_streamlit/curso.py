import streamlit as st

def programacion_streamlit():
    # Configuración de la página
    st.title("🚀 Minicurso: Introducción a Streamlit")
    st.write("Aprende a construir aplicaciones interactivas con **Streamlit** en Python.")

    # Diseño de columnas (ajustando tamaños)
    col1, col2 = st.columns([0.8, 3])  # Columna izquierda más chica

    # Columna izquierda: comandos básicos
    with col1:
        st.subheader("📋 Comandos Básicos")
        st.code("$ pip install streamlit", language='bash')
        st.write("**Instalación de Streamlit**")

        st.code("import streamlit as st", language='python')
        st.write("**Importa la biblioteca en tu código**")

        st.code("st.title('Mi título')", language='python')
        st.write("**Título principal en tu app**")

        st.code("st.write('¡Hola Mundo!')", language='python')
        st.write("**Texto básico en tu app**")

        st.code("st.sidebar.radio('Choose:', ['Opción 1', 'Opción 2'])", language='python')
        st.write("**Radio button en la barra lateral**")

    # Columna derecha: ejemplos de código
    with col2:
        st.subheader("🛠 Ejemplos de Código")

        # Ejemplo 1: Título y texto
        st.write("### 1. Título y Texto")
        st.code("""
import streamlit as st

st.title("Mi Primera App")
st.write("¡Hola Mundo desde Streamlit!")
        """, language='python')
        st.success("Resultado: Un título con texto sencillo.")

        # Ejemplo 2: Widgets
        st.write("### 2. Uso de Widgets")
        st.code("""
import streamlit as st

opcion = st.radio("Elige una opción:", ["Opción 1", "Opción 2"])
st.write("Has elegido:", opcion)
        """, language='python')
        st.success("Resultado: Muestra un radio button interactivo.")

        # Ejemplo 3: Mostrar datos
        st.write("### 3. Mostrar Datos")
        st.code("""
import streamlit as st
import pandas as pd

data = {'Columna 1': [1, 2, 3], 'Columna 2': [4, 5, 6]}
df = pd.DataFrame(data)

st.write("### Tabla de Datos")
st.dataframe(df)
        """, language='python')
        st.success("Resultado: Una tabla interactiva de datos.")

        # Ejemplo 4: Sidebar
        st.write("### 4. Barra Lateral")
        st.code("""
import streamlit as st

st.sidebar.title("Menú Lateral")
opcion = st.sidebar.radio("Navegación:", ["Inicio", "Acerca de"])
st.write("Has seleccionado:", opcion)
        """, language='python')
        st.success("Resultado: Una barra lateral con navegación básica.")

    # Mensaje final
    st.info("¡Felicidades! 🚀 Ya has aprendido los conceptos básicos de Streamlit. Puedes combinar estos elementos para crear aplicaciones más complejas.")

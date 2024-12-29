
import streamlit as st
from sidebar import sidebar_menu
from importlib import import_module
from homepage import show_home

# Configuración de la página
st.set_page_config(page_title="Cursos Streamlit", page_icon="📚", layout="wide")

def cargar_modulo_y_funcion(ruta_base, subcarpeta, archivo):
    """Carga dinámicamente un módulo y ejecuta una función basada en el nombre del archivo."""
    try:
        modulo = f"{ruta_base}.{subcarpeta.replace('/', '.')}.{archivo}"
        mod = import_module(modulo)
        funcion = getattr(mod, archivo, None)  # Busca una función con el nombre del archivo
        if funcion:
            funcion()
        else:
            st.error(f"El archivo {archivo}.py no contiene una función llamada `{archivo}`.")
    except ModuleNotFoundError as e:
        st.error(f"No se pudo cargar el módulo: {archivo}. Error: {e}")
    except Exception as e:
        st.error(f"Error al ejecutar el archivo {archivo}.py: {e}")

# Sidebar
menu, subcarpeta, archivo = sidebar_menu()

# Lógica del contenido principal
if menu == "Home":
    show_home()  # Llama a la función `show_home` desde homepage.py
elif subcarpeta and archivo:
    ruta_base = f"courses.{menu.lower()}"
    cargar_modulo_y_funcion(ruta_base, subcarpeta, archivo)

import streamlit as st
from sidebar import sidebar_menu
from homepage import homepage

# Importar páginas de los cursos
from pages.cloud.curso1.curso import cloud_curso1
from pages.cloud.curso2.curso import cloud_curso2

from pages.programacion.curso1.curso import programacion_curso1
from pages.programacion.curso2.curso import programacion_curso2

from pages.utilidades.curso1.curso import utilidades_curso1
from pages.utilidades.curso2.curso import utilidades_curso2

# Configuración de la página
st.set_page_config(page_title="Cursos Streamlit", page_icon="📚", layout="wide")

# Sidebar
menu, submenu = sidebar_menu()

# Lógica del contenido principal
if menu == "Home":
    homepage()

elif menu == "Cloud":
    if submenu == "Curso 1":
        cloud_curso1()
    elif submenu == "Curso 2":
        cloud_curso2()

elif menu == "Programación":
    if submenu == "Curso 1":
        programacion_curso1()
    elif submenu == "Curso 2":
        programacion_curso2()

elif menu == "Utilidades":
    if submenu == "Curso 1":
        utilidades_curso1()
    elif submenu == "Curso 2":
        utilidades_curso2()

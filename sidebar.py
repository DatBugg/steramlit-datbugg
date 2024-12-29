import os
import streamlit as st

def listar_estructura(carpeta_base):
    """Lista recursivamente las subcarpetas y archivos `.py` en una estructura ordenada."""
    estructura = {}
    for raiz, subcarpetas, archivos in os.walk(carpeta_base):
        carpeta_relativa = os.path.relpath(raiz, carpeta_base)
        if carpeta_relativa == ".":
            carpeta_relativa = ""  # Ignorar la raíz como un punto
        estructura[carpeta_relativa] = [archivo for archivo in archivos if archivo.endswith(".py")]
    return estructura

def sidebar_menu():
    st.sidebar.markdown(
        """
        <style>
        .sidebar-button {
            display: block;
            width: calc(100% - 20px);
            padding: 10px 15px;
            margin: 5px 0;
            text-align: left;
            border: none;
            outline: none;
            background-color: #f0f0f0;
            color: #000;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
        }
        .sidebar-button:hover {
            background-color: #ff4d4d;
            color: #fff;
        }
        .sidebar-submenu {
            margin-left: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Opciones principales
    opciones_principales = ["Home", "Cloud", "Programming", "Utilities"]
    for opcion in opciones_principales:
        if st.sidebar.button(opcion, key=f"main-{opcion.lower()}"):
            st.session_state["menu"] = opcion

    menu = st.session_state.get("menu", "Home")
    subcarpeta_seleccionada = None
    archivo_seleccionado = None

    st.sidebar.markdown("<h3 style='margin-top: 20px;'>Guides</h3>", unsafe_allow_html=True)

    carpeta_base = f"courses/{menu.lower()}"

    # Validar si la carpeta existe
    if os.path.exists(carpeta_base):
        estructura = listar_estructura(carpeta_base)
        subcarpetas = [sub for sub in estructura.keys() if sub]  # Evitar incluir la raíz vacía

        for subcarpeta in subcarpetas:
            if st.sidebar.button(subcarpeta, key=f"sub-{menu.lower()}-{subcarpeta}", help="Subcarpeta"):
                st.session_state["subcarpeta"] = subcarpeta

        subcarpeta_seleccionada = st.session_state.get("subcarpeta")

    st.sidebar.markdown("<h3 style='margin-top: 20px;'>Episode</h3>", unsafe_allow_html=True)

    if subcarpeta_seleccionada and subcarpeta_seleccionada in estructura:
        archivos = estructura[subcarpeta_seleccionada]
        for archivo in archivos:
            archivo_visible = archivo.replace(".py", "").replace("_", " ")
            if st.sidebar.button(
                archivo_visible, 
                key=f"file-{menu.lower()}-{subcarpeta_seleccionada}-{archivo}",
                help="Archivo del curso",
            ):
                archivo_seleccionado = archivo.replace(".py", "")

    return menu, subcarpeta_seleccionada, archivo_seleccionado

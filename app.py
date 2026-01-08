import streamlit as st
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="Geometría 3D",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("📐 App de Geometría 3D")
st.markdown("**Desarrollado por Ing Orlando Ramirez Rodriguez**  \n_The Bird Orla_ 🐦")

st.divider()

# ---------------- SELECCIÓN ----------------
figura = st.selectbox(
    "🔷 Seleccione un cuerpo geométrico:",
    ["Cubo 🧊", "Esfera ⚪"]
)

# ---------------- CUBO ----------------
if figura == "Cubo 🧊":
    st.subheader("🧊 Cubo")
    arista = st.slider("📏 Longitud de la arista", 0.1, 10.0, 2.0)

    volumen = arista ** 3
    area_lateral = 4 * arista ** 2
    area_total = 6 * arista ** 2

    col1, col2, col3 = st.columns(3)
    col1.metric("📦 Volumen", f"{volumen:.2f}")
    col2.metric("🟦 Área lateral", f"{area_lateral:.2f}")
    col3.metric("🟩 Área total", f"{area_total:.2f}")

    # Gráfica 3D del cubo
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = [0, arista]
    for s, e in [
        [(0,0,0),(arista,0,0)], [(0,arista,0),(arista,arista,0)],
        [(0,0,arista),(arista,0,arista)], [(0,arista,arista),(arista,arista,arista)],
        [(0,0,0),(0,arista,0)], [(arista,0,0),(arista,arista,0)],
        [(0,0,arista),(0,arista,arista)], [(arista,0,arista),(arista,arista,arista)],
        [(0,0,0),(0,0,arista)], [(arista,0,0),(arista,0,arista)],
        [(0,arista,0),(0,arista,arista)], [(arista,arista,0),(arista,arista,arista)]
    ]:
        ax.plot3D(*zip(s,e), color="deepskyblue", linewidth=3)

    ax.set_title("Cubo 3D", color="blue")
    ax.set_box_aspect([1,1,1])
    st.pyplot(fig)

# ---------------- ESFERA ----------------
elif figura == "Esfera ⚪":
    st.subheader("⚪ Esfera")
    radio = st.slider("📏 Radio de la esfera", 0.1, 10.0, 2.0)

    volumen = (4/3) * math.pi * radio ** 3
    area_lateral = 4 * math.pi * radio ** 2
    area_total = area_lateral  # en la esfera son iguales

    col1, col2, col3 = st.columns(3)
    col1.metric("📦 Volumen", f"{volumen:.2f}")
    col2.metric("🔵 Área lateral", f"{area_lateral:.2f}")
    col3.metric("🟣 Área total", f"{area_total:.2f}")

    # Gráfica 3D de la esfera
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)

    x = radio * np.outer(np.cos(u), np.sin(v))
    y = radio * np.outer(np.sin(u), np.sin(v))
    z = radio * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color="violet", alpha=0.8)
    ax.set_title("Esfera 3D", color="purple")
    ax.set_box_aspect([1,1,1])

    st.pyplot(fig)

st.divider()
st.caption("📚 Aprende geometría jugando con figuras en 3D")

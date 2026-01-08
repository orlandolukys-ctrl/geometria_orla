import streamlit as st
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="Geometría 3D",
    layout="centered"
)

st.title("📐 App de Geometría 3D")
st.markdown(
    "**Desarrollado por Ing Orlando Ramirez Rodriguez**  \n"
    "_The Bird Orla_ 🐦"
)

st.divider()

# ---------------- SELECCIÓN DE FIGURA ----------------
figura = st.selectbox(
    "🔷 Seleccione un cuerpo geométrico:",
    ["Cubo 🧊", "Esfera ⚪"]
)

# ===================== CUBO =====================
if figura == "Cubo 🧊":
    st.subheader("🧊 Cubo")

    arista = st.slider(
        "📏 Longitud de la arista (u)",
        min_value=0.1,
        max_value=10.0,
        value=2.0
    )

    volumen = arista ** 3
    area_lateral = 4 * arista ** 2
    area_total = 6 * arista ** 2

    col1, col2, col3 = st.columns(3)
    col1.metric("📦 Volumen", f"{volumen:.2f} u³")
    col2.metric("🟦 Área lateral", f"{area_lateral:.2f} u²")
    col3.metric("🟩 Área total", f"{area_total:.2f} u²")

    # -------- Gráfica 3D del Cubo --------
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    edges = [
        [(0,0,0),(arista,0,0)], [(0,arista,0),(arista,arista,0)],
        [(0,0,arista),(arista,0,arista)], [(0,arista,arista),(arista,arista,arista)],
        [(0,0,0),(0,arista,0)], [(arista,0,0),(arista,arista,0)],
        [(0,0,arista),(0,arista,arista)], [(arista,0,arista),(arista,arista,arista)],
        [(0,0,0),(0,0,arista)], [(arista,0,0),(arista,0,arista)],
        [(0,arista,0),(0,arista,arista)], [(arista,arista,0),(arista,arista,arista)]
    ]

    for edge in edges:
        ax.plot3D(*zip(*edge), color="deepskyblue", linewidth=3)

    ax.set_title("Cubo 3D", color="blue")
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    st.pyplot(fig)

# ===================== ESFERA =====================
elif figura == "Esfera ⚪":
    st.subheader("⚪ Esfera")

    radio = st.slider(
        "📏 Radio de la esfera (u)",
        min_value=0.1,
        max_value=10.0,
        value=2.0
    )

    volumen = (4 / 3) * math.pi * radio ** 3
    area_total = 4 * math.pi * radio ** 2

    col1, col2 = st.columns(2)
    col1.metric("📦 Volumen", f"{volumen:.2f} u³")
    col2.metric("🟣 Área total", f"{area_total:.2f} u²")

    # -------- Gráfica 3D de la Esfera --------
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    u = np.linspace(0, 2 * math.pi, 60)
    v = np.linspace(0, math.pi, 60)

    x = radio * np.outer(np.cos(u), np.sin(v))
    y = radio * np.outer(np.sin(u), np.sin(v))
    z = radio * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color="violet", alpha=0.85)

    ax.set_title("Esfera 3D", color="purple")
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    st.pyplot(fig)

# ---------------- PIE DIDÁCTICO ----------------
st.divider()
st.info("📌 u representa la unidad de longitud. Áreas en u² y volúmenes en u³.")
st.caption("📚 Aprende geometría jugando con cuerpos en 3D")



   
   
    
    

    

    

   

    

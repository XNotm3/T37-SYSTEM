import streamlit as st
import random

# === THEME T37 CYBERPUNK CIRCUIT BOARD ===
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
<style>
    /* Fondo circuitos neon ultra */
    .stApp {
        background-image: url("https://images.stockcake.com/public/d/d/7/dd7c8de0-80a7-4a1e-b49e-4ef9e4f740ab_large/neon-circuit-glow-stockcake.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Overlay oscuro con borde neon para contenido */
    .main > div {
        background-color: rgba(0, 5, 25, 0.8);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 2px solid #00ffea;
        box-shadow: 0 0 30px rgba(0, 255, 234, 0.5);
    }
    
    /* Texto neon glow intenso */
    h1, h2, h3, h4, .stMarkdown, label, .stCaption, .stText {
        color: #00ffea !important;
        text-shadow: 0 0 20px #00ffea, 0 0 10px #00ffff;
        font-family: 'Orbitron', 'Courier New', monospace !important;
    }
    
    h1 { font-size: 3.5rem !important; text-align: center; margin-bottom: 0.5rem; }
    h2 { font-size: 2.2rem !important; }
    
    /* Sliders con barra neon */
    .stSlider > div > div > div > div {
        background: linear-gradient(to right, #00ff41, #00ffff) !important;
        height: 8px !important;
        border-radius: 5px;
    }
    
    /* Botones neon verde */
    button[kind="primary"] {
        background: linear-gradient(#00ff41, #008822) !important;
        color: black !important;
        box-shadow: 0 0 25px #00ff41;
        border: none !important;
        font-weight: bold;
    }
    
    /* Sidebar cyber */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 15, 45, 0.95);
        border-right: 4px solid #00ffea;
        box-shadow: 0 0 30px rgba(0, 255, 234, 0.7);
    }
    
    /* Progress bars neon */
    .stProgress > div > div > div > div {
        background: linear-gradient(to right, #00ffff, #00ff41) !important;
    }
    
    /* Tabs neon */
    .stTabs [data-baseweb="tab"] {
        color: #00ffea !important;
        text-shadow: 0 0 10px #00ffea;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="T37 PERSONALITY SYSTEM", layout="wide")
st.title("🧠 T

import streamlit as st
import random

# === THEME T37 CYBERPUNK CIRCUIT BOARD ===
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
<style>
    /* Fondo circuit board cyberpunk high-res */
    .stApp {
        background-image: url("https://img.freepik.com/free-vector/realistic-neon-lights-background_23-2148904874.jpg?w=2000");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Overlay oscuro con borde neon */
    .main > div {
        background-color: rgba(0, 0, 20, 0.85);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        border: 3px solid #00ffea;
        box-shadow: 0 0 40px rgba(0, 255, 234, 0.6);
    }
    
    /* Texto neon glow */
    h1, h2, h3, h4, .stMarkdown, label, .stCaption, .stText {
        color: #00ffea !important;
        text-shadow: 0 0 25px #00ffea, 0 0 15px #00ffff;
        font-family: 'Orbitron', 'Courier New', monospace !important;
    }
    
    h1 { font-size: 3.8rem !important; text-align: center; }
    h2 { font-size: 2.4rem !important; }
    
    /* Sliders neon */
    .stSlider > div > div > div > div {
        background: linear-gradient(to right, #00ff41, #00ffff) !important;
        height: 10px !important;
        border-radius: 8px;
    }
    
    /* Botones neon */
    button[kind="primary"] {
        background: linear-gradient(#00ff41, #008822) !important;
        color: black !important;
        box-shadow: 0 0 30px #00ff41;
        border: none !important;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 15, 50, 0.95);
        border-right: 5px solid #00ffea;
        box-shadow: 0 0 40px rgba(0, 255, 234, 0.8);
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(to right, #00ffff, #00ff41) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        color: #00ffea !important;
        text-shadow: 0 0 15px #00ffea;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="T37 PERSONALITY SYSTEM", layout="wide")
st.title("🧠 T37 PERSONALITY SYSTEM")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO • TRANSFORMA TU SISTEMA PERSONAL**")
st.markdown("Diagnostica y optimiza tu mente como una motherboard futurista • Basado en Robert Sapolsky")
st.markdown("---")

# Inicializar sesión
if "perfiles_guardados" not in st.session_state:
    st.session_state.perfiles_guardados = {}

# Sidebar
st.sidebar.header("🎛️ MODOS RÁPIDOS")
presets = {
    "Ninguno": None,
    "🦸 TITÁN MÁXIMO": {"g":75,"n":70,"e":85,"c":85,"f":95,"h":95,"exp":85,"ent":90,"mom":95,"con":90},
    "🧘 SABIO ESTOICO": {"g":65,"n":75,"e":80,"c":90,"f":85,"h":80,"exp":85,"ent":70,"mom":90,"con":95},
    "🎨 FLOW CREATIVO": {"g":70,"n":65,"e":75,"c":80,"f":90,"h":75,"exp":80,"ent":85,"mom":95,"con":85},
    "😈 SUPERVIVENCIA": {"g":45,"n":40,"e":45,"c":50,"f":40,"h":45,"exp":55,"ent":35,"mom":40,"con":45},
    "⚡ SOCIAL CARISMÁTICO": {"g":75,"n":70,"e":80,"c":85,"f":85,"h":80,"exp":85,"ent":95,"mom":90,"con":80},
    "🌙 RECUPERACIÓN PROFUNDA": {"g":55,"n":60,"e":65,"c":70,"f":95,"h":65,"exp":70,"ent":60,"mom":85,"con":75},
}

preset = st.sidebar.selectbox("Selecciona modo", list(pres

import streamlit as st
import random

# === THEME T37 - FONDO NEGRO SÓLIDO + NEON SELECTIVO ===
st.markdown("""
<style>
    /* Fondo negro sólido */
    .stApp {
        background-color: #000000;
    }
    
    /* Contenido con fondo negro sutil */
    .main > div {
        background-color: rgba(10, 10, 10, 0.9);
        padding: 20px;
        border-radius: 15px;
    }
    
    /* Texto normal (blanco/gris claro, sin glow excepto título y resultados) */
    .stMarkdown, label, .stCaption, p, div {
        color: #e0e0e0 !important;
        font-family: 'Courier New', monospace;
    }
    
    /* Título principal y diagnóstico con neon azul */
    h1, .diagnostico-titulo {
        color: #00bfff !important;
        text-shadow: 0 0 20px #00bfff;
        text-align: center;
        font-size: 2.8rem !important;
    }
    
    h2 { font-size: 1.8rem !important; color: #ffffff; }
    
    /* Sliders neon por capa */
    /* Rojo para Núcleo */
    div[data-testid="stVerticalBlock"]:nth-child(1) .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ff0000, #ff5555) !important;
    }
    /* Naranja para Profundas */
    div[data-testid="stVerticalBlock"]:nth-child(2) .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ff8800, #ffaa55) !important;
    }
    /* Amarillo para Medias */
    div[data-testid="stVerticalBlock"]:nth-child(3) .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ffff00, #ffff77) !important;
    }
    /* Verde para Externas */
    div[data-testid="stVerticalBlock"]:nth-child(4) .stSlider > div > div > div > div {
        background: linear-gradient(to right, #00ff00, #55ff55) !important;
    }
    
    /* Progress bars neon azul suave */
    .stProgress > div > div > div > div {
        background: linear-gradient(to right, #00bfff, #0099ff) !important;
    }
    
    /* Sidebar negra */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="T37 PERSONALITY SYSTEM", layout="wide")
st.title("🧠 T37 PERSONALITY SYSTEM")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO**")
st.markdown("Diagnostica y transforma tu sistema personal")
st.markdown("---")

# Inicializar sesión
if "perfiles_guardados" not in st.session_state:
    st.session_state.perfiles_guardados = {}

# Sidebar
st.sidebar.header("MODOS RÁPIDOS")
presets = {
    "Ninguno": None,
    "🦸 TITÁN MÁXIMO": {"g":75,"n":70,"e":85,"c":85,"f":95,"h":95,"exp":85,"ent":90,"mom":95,"con":90},
    "🧘 SABIO ESTOICO": {"g":65,"n":75,"e":80,"c":90,"f":85,"h":80,"exp":85,"ent":70,"mom":90,"con":95},
    "🎨 FLOW CREATIVO": {"g":70,"n":65,"e":75,"c":80,"f":90,"h":75,"exp":80,"ent":85,"mom":95,"con":85},
    "😈 SUPERVIVENCIA": {"g":45,"n":40,"e":45,"c":50,"f":40,"h":45,"exp":55,"ent":35,"mom":40,"con":45},
    "⚡ SOCIAL CARISMÁTICO": {"g":75,"n":70,"e":80,"c":85,"f":85,"h":80,"exp":85,"ent":95,"mom":90,"con":80},
    "🌙 RECUPERACIÓN PROFUNDA": {"g":55,"n":60,"e":65,"c":70,"f":95,"h":65,"exp":70,"ent":60,"mom":85,"con":75},
}

preset = st.sidebar.selectbox("Selecciona modo", list(presets.keys()))

st.sidebar.markdown("---")
col1, col2 = st.sidebar.columns(2)
reset = col1.button("RESET")
randomize = col2.button("RANDOM")

st.sidebar.markdown("### PERFILES PERSONALES")
nombre = st.sidebar.text_input("Nombre para guardar")
guardar_btn = st.sidebar.button("GUARDAR ACTUAL")

cargar = st.sidebar.selectbox("Cargar perfil", [""] + list(st.session_state.perfiles_guardados.keys()))

# Defaults
defaults = {"g":50,"n":50,"e":60,"c":60,"f":70,"h":70,"exp":65,"ent":75,"mom":80,"con":60}

if preset != "Ninguno" and presets[preset] is not None:
    defaults.update(presets[preset])
if cargar:
    defaults.update(st.session_state.perfiles_guardados[cargar])

if reset:
    st.rerun()
if randomize:
    defaults = {k: random.randint(30,90) for k in defaults}
    st.rerun()

# Sliders con botón (?) de explicación
tab1, tab2, tab3, tab4 = st.tabs(["🔴 NÚCLEO", "🟠 PROFUNDAS", "🟡 MEDIAS", "🟢 EXTERNAS"])

with tab1:
    col_slider, col_help = st.columns([4,1])
    with col_slider:
        g = st.slider("GENÉTICA BASE", 0,100,defaults["g"], key="g")
    with col_help:
        with st.expander("?"):
            st.write("Tu hardware de fábrica: temperamento innato, resiliencia genética, predisposiciones. Casi inmodificable.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        n = st.slider("NEURODESARROLLO TEMPRANO",0,100,defaults["n"], key="n")
    with col_help:
        with st.expander("?"):
            st.write("Apego seguro, estrés 0-5 años. Fija

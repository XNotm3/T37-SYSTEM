import streamlit as st
import random

# === THEME T37 CYBERPUNK - FONDO NEGRO CON CIRCUITOS NEON AZULES ===
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
<style>
    /* Fondo negro sólido con circuitos neon azules */
    .stApp {
        background-image: url("https://images.stockcake.com/public/d/d/7/dd7c8de0-80a7-4a1e-b49e-4ef9e4f740ab_large/neon-circuit-glow-stockcake.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-color: #000000; /* Fallback negro sólido */
    }
    
    /* Overlay oscuro para contenido */
    .main > div {
        background-color: rgba(0, 0, 0, 0.85);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        border: 3px solid #00bfff; /* Borde azul neon */
        box-shadow: 0 0 40px rgba(0, 191, 255, 0.6);
    }
    
    /* Texto neon azul glow */
    h1, h2, h3, h4, .stMarkdown, label, .stCaption {
        color: #00bfff !important; /* Azul neon intenso */
        text-shadow: 0 0 25px #00bfff, 0 0 15px #0099ff;
        font-family: 'Orbitron', monospace !important;
    }
    
    h1 { font-size: 3.8rem !important; text-align: center; }
    
    /* Sliders neon azul */
    .stSlider > div > div > div > div {
        background: linear-gradient(to right, #00bfff, #0099ff) !important;
        height: 10px !important;
        border-radius: 8px;
    }
    
    /* Botones neon azul */
    button[kind="primary"] {
        background: linear-gradient(#00bfff, #0066cc) !important;
        color: white !important;
        box-shadow: 0 0 30px #00bfff;
        border: none !important;
        font-weight: bold;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 30, 0.95);
        border-right: 5px solid #00bfff;
        box-shadow: 0 0 40px rgba(0, 191, 255, 0.8);
    }
    
    /* Progress bars neon azul */
    .stProgress > div > div > div > div {
        background: linear-gradient(to right, #00bfff, #0099ff) !important;
    }
    
    /* Tabs neon azul */
    .stTabs [data-baseweb="tab"] {
        color: #00bfff !important;
        text-shadow: 0 0 15px #00bfff;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="T37 PERSONALITY SYSTEM", layout="wide")
st.title("🧠 T37 PERSONALITY SYSTEM")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO • TRANSFORMA TU SISTEMA**")
st.markdown("Diagnostica y optimiza tu mente como una motherboard futurista")
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

preset = st.sidebar.selectbox("Selecciona modo", list(presets.keys()))

st.sidebar.markdown("---")
col1, col2 = st.sidebar.columns(2)
reset = col1.button("🔄 RESET")
randomize = col2.button("🎲 RANDOM")

st.sidebar.markdown("### 💾 PERFILES PERSONALES")
nombre = st.sidebar.text_input("Nombre para guardar (ej: Objetivo 2026)")
guardar_btn = st.sidebar.button("GUARDAR ACTUAL")

cargar = st.sidebar.selectbox("Cargar perfil guardado", [""] + list(st.session_state.perfiles_guardados.keys()))

# Defaults
defaults = {"g":50,"n":50,"e":60,"c":60,"f":70,"h":70,"exp":65,"ent":75,"mom":80,"con":60}

# Aplicar preset o cargar
if preset != "Ninguno" and presets[preset] is not None:
    defaults.update(presets[preset])
if cargar:
    defaults.update(st.session_state.perfiles_guardados[cargar])

# Reset o Random
if reset:
    st.rerun()
if randomize:
    defaults = {k: random.randint(30,90) for k in defaults}
    st.rerun()

# Sliders
tab1, tab2, tab3, tab4 = st.tabs(["🔴 NÚCLEO", "🟠 PROFUNDAS", "🟡 MEDIAS", "🟢 EXTERNAS"])

with tab1:
    g = st.slider("GENÉTICA BASE", 0,100,defaults["g"],help="Hardware de fábrica. Temperamento innato.")
    n = st.slider("NEURODESARROLLO TEMPRANO",0,100,defaults["n"],help="Apego y estrés infantil.")

with tab2:
    e = st.slider("ESQUEMAS INFANCIA",0,100,defaults["e"],help="Creencias núcleo.")
    c = st.slider("NARRATIVA CULTURAL",0,100,defaults["c"],help="Valores absorbidos.")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        f = st.slider("FISIOLOGÍA ACTUAL",0,100,defaults["f"],help="Sueño, dieta, ejercicio.")
        h = st.slider("HÁBITOS DIARIOS",0,100,defaults["h"],help="Disciplina y rutinas.")
    with col2:
        exp = st.slider("EXPERIENCIAS ADULTAS",0,100,defaults["exp"],help="Relaciones y logros/traumas.")

with tab4:
    ent = st.slider("ENTORNO INMEDIATO",0,100,defaults["ent"],help="Personas y espacio.")
    mom = st.slider("ESTADO MOMENTO",0,100,defaults["mom"],help="Energía actual.")
    con = st.slider("CONCIENCIA INTERNA",0,100,defaults["con"],help="Meditación y terapia.")

# Guardar perfil
if guardar_btn and nombre:
    datos = {"g":g,"n":n,"e":e,"c":c,"f":f,"h":h,"exp":exp,"ent":ent,"mom":mom,"con":con}
    st.session_state.perfiles_guardados[nombre] = datos
    st.sidebar.success(f"Guardado: {nombre}")

st.markdown("---")
st.header("🧬 DIAGNÓSTICO DE SISTEMA")

# Cálculo
rango = g/100*0.7 + n/100*0.3
creencias = (e+c)/200
medio = (f+h+exp)/300
externo = (ent+mom)/200
amp = (con/100)**0.6
score = (rango*0.35 + creencias*0.15 + medio*0.25 + externo*0.25)*100*amp

rasgos = {
    "RESILIENCIA": round(rango*50 + medio*40 + con/100*10,1),
    "FOCO": round(h/100*60 + f/100*30 + mom/100*10,1),
    "EMPATÍA": round(creencias*40 + ent/100*40 + c/100*20,1),
    "CREATIVIDAD": round(g/100*30 + externo*50 + con/100*20,1),
    "BAJA ANSIEDAD": round(100 - (n/100*40 + f/100*40 + ent/100*20),1),
    "AUTOESTIMA": round(e/100*50 + exp/100*40 + con/100*10,1),
}

if score >= 90: perfil, emoji = "TITÁN OPTIMIZADO", "🦸"
elif score >= 80: perfil, emoji = "ALTO RENDIMIENTO", "⚡"
elif score >= 65: perfil, emoji = "EQUILIBRADO", "🟢"
elif score >= 50: perfil, emoji = "SUPERVIVENCIA", "🟡"
elif score >= 35: perfil, emoji = "REACTIVO", "🟠"
else: perfil, emoji = "SOBRECARGA", "🔴"

col1, col2 = st.columns([1,3])
with col1:
    st.markdown(f"<h1 style='text-align:center'>{emoji}<br>{perfil}</h1>", unsafe_allow_html=True)
    st.progress(score/100)
    st.metric("GLOBAL", f"{score:.1f}/100")

with col2:
    st.subheader("RADAR DE RASGOS")
    for rasgo, val in rasgos.items():
        st.progress(val/100)
        st.write(f"**{rasgo}**: {val}/100")

st.subheader("DESCRIPCIÓN")
desc = {
    "TITÁN OPTIMIZADO": "Sistema al máximo. Flujo y claridad total.",
    "ALTO RENDIMIENTO": "Energía óptima y regulación perfecta.",
    "EQUILIBRADO": "Funcionamiento sólido con potencial alto.",
    "SUPERVIVENCIA": "Operativo pero forzado.",
    "REACTIVO": "Alta carga emocional.",
    "SOBRECARGA": "Sistema en riesgo."
}
st.write(desc[perfil])

st.success(f"**BOTTLENECK**: {min(rasgos, key=rasgos.get)} → Prioriza esta área")

st.info("💡 CONSEJO: " + random.choice(["Fisiología primero", "Conciencia amplifica todo", "Limpia entorno", "Maximiza lo modificable"]))

st.caption("T37 PERSONALITY SYSTEM v4.0 • Neon Blue Circuit Edition")

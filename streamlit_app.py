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
    /* Rojo para Núcleo (tab 1) */
    div[data-testid="stTab"]:nth-child(1) ~ div .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ff0000, #ff5555) !important;
    }
    /* Naranja para Profundas (tab 2) */
    div[data-testid="stTab"]:nth-child(2) ~ div .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ff8800, #ffaa55) !important;
    }
    /* Amarillo para Medias (tab 3) */
    div[data-testid="stTab"]:nth-child(3) ~ div .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ffff00, #ffff77) !important;
    }
    /* Verde para Externas (tab 4) */
    div[data-testid="stTab"]:nth-child(4) ~ div .stSlider > div > div > div > div {
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
            st.write("""Tu hardware de fábrica: temperamento innato, resiliencia genética, predisposiciones. Casi inmodificable.""")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        n = st.slider("NEURODESARROLLO TEMPRANO",0,100,defaults["n"], key="n")
    with col_help:
        with st.expander("?"):
            st.write("""Apego seguro, estrés 0-5 años. Fija límites emocionales profundos.""")

with tab2:
    col_slider, col_help = st.columns([4,1])
    with col_slider:
        e = st.slider("ESQUEMAS INFANCIA",0,100,defaults["e"], key="e")
    with col_help:
        with st.expander("?"):
            st.write("""Creencias núcleo sobre ti y el mundo. Cambiable con terapia profunda.""")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        c = st.slider("NARRATIVA CULTURAL",0,100,defaults["c"], key="c")
    with col_help:
        with st.expander("?"):
            st.write("""Valores, ideología, expectativas sociales absorbidas.""")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        col_slider, col_help = st.columns([4,1])
        with col_slider:
            f = st.slider("FISIOLOGÍA ACTUAL",0,100,defaults["f"], key="f")
        with col_help:
            with st.expander("?"):
                st.write("""Sueño, hormonas, dieta, ejercicio. Impacto rápido y potente.""")

        col_slider, col_help = st.columns([4,1])
        with col_slider:
            h = st.slider("HÁBITOS DIARIOS",0,100,defaults["h"], key="h")
        with col_help:
            with st.expander("?"):
                st.write("""Disciplina, rutinas. Tu mayor palanca de cambio a largo plazo.""")

    with col2:
        col_slider, col_help = st.columns([4,1])
        with col_slider:
            exp = st.slider("EXPERIENCIAS ADULTAS",0,100,defaults["exp"], key="exp")
        with col_help:
            with st.expander("?"):
                st.write("""Relaciones, logros y traumas recientes que moldean tu identidad actual.""")

with tab4:
    col_slider, col_help = st.columns([4,1])
    with col_slider:
        ent = st.slider("ENTORNO INMEDIATO",0,100,defaults["ent"], key="ent")
    with col_help:
        with st.expander("?"):
            st.write("""Personas, contenido consumido, espacio físico. Cambia rápido.""")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        mom = st.slider("ESTADO MOMENTO",0,100,defaults["mom"], key="mom")
    with col_help:
        with st.expander("?"):
            st.write("""Energía actual, glucosa, postura. Fluctúa hora a hora.""")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        con = st.slider("CONCIENCIA INTERNA",0,100,defaults["con"], key="con")
    with col_help:
        with st.expander("?"):
            st.write("""Meditación, terapia, reflexión. Amplifica todos los cambios.""")

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

# Resultados con neon solo aquí
st.markdown(f"<h1 class='diagnostico-titulo'>{emoji} {perfil}</h1>", unsafe_allow_html=True)
st.progress(score/100)
st.metric("GLOBAL", f"{score:.1f}/100")

st.subheader("RADAR DE RASGOS")
for rasgo, val in rasgos.items():
    st.progress(val/100)
    st.caption(f"**{rasgo}**: {val}/100")

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

st.caption("T37 PERSONALITY SYSTEM v4.1 • Clean Black Edition")

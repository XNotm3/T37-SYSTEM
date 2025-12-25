import streamlit as st
import random

# === THEME T37 - FONDO NEGRO SÓLIDO + NEON SELECTIVO ===
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    .main > div {
        background-color: rgba(10, 10, 10, 0.9);
        padding: 20px;
        border-radius: 15px;
    }
    .stMarkdown, label, .stCaption {
        color: #e0e0e0 !important;
        font-family: 'Courier New', monospace;
    }
    h1, .diagnostico-titulo {
        color: #00bfff !important;
        text-shadow: 0 0 20px #00bfff;
        text-align: center;
        font-size: 2.8rem !important;
    }
    h2 { font-size: 1.8rem !important; color: #ffffff; }
    .stProgress > div > div > div > div {
        background: linear-gradient(to right, #00bfff, #0099ff) !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="T37 PERSONALITY SYSTEM", layout="wide")
st.title("🧠 T37 PERSONALITY SYSTEM")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO**")
st.markdown("Cada capa se desglosa en componentes. El slider principal muestra la media automática.")
st.markdown("---")

# Inicializar sesión
if "perfiles_guardados" not in st.session_state:
    st.session_state.perfiles_guardados = {}

# Sidebar
st.sidebar.header("MODOS RÁPIDOS")
presets = {
    "Ninguno": None,
    "🦸 TITÁN MÁXIMO": {"g1":70,"g2":80,"p1":75,"p2":70,"p3":80,"m1":90,"m2":95,"m3":85,"e1":90,"e2":90,"e3":90,"mom":95,"con":90},
    "🧘 SABIO ESTOICO": {"g1":60,"g2":70,"p1":80,"p2":75,"p3":85,"m1":85,"m2":80,"m3":85,"e1":70,"e2":70,"e3":70,"mom":90,"con":95},
    "🎨 FLOW CREATIVO": {"g1":65,"g2":75,"p1":70,"p2":75,"p3":80,"m1":90,"m2":75,"m3":80,"e1":85,"e2":85,"e3":85,"mom":95,"con":85},
    "😈 SUPERVIVENCIA": {"g1":40,"g2":50,"p1":45,"p2":40,"p3":50,"m1":40,"m2":45,"m3":55,"e1":35,"e2":30,"e3":40,"mom":40,"con":45},
    "⚡ SOCIAL CARISMÁTICO": {"g1":75,"g2":70,"p1":80,"p2":80,"p3":85,"m1":85,"m2":80,"m3":85,"e1":95,"e2":95,"e3":90,"mom":90,"con":80},
    "🌙 RECUPERACIÓN": {"g1":55,"g2":60,"p1":65,"p2":65,"p3":70,"m1":95,"m2":65,"m3":70,"e1":60,"e2":60,"e3":60,"mom":85,"con":75},
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

# Defaults detallados
defaults = {
    "g1":50, "g2":50,  # Núcleo
    "p1":60, "p2":60, "p3":60,  # Profundas
    "m1":70, "m2":70, "m3":65,  # Medias
    "e1":75, "e2":75, "e3":75,  # Externas entorno
    "mom":80, "con":60
}

if preset != "Ninguno" and presets[preset] is not None:
    defaults.update(presets[preset])
if cargar:
    defaults.update(st.session_state.perfiles_guardados[cargar])

if reset:
    st.rerun()
if randomize:
    defaults = {k: random.randint(30,90) for k in defaults}
    st.rerun()

# Tabs con capas desglosadas
tab1, tab2, tab3, tab4 = st.tabs(["🔴 NÚCLEO", "🟠 PROFUNDAS", "🟡 MEDIAS", "🟢 EXTERNAS"])

# 🔴 NÚCLEO (5-10% modificable)
with tab1:
    st.markdown("**MODIFICABILIDAD: 5-10%** (casi inmodificable – futuro edición genética)")
    nucleo_global = (defaults.get("g1",50) + defaults.get("g2",50)) / 2
    st.slider("NÚCLEO GLOBAL", 0,100, int(nucleo_global), disabled=True)

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        g1 = st.slider("GENÉTICA HEREDADA", 0,100,defaults["g1"], key="g1")
    with col_help:
        with st.expander("?"):
            st.write("Temperamento innato, predisposiciones genéticas (ej. ansiedad, impulsividad).")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        g2 = st.slider("EXPOSICIÓN PRENATAL", 0,100,defaults["g2"], key="g2")
    with col_help:
        with st.expander("?"):
            st.write("Nutrición materna, estrés en útero, hormonas fetales.")

# 🟠 PROFUNDAS (20-40% modificable)
with tab2:
    st.markdown("**MODIFICABILIDAD: 20-40%** (con terapia profunda y tiempo)")
    profundas_global = (defaults.get("p1",60) + defaults.get("p2",60) + defaults.get("p3",60)) / 3
    st.slider("PROFUNDAS GLOBAL", 0,100, int(profundas_global), disabled=True)

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        p1 = st.slider("APEGO TEMPRANO (0-5 años)", 0,100,defaults["p1"], key="p1")
    with col_help:
        with st.expander("?"):
            st.write("Calidad del vínculo con cuidadores. Cableado básico de seguridad emocional.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        p2 = st.slider("ESQUEMAS INFANCIA/ADOLESCENCIA", 0,100,defaults["p2"], key="p2")
    with col_help:
        with st.expander("?"):
            st.write("Creencias núcleo sobre uno mismo y el mundo (ej. 'no soy suficiente').")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        p3 = st.slider("NARRATIVA CULTURAL", 0,100,defaults["p3"], key="p3")
    with col_help:
        with st.expander("?"):
            st.write("Valores, religión, normas de género absorbidas.")

# 🟡 MEDIAS (60-80% modificable)
with tab3:
    st.markdown("**MODIFICABILIDAD: 60-80%** (con disciplina y hábitos consistentes)")
    medias_global = (defaults.get("m1",70) + defaults.get("m2",70) + defaults.get("m3",65)) / 3
    st.slider("MEDIAS GLOBAL", 0,100, int(medias_global), disabled=True)

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        m1 = st.slider("FISIOLOGÍA ACTUAL", 0,100,defaults["m1"], key="m1")
    with col_help:
        with st.expander("?"):
            st.write("Sueño, hormonas, dieta, ejercicio. Impacto rápido.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        m2 = st.slider("HÁBITOS DIARIOS", 0,100,defaults["m2"], key="m2")
    with col_help:
        with st.expander("?"):
            st.write("Rutinas, disciplina, productividad entrenada.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        m3 = st.slider("EXPERIENCIAS ADULTAS ACUMULADAS", 0,100,defaults["m3"], key="m3")
    with col_help:
        with st.expander("?"):
            st.write("Relaciones, éxitos/fracasos laborales recientes.")

# 🟢 EXTERNAS (90-100% modificable)
with tab4:
    st.markdown("**MODIFICABILIDAD: 90-100%** (cambio rápido y accesible)")
    externas_global = (defaults.get("e1",75) + defaults.get("e2",75) + defaults.get("e3",75) + defaults.get("mom",80) + defaults.get("con",60)) / 5
    st.slider("EXTERNAS GLOBAL", 0,100, int(externas_global), disabled=True)

    st.markdown("**ENTORNO INMEDIATO**")
    entorno_global = (defaults.get("e1",75) + defaults.get("e2",75) + defaults.get("e3",75)) / 3
    st.slider("ENTORNO GLOBAL", 0,100, int(entorno_global), disabled=True)

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        e1 = st.slider("PERSONAS CERCANAS", 0,100,defaults["e1"], key="e1")
    with col_help:
        with st.expander("?"):
            st.write("Calidad emocional de familia, pareja, amigos.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        e2 = st.slider("CONTENIDO CONSUMIDO", 0,100,defaults["e2"], key="e2")
    with col_help:
        with st.expander("?"):
            st.write("Redes, noticias, libros, música. Lo que entra moldea tu mente.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        e3 = st.slider("ESPACIO FÍSICO", 0,100,defaults["e3"], key="e3")
    with col_help:
        with st.expander("?"):
            st.write("Orden, luz, ruido, ergonomía del entorno.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        mom = st.slider("ESTADO MOMENTO-A-MOMENTO", 0,100,defaults["mom"], key="mom")
    with col_help:
        with st.expander("?"):
            st.write("Glucosa, fatiga, postura actual. Fluctúa rápido.")

    col_slider, col_help = st.columns([4,1])
    with col_slider:
        con = st.slider("CONCIENCIA INTERNA", 0,100,defaults["con"], key="con")
    with col_help:
        with st.expander("?"):
            st.write("Meditación, terapia, reflexión. Amplificador universal.")

# Guardar perfil
if guardar_btn and nombre:
    datos = {k:v for k, v in locals().items() if k in defaults}
    st.session_state.perfiles_guardados[nombre] = datos
    st.sidebar.success(f"Guardado: {nombre}")

st.markdown("---")
st.header("🧬 DIAGNÓSTICO DE SISTEMA")

# Cálculo con nuevas variables
nucleo = (g1 + g2) / 2 / 100
profundas = (p1 + p2 + p3) / 3 / 100
medias = (m1 + m2 + m3) / 3 / 100
externas = ((e1 + e2 + e3)/3 + mom + con) / 3 / 100

amp = (con / 100) ** 0.6

score = (nucleo * 0.25 + profundas * 0.20 + medias * 0.30 + externas * 0.25) * 100 * amp

rasgos = {
    "RESILIENCIA": round(nucleo*50 + medias*40 + con/100*10,1),
    "FOCO": round(m2/100*60 + m1/100*30 + mom/100*10,1),
    "EMPATÍA": round(profundas*40 + (e1+e2+e3)/300*40,1),
    "CREATIVIDAD": round(nucleo*30 + externas*50 + con/100*20,1),
    "BAJA ANSIEDAD": round(100 - (nucleo*40 + m1/100*40 + (e1+e2+e3)/300*20),1),
    "AUTOESTIMA": round(profundas*50 + m3/100*40 + con/100*10,1),
}

if score >= 90: perfil, emoji = "TITÁN OPTIMIZADO", "🦸"
elif score >= 80: perfil, emoji = "ALTO RENDIMIENTO", "⚡"
elif score >= 65: perfil, emoji = "EQUILIBRADO", "🟢"
elif score >= 50: perfil, emoji = "SUPERVIVENCIA", "🟡"
elif score >= 35: perfil, emoji = "REACTIVO", "🟠"
else: perfil, emoji = "SOBRECARGA", "🔴"

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

st.info("💡 CONSEJO: Las capas externas son tu mayor palanca ahora mismo.")

st.caption("T37 PERSONALITY SYSTEM v5.0 • Edición Desglosada por Componentes")

import streamlit as st
import random

# === THEME T37 - FONDO NEGRO SÓLIDO + NEON SELECTIVO ===
st.markdown("""
<style>
    /* Fondo negro sólido */
    .stApp { background-color: #000000; }
    
    /* Contenido principal */
    .main > div {
        background-color: rgba(10, 10, 10, 0.9);
        padding: 20px;
        border-radius: 15px;
    }
    
    /* Texto general */
    .stMarkdown, label, .stCaption, p {
        color: #e0e0e0 !important;
        font-family: 'Courier New', monospace;
    }
    
    /* Título y diagnóstico con neon azul */
    h1, .diagnostico-titulo {
        color: #00bfff !important;
        text-shadow: 0 0 20px #00bfff;
        text-align: center;
        font-size: 2.8rem !important;
    }
    
    h2 { font-size: 1.8rem !important; color: #ffffff; }
    
    /* Progress bars neon azul */
    .stProgress > div > div > div > div {
        background: linear-gradient(to right, #00bfff, #0099ff) !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #00bfff;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="T37 PERSONALITY SYSTEM", layout="wide")
st.title("🧠 T37 PERSONALITY SYSTEM v6.0")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO • TRANSFORMA TU SISTEMA PERSONAL**")
st.markdown("Cada capa se desglosa en sus componentes causales más potentes. El slider global muestra la media automática.")
st.markdown("---")

# === Estado de sesión centralizado ===
if "values" not in st.session_state:
    st.session_state.values = {}
if "perfiles" not in st.session_state:
    st.session_state.perfiles = {}

# === Valores por defecto ===
default_values = {
    # Núcleo
    "gen_heredada": 50, "exp_prenatal": 50, "neuro_critico": 50,
    # Profundas
    "estilo_apego": 60, "esquemas_maladapt": 60, "narrativa_cultural": 60,
    # Medias
    "fisiologia_actual": 70, "habitos_ejecutivos": 70, "exp_adultas": 65,
    # Externas
    "personas_cercanas": 75, "contenido_consumido": 75, "espacio_fisico": 75,
    "estado_momento": 80, "conciencia_interna": 60
}

# Inicializar valores si no existen
for key, val in default_values.items():
    if key not in st.session_state.values:
        st.session_state.values[key] = val

# === Sidebar ===
st.sidebar.header("🎛️ MODOS RÁPIDOS")
presets = {
    "Ninguno": None,
    "🦸 TITÁN MÁXIMO": {"gen_heredada":75,"exp_prenatal":70,"neuro_critico":70,"estilo_apego":85,"esquemas_maladapt":85,"narrativa_cultural":85,"fisiologia_actual":95,"habitos_ejecutivos":95,"exp_adultas":85,"personas_cercanas":90,"contenido_consumido":90,"espacio_fisico":90,"estado_momento":95,"conciencia_interna":90},
    "🧘 SABIO ESTOICO": {"gen_heredada":65,"exp_prenatal":70,"neuro_critico":75,"estilo_apego":80,"esquemas_maladapt":75,"narrativa_cultural":90,"fisiologia_actual":85,"habitos_ejecutivos":80,"exp_adultas":85,"personas_cercanas":70,"contenido_consumido":70,"espacio_fisico":70,"estado_momento":90,"conciencia_interna":95},
    "🎨 FLOW CREATIVO": {"gen_heredada":70,"exp_prenatal":65,"neuro_critico":65,"estilo_apego":75,"esquemas_maladapt":75,"narrativa_cultural":80,"fisiologia_actual":90,"habitos_ejecutivos":75,"exp_adultas":80,"personas_cercanas":85,"contenido_consumido":85,"espacio_fisico":85,"estado_momento":95,"conciencia_interna":85},
    "😈 SUPERVIVENCIA": {"gen_heredada":45,"exp_prenatal":50,"neuro_critico":40,"estilo_apego":45,"esquemas_maladapt":40,"narrativa_cultural":50,"fisiologia_actual":40,"habitos_ejecutivos":45,"exp_adultas":55,"personas_cercanas":35,"contenido_consumido":30,"espacio_fisico":40,"estado_momento":40,"conciencia_interna":45},
    "⚡ SOCIAL CARISMÁTICO": {"gen_heredada":75,"exp_prenatal":70,"neuro_critico":70,"estilo_apego":80,"esquemas_maladapt":80,"narrativa_cultural":85,"fisiologia_actual":85,"habitos_ejecutivos":80,"exp_adultas":85,"personas_cercanas":95,"contenido_consumido":95,"espacio_fisico":90,"estado_momento":90,"conciencia_interna":80},
    "🌙 RECUPERACIÓN PROFUNDA": {"gen_heredada":55,"exp_prenatal":60,"neuro_critico":60,"estilo_apego":65,"esquemas_maladapt":65,"narrativa_cultural":70,"fisiologia_actual":95,"habitos_ejecutivos":65,"exp_adultas":70,"personas_cercanas":60,"contenido_consumido":60,"espacio_fisico":60,"estado_momento":85,"conciencia_interna":75},
}

preset = st.sidebar.selectbox("Selecciona modo", list(presets.keys()))

st.sidebar.markdown("---")
col1, col2 = st.sidebar.columns(2)
reset = col1.button("RESET")
randomize = col2.button("RANDOM")

st.sidebar.markdown("### PERFILES PERSONALES")
nombre = st.sidebar.text_input("Nombre para guardar")
if st.sidebar.button("GUARDAR ACTUAL") and nombre:
    st.session_state.perfiles[nombre] = st.session_state.values.copy()
    st.sidebar.success(f"Guardado: {nombre}")

cargar = st.sidebar.selectbox("Cargar perfil", [""] + list(st.session_state.perfiles.keys()))

# Aplicar preset o carga
if preset != "Ninguno" and presets[preset]:
    st.session_state.values.update(presets[preset])
if cargar:
    st.session_state.values.update(st.session_state.perfiles[cargar])

if reset:
    st.session_state.values = default_values.copy()
    st.rerun()
if randomize:
    st.session_state.values = {k: random.randint(30,90) for k in default_values}
    st.rerun()

# === Tabs con capas desglosadas ===
tab1, tab2, tab3, tab4 = st.tabs(["🔴 NÚCLEO", "🟠 PROFUNDAS", "🟡 MEDIAS", "🟢 EXTERNAS"])

# 🔴 NÚCLEO
with tab1:
    st.markdown("**MODIFICABILIDAD: 5-10%** – Casi inmodificable (futuro edición genética/epigenética)")
    nucleo_media = (st.session_state.values["gen_heredada"] + st.session_state.values["exp_prenatal"] + st.session_state.values["neuro_critico"]) / 3
    st.slider("NÚCLEO GLOBAL", 0, 100, int(nucleo_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["gen_heredada"] = st.slider("GENÉTICA HEREDADA", 0,100,st.session_state.values["gen_heredada"])
    with col_h:
        with st.expander("?"):
            st.write("Variantes genéticas clave (serotonina, dopamina, CRHR1). Temperamento y resiliencia base.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["exp_prenatal"] = st.slider("EXPOSICIÓN PRENATAL", 0,100,st.session_state.values["exp_prenatal"])
    with col_h:
        with st.expander("?"):
            st.write("Estrés materno, hormonas fetales, nutrición en útero. Impacto permanente.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["neuro_critico"] = st.slider("NEURODESARROLLO CRÍTICO (0-3 años)", 0,100,st.session_state.values["neuro_critico"])
    with col_h:
        with st.expander("?"):
            st.write("Cableado permanente de amígdala y prefrontal. Volumen y conectividad base.")

# 🟠 PROFUNDAS
with tab2:
    st.markdown("**MODIFICABILIDAD: 20-40%** – Requiere terapia profunda y tiempo")
    profundas_media = (st.session_state.values["estilo_apego"] + st.session_state.values["esquemas_maladapt"] + st.session_state.values["narrativa_cultural"]) / 3
    st.slider("PROFUNDAS GLOBAL", 0, 100, int(profundas_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["estilo_apego"] = st.slider("ESTILO DE APEGO", 0,100,st.session_state.values["estilo_apego"])
    with col_h:
        with st.expander("?"):
            st.write("Seguro, ansioso, evitante o desorganizado. Modelo relacional internalizado.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["esquemas_maladapt"] = st.slider("ESQUEMAS MALADAPTATIVOS", 0,100,st.session_state.values["esquemas_maladapt"])
    with col_h:
        with st.expander("?"):
            st.write("Creencias núcleo negativas (abandono, defectuosidad, perfeccionismo).")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["narrativa_cultural"] = st.slider("NARRATIVA CULTURAL", 0,100,st.session_state.values["narrativa_cultural"])
    with col_h:
        with st.expander("?"):
            st.write("Valores de éxito, género, moral religiosa o política internalizada.")

# 🟡 MEDIAS
with tab3:
    st.markdown("**MODIFICABILIDAD: 60-80%** – Con disciplina y hábitos consistentes")
    medias_media = (st.session_state.values["fisiologia_actual"] + st.session_state.values["habitos_ejecutivos"] + st.session_state.values["exp_adultas"]) / 3
    st.slider("MEDIAS GLOBAL", 0, 100, int(medias_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["fisiologia_actual"] = st.slider("FISIOLOGÍA ACTUAL", 0,100,st.session_state.values["fisiologia_actual"])
    with col_h:
        with st.expander("?"):
            st.write("Sueño, inflamación, eje HPA, niveles hormonales. Estado bioquímico del momento.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["habitos_ejecutivos"] = st.slider("HÁBITOS EJECUTIVOS", 0,100,st.session_state.values["habitos_ejecutivos"])
    with col_h:
        with st.expander("?"):
            st.write("Control de impulsos, planificación, perseverancia entrenada.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["exp_adultas"] = st.slider("EXPERIENCIAS ADULTAS REFORZANTES", 0,100,st.session_state.values["exp_adultas"])
    with col_h:
        with st.expander("?"):
            st.write("Éxitos repetidos o fracasos que moldean identidad actual.")

# 🟢 EXTERNAS
with tab4:
    st.markdown("**MODIFICABILIDAD: 90-100%** – Cambio rápido y accesible")
    entorno_media = (st.session_state.values["personas_cercanas"] + st.session_state.values["contenido_consumido"] + st.session_state.values["espacio_fisico"]) / 3
    st.slider("ENTORNO GLOBAL", 0, 100, int(entorno_media), disabled=True)

    externas_media = (entorno_media + st.session_state.values["estado_momento"] + st.session_state.values["conciencia_interna"]) / 3
    st.slider("EXTERNAS GLOBAL", 0, 100, int(externas_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["personas_cercanas"] = st.slider("PERSONAS CERCANAS", 0,100,st.session_state.values["personas_cercanas"])
    with col_h:
        with st.expander("?"):
            st.write("Calidad emocional diaria de relaciones cercanas.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["contenido_consumido"] = st.slider("CONTENIDO CONSUMIDO", 0,100,st.session_state.values["contenido_consumido"])
    with col_h:
        with st.expander("?"):
            st.write("Redes, noticias, conversaciones. Priming cognitivo constante.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["espacio_fisico"] = st.slider("ESPACIO FÍSICO", 0,100,st.session_state.values["espacio_fisico"])
    with col_h:
        with st.expander("?"):
            st.write("Orden, luz, ruido, ergonomía. Impacto sensorial continuo.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["estado_momento"] = st.slider("ESTADO MOMENTO-A-MOMENTO", 0,100,st.session_state.values["estado_momento"])
    with col_h:
        with st.expander("?"):
            st.write("Glucosa, fatiga, postura. Priming corporal inmediato.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        st.session_state.values["conciencia_interna"] = st.slider("CONCIENCIA INTERNA", 0,100,st.session_state.values["conciencia_interna"])
    with col_h:
        with st.expander("?"):
            st.write("Meditación, terapia, metacognición. Amplificador de todas las capas modificables.")

st.markdown("---")
st.header("🧬 DIAGNÓSTICO DE SISTEMA")

# Cálculo preciso
v = st.session_state.values

nucleo = (v["gen_heredada"] + v["exp_prenatal"] + v["neuro_critico"]) / 3 / 100
profundas = (v["estilo_apego"] + v["esquemas_maladapt"] + v["narrativa_cultural"]) / 3 / 100
medias = (v["fisiologia_actual"] + v["habitos_ejecutivos"] + v["exp_adultas"]) / 3 / 100
entorno = (v["personas_cercanas"] + v["contenido_consumido"] + v["espacio_fisico"]) / 3 / 100
externas = (entorno + v["estado_momento"] / 100 + v["conciencia_interna"] / 100) / 3

amp = (v["conciencia_interna"] / 100) ** 0.6

score = (nucleo * 0.25 + profundas * 0.20 + medias * 0.30 + externas * 0.25) * 100 * amp

# Rasgos
rasgos = {
    "RESILIENCIA": round(nucleo*60 + medias*30 + v["conciencia_interna"]/100*10,1),
    "FOCO": round(v["habitos_ejecutivos"]/100*60 + v["fisiologia_actual"]/100*30 + v["estado_momento"]/100*10,1),
    "EMPATÍA": round(profundas*50 + entorno*40 + v["conciencia_interna"]/100*10,1),
    "CREATIVIDAD": round(nucleo*30 + externas*50 + v["conciencia_interna"]/100*20,1),
    "BAJA ANSIEDAD": round(100 - (nucleo*40 + v["fisiologia_actual"]/100*40 + entorno*20),1),
    "AUTOESTIMA": round(profundas*50 + v["exp_adultas"]/100*40 + v["conciencia_interna"]/100*10,1),
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
    "TITÁN OPTIMIZADO": "Operas cerca del máximo de tu rango genético. Flujo, resiliencia y claridad sostenida.",
    "ALTO RENDIMIENTO": "Energía abundante, foco consistente y regulación emocional óptima.",
    "EQUILIBRADO": "Funcionamiento sólido con amplio margen para upgrades.",
    "SUPERVIVENCIA": "Operativo pero con esfuerzo. Prioriza recuperación.",
    "REACTIVO": "Alta reactividad emocional. Intervención urgente en fisiología y entorno.",
    "SOBRECARGA": "Sistema en riesgo. Modo protección: descanso y aislamiento de estresores."
}
st.write(desc[perfil])

bottleneck = min(rasgos, key=rasgos.get)
st.success(f"**BOTTLENECK**: {bottleneck} → Ataca primero esta área")

st.info("💡 CONSEJO: Las capas externas y medias son tu mayor palanca de cambio inmediato.")

st.caption("T37 PERSONALITY SYSTEM v6.0 • Edición Causal Profunda • Tu herramienta de transformación real")

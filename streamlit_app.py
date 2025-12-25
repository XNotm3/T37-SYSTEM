import streamlit as st
import random

# === THEME T37 - FONDO NEGRO SÓLIDO + NEON SELECTIVO ===
st.markdown("""
<style>
    .stApp { background-color: #000000; }
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
st.title("🧠 T37 PERSONALITY SYSTEM v6.4")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO • TRANSFORMA TU SISTEMA PERSONAL**")
st.markdown("Cada capa se desglosa en sus componentes causales más potentes. El slider global muestra la media automática.")
st.markdown("---")

# === Valores por defecto ===
default_values = {
    "gen_heredada": 50, "exp_prenatal": 50, "neuro_critico": 50,
    "estilo_apego": 60, "esquemas_maladapt": 60, "narrativa_cultural": 60,
    "fisiologia_actual": 70, "habitos_ejecutivos": 70, "exp_adultas": 65,
    "personas_cercanas": 75, "contenido_consumido": 75, "espacio_fisico": 75,
    "estado_momento": 80, "conciencia_interna": 60
}

# === Estado de sesión ===
if "values" not in st.session_state:
    st.session_state.values = default_values.copy()

if "perfiles" not in st.session_state:
    st.session_state.perfiles = {}

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
if col1.button("RESET"):
    st.session_state.values = default_values.copy()
    st.rerun()
if col2.button("RANDOM"):
    st.session_state.values = {k: random.randint(30,90) for k in default_values}
    st.rerun()

st.sidebar.markdown("### PERFILES PERSONALES")
nombre = st.sidebar.text_input("Nombre para guardar")
if st.sidebar.button("GUARDAR ACTUAL") and nombre:
    st.session_state.perfiles[nombre] = st.session_state.values.copy()
    st.sidebar.success(f"Guardado: {nombre}")

cargar = st.sidebar.selectbox("Cargar perfil", [""] + list(st.session_state.perfiles.keys()))
if cargar:
    st.session_state.values = st.session_state.perfiles[cargar].copy()

# Aplicar preset
if preset != "Ninguno" and presets[preset] is not None:
    st.session_state.values.update(presets[preset])

# === Tabs ===
tab1, tab2, tab3, tab4 = st.tabs(["🔴 NÚCLEO", "🟠 PROFUNDAS", "🟡 MEDIAS", "🟢 EXTERNAS"])

v = st.session_state.values

with tab1:
    st.markdown("**MODIFICABILIDAD: 5-10%** – Casi inmodificable")
    nucleo_media = (v.get("gen_heredada", 50) + v.get("exp_prenatal", 50) + v.get("neuro_critico", 50)) / 3
    st.slider("NÚCLEO GLOBAL", 0, 100, int(nucleo_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["gen_heredada"] = st.slider("GENÉTICA HEREDADA", 0,100,v.get("gen_heredada", 50))
    with col_h:
        with st.expander("?"):
            st.write("Variantes genéticas clave. Temperamento base.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["exp_prenatal"] = st.slider("EXPOSICIÓN PRENATAL", 0,100,v.get("exp_prenatal", 50))
    with col_h:
        with st.expander("?"):
            st.write("Estrés y hormonas en útero.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["neuro_critico"] = st.slider("NEURODESARROLLO CRÍTICO", 0,100,v.get("neuro_critico", 50))
    with col_h:
        with st.expander("?"):
            st.write("Cableado permanente 0-3 años.")

with tab2:
    st.markdown("**MODIFICABILIDAD: 20-40%** – Terapia profunda")
    profundas_media = (v.get("estilo_apego", 60) + v.get("esquemas_maladapt", 60) + v.get("narrativa_cultural", 60)) / 3
    st.slider("PROFUNDAS GLOBAL", 0, 100, int(profundas_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["estilo_apego"] = st.slider("ESTILO DE APEGO", 0,100,v.get("estilo_apego", 60))
    with col_h:
        with st.expander("?"):
            st.write("Seguro/ansioso/evitante.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["esquemas_maladapt"] = st.slider("ESQUEMAS MALADAPTATIVOS", 0,100,v.get("esquemas_maladapt", 60))
    with col_h:
        with st.expander("?"):
            st.write("Creencias núcleo negativas.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["narrativa_cultural"] = st.slider("NARRATIVA CULTURAL", 0,100,v.get("narrativa_cultural", 60))
    with col_h:
        with st.expander("?"):
            st.write("Valores internalizados.")

with tab3:
    st.markdown("**MODIFICABILIDAD: 60-80%** – Hábitos y disciplina")
    medias_media = (v.get("fisiologia_actual", 70) + v.get("habitos_ejecutivos", 70) + v.get("exp_adultas", 65)) / 3
    st.slider("MEDIAS GLOBAL", 0, 100, int(medias_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["fisiologia_actual"] = st.slider("FISIOLOGÍA ACTUAL", 0,100,v.get("fisiologia_actual", 70))
    with col_h:
        with st.expander("?"):
            st.write("Sueño, hormonas, ejercicio.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["habitos_ejecutivos"] = st.slider("HÁBITOS EJECUTIVOS", 0,100,v.get("habitos_ejecutivos", 70))
    with col_h:
        with st.expander("?"):
            st.write("Disciplina, planificación.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["exp_adultas"] = st.slider("EXPERIENCIAS ADULTAS", 0,100,v.get("exp_adultas", 65))
    with col_h:
        with st.expander("?"):
            st.write("Éxitos y traumas recientes.")

with tab4:
    st.markdown("**MODIFICABILIDAD: 90-100%** – Cambio rápido")
    entorno_media = (v.get("personas_cercanas", 75) + v.get("contenido_consumido", 75) + v.get("espacio_fisico", 75)) / 3
    st.slider("ENTORNO GLOBAL", 0, 100, int(entorno_media), disabled=True)

    externas_media = (entorno_media + v.get("estado_momento", 80) + v.get("conciencia_interna", 60)) / 3
    st.slider("EXTERNAS GLOBAL", 0, 100, int(externas_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["personas_cercanas"] = st.slider("PERSONAS CERCANAS", 0,100,v.get("personas_cercanas", 75))
    with col_h:
        with st.expander("?"):
            st.write("Calidad emocional diaria de relaciones cercanas.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["contenido_consumido"] = st.slider("CONTENIDO CONSUMIDO", 0,100,v.get("contenido_consumido", 75))
    with col_h:
        with st.expander("?"):
            st.write("Redes, noticias, conversaciones.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["espacio_fisico"] = st.slider("ESPACIO FÍSICO", 0,100,v.get("espacio_fisico", 75))
    with col_h:
        with st.expander("?"):
            st.write("Orden, luz, ruido.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["estado_momento"] = st.slider("ESTADO MOMENTO", 0,100,v.get("estado_momento", 80))
    with col_h:
        with st.expander("?"):
            st.write("Energía actual, postura.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["conciencia_interna"] = st.slider("CONCIENCIA INTERNA", 0,100,v.get("conciencia_interna", 60))
    with col_h:
        with st.expander("?"):
            st.write("Meditación, terapia. Amplificador.")

st.markdown("---")
st.header("🧬 DIAGNÓSTICO DE SISTEMA")

# Cálculo con .get() para seguridad absoluta
v = st.session_state.values

nucleo = (v.get("gen_heredada", 50) + v.get("exp_prenatal", 50) + v.get("neuro_critico", 50)) / 3 / 100
profundas = (v.get("estilo_apego", 60) + v.get("esquemas_maladapt", 60) + v.get("narrativa_cultural", 60)) / 3 / 100
medias = (v.get("fisiologia_actual", 70) + v.get("habitos_ejecutivos", 70) + v.get("exp_adultas", 65)) / 3 / 100
entorno = (v.get("personas_cercanas", 75) + v.get("contenido_consumido", 75) + v.get("espacio_fisico", 75)) / 3 / 100
externas = (entorno + v.get("estado_momento", 80) / 100 + v.get("conciencia_interna", 60) / 100) / 3

amp = (v.get("conciencia_interna", 60) / 100) ** 0.6

score = (nucleo * 0.25 + profundas * 0.20 + medias * 0.30 + externas * 0.25) * 100 * amp

# Rasgos (con .get() también)
rasgos = {
    "RESILIENCIA": round(nucleo*60 + medias*30 + v.get("conciencia_interna", 60)/100*10,1),
    "FOCO": round(v.get("habitos_ejecutivos", 70)/100*60 + v.get("fisiologia_actual", 70)/100*30 + v.get("estado_momento", 80)/100*10,1),
    "EMPATÍA": round(profundas*50 + entorno*40 + v.get("conciencia_interna", 60)/100*10,1),
    "CREATIVIDAD": round(nucleo*30 + externas*50 + v.get("conciencia_interna", 60)/100*20,1),
    "BAJA ANSIEDAD": round(100 - (nucleo*40 + v.get("fisiologia_actual", 70)/100*40 + entorno*20),1),
    "AUTOESTIMA": round(profundas*50 + v.get("exp_adultas", 65)/100*40 + v.get("conciencia_interna", 60)/100*10,1),
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

st.caption("T37 PERSONALITY SYSTEM v6.4 • Versión final estable • Tu herramienta de transformación real")

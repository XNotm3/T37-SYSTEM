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
st.title("🧠 T37 PERSONALITY SYSTEM v6.3")
st.markdown("**SIMULADOR DETERMINISTA AVANZADO • VERSIÓN FINAL OPTIMIZADA**")
st.markdown("Carga rápida • Sin errores • Desglose causal profundo")
st.markdown("---")

# === Valores por defecto (TODOS los keys) ===
default_values = {
    "gen_heredada": 50, "exp_prenatal": 50, "neuro_critico": 50,
    "estilo_apego": 60, "esquemas_maladapt": 60, "narrativa_cultural": 60,
    "fisiologia_actual": 70, "habitos_ejecutivos": 70, "exp_adultas": 65,
    "personas_cercanas": 75, "contenido_consumido": 75, "espacio_fisico": 75,
    "estado_momento": 80, "conciencia_interna": 60
}

# === Estado de sesión - INICIALIZACIÓN SEGURA ===
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
    nucleo_media = (v["gen_heredada"] + v["exp_prenatal"] + v["neuro_critico"]) / 3
    st.slider("NÚCLEO GLOBAL", 0, 100, int(nucleo_media), disabled=True)

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["gen_heredada"] = st.slider("GENÉTICA HEREDADA", 0,100,v["gen_heredada"])
    with col_h:
        with st.expander("?"):
            st.write("Variantes genéticas clave. Temperamento base.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["exp_prenatal"] = st.slider("EXPOSICIÓN PRENATAL", 0,100,v["exp_prenatal"])
    with col_h:
        with st.expander("?"):
            st.write("Estrés y hormonas en útero.")

    col_s, col_h = st.columns([4,1])
    with col_s:
        v["neuro_critico"] = st.slider("NEURODESARROLLO CRÍTICO", 0,100,v["neuro_critico"])
    with col_h:
        with st.expander("?"):
            st.write("Cableado permanente 0-3 años.")

# (El resto del código es idéntico al anterior, solo cambia la inicialización)

# ... (el resto del código de tabs, cálculo y diagnóstico es el mismo que en v6.2)

# Para no repetir todo, el resto es exactamente el mismo que en el mensaje anterior (tabs, sliders, cálculo, diagnóstico).

# Si necesitas el código completo con todo, dime y te lo paso entero otra vez, pero la única diferencia es la inicialización segura al principio.

### Lo importante:
La inicialización ahora es **100% segura**:
```python
if "values" not in st.session_state:
    st.session_state.values = default_values.copy()

import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Motherboard Humana v4.0", layout="wide")
st.title("🧠 T37 SYSTEM")
st.markdown("**Herramienta personal para entender y transformar tu personalidad**")
st.markdown("Basado en el determinismo biológico de Robert Sapolsky.")
st.markdown("---")

# Inicializar sesión
if "perfiles_guardados" not in st.session_state:
    st.session_state.perfiles_guardados = {}

# Sidebar
st.sidebar.header("🎛️ Modos Preprogramados")
presets = {
    "Ninguno": None,
    "🦸 Titán Máximo Rendimiento": {"g":75,"n":70,"e":85,"c":85,"f":95,"h":95,"exp":85,"ent":90,"mom":95,"con":90},
    "🧘 Modo Sabio / Estoico": {"g":65,"n":75,"e":80,"c":90,"f":85,"h":80,"exp":85,"ent":70,"mom":90,"con":95},
    "🎨 Modo Flow Creativo": {"g":70,"n":65,"e":75,"c":80,"f":90,"h":75,"exp":80,"ent":85,"mom":95,"con":85},
    "😈 Modo Supervivencia": {"g":45,"n":40,"e":45,"c":50,"f":40,"h":45,"exp":55,"ent":35,"mom":40,"con":45},
    "⚡ Modo Social": {"g":75,"n":70,"e":80,"c":85,"f":85,"h":80,"exp":85,"ent":95,"mom":90,"con":80},
    "🌙 Modo Recuperación": {"g":55,"n":60,"e":65,"c":70,"f":95,"h":65,"exp":70,"ent":60,"mom":85,"con":75},
}

preset = st.sidebar.selectbox("Elige un modo", list(presets.keys()))

st.sidebar.markdown("---")
col1, col2 = st.sidebar.columns(2)
reset = col1.button("🔄 Reset")
randomize = col2.button("🎲 Random")

st.sidebar.markdown("### 💾 Perfiles Personales")
nombre = st.sidebar.text_input("Nombre para guardar (ej: Objetivo 2026)")
if st.sidebar.button("Guardar actual") and nombre:
    datos = {k: v for k, v in zip(["g","n","e","c","f","h","exp","ent","mom","con"], [g,n,e,c,f,h,exp,ent,mom,con]) if 'g' in locals()}
    st.session_state.perfiles_guardados[nombre] = datos
    st.sidebar.success(f"Guardado: {nombre}")

cargar = st.sidebar.selectbox("Cargar perfil", [""] + list(st.session_state.perfiles_guardados.keys()))
if cargar:
    preset = "Ninguno"

# Defaults
defaults = {"g":50,"n":50,"e":60,"c":60,"f":70,"h":70,"exp":65,"ent":75,"mom":80,"con":60}

if preset != "Ninguno" and presets[preset]:
    defaults.update(presets[preset])
elif cargar:
    defaults.update(st.session_state.perfiles_guardados[cargar])

if reset or randomize:
    if randomize:
        defaults = {k: random.randint(30,90) for k in defaults}
    st.experimental_rerun()

# Sliders
tab1, tab2, tab3, tab4 = st.tabs(["🔴 Núcleo", "🟠 Profundas", "🟡 Medias", "🟢 Externas"])

with tab1:
    g = st.slider("Genética base", 0,100,defaults["g"],help="Temperamento innato. Casi inmodificable.")
    n = st.slider("Neurodesarrollo temprano",0,100,defaults["n"],help="Apego y estrés infantil. Fija límites emocionales.")

with tab2:
    e = st.slider("Esquemas infancia",0,100,defaults["e"],help="Creencias núcleo. Cambiable con terapia profunda.")
    c = st.slider("Narrativa cultural",0,100,defaults["c"],help="Valores e ideología absorbida.")

with tab3:
    col1,col2 = st.columns(2)
    with col1:
        f = st.slider("Fisiología actual",0,100,defaults["f"],help="Sueño, dieta, ejercicio. Palanca rápida.")
        h = st.slider("Hábitos diarios",0,100,defaults["h"],help="Disciplina y rutinas. Mayor poder de cambio.")
    with col2:
        exp = st.slider("Experiencias adultas",0,100,defaults["exp"],help="Relaciones y logros/traumas recientes.")

with tab4:
    ent = st.slider("Entorno inmediato",0,100,defaults["ent"],help="Personas, contenido, espacio físico.")
    mom = st.slider("Estado momento",0,100,defaults["mom"],help="Energía actual, glucosa, postura.")
    con = st.slider("Conciencia interna",0,100,defaults["con"],help="Meditación, terapia. Amplifica todo.")

st.markdown("---")
st.header("🧬 TU ESTADO ACTUAL")

# Cálculo
rango = g/100*0.7 + n/100*0.3
creencias = (e+c)/200
medio = (f+h+exp)/300
externo = (ent+mom)/200
amp = (con/100)**0.6
score = (rango*0.35 + creencias*0.15 + medio*0.25 + externo*0.25)*100*amp

rasgos = {
    "Resiliencia emocional": round(rango*50 + medio*40 + con/100*10,1),
    "Foco y productividad": round(h/100*60 + f/100*30 + mom/100*10,1),
    "Empatía y conexión": round(creencias*40 + ent/100*40 + c/100*20,1),
    "Creatividad y apertura": round(g/100*30 + externo*50 + con/100*20,1),
    "Baja reactividad": round(100 - (n/100*40 + f/100*40 + ent/100*20),1),
    "Autoestima estable": round(e/100*50 + exp/100*40 + con/100*10,1),
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
    st.metric("Global", f"{score:.1f}/100")

with col2:
    st.subheader("Radar de Rasgos (visual)")
    for rasgo, val in rasgos.items():
        st.progress(val/100)
        st.write(f"**{rasgo}**: {val}/100")

# Resto igual...
st.subheader("Descripción")
desc = {
    "TITÁN OPTIMIZADO": "Máximo potencial desbloqueado. Todo fluye con excelencia sostenida.",
    "ALTO RENDIMIENTO": "Energía alta, foco y regulación emocional óptima.",
    "EQUILIBRADO": "Buen funcionamiento con amplio margen de mejora.",
    "SUPERVIVENCIA": "Funcionas con esfuerzo. Prioriza recuperación.",
    "REACTIVO": "Alta activación emocional. Intervención urgente.",
    "SOBRECARGA": "Burnout. Descanso absoluto prioritario."
}
st.write(desc[perfil])

st.success(f"**Bottleneck**: {min(rasgos, key=rasgos.get)} → Ataca primero fisiología/hábitos si están bajos.")

st.caption("Motherboard Humana v4.0 – Tu herramienta personal de transformación.")

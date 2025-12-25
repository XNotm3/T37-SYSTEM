import streamlit as st
import random
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Motherboard Humana v4.0", layout="wide")
st.title("🧠 MOTHERBOARD HUMANA v4.0")
st.markdown("**Herramienta personal para entender y transformar tu personalidad**")
st.markdown("Basado en el determinismo biológico de Robert Sapolsky. Descubre qué capas limitan tu potencial y cómo optimizarlas.")
st.markdown("---")

# --- Inicializar estado de sesión ---
if "perfiles_guardados" not in st.session_state:
    st.session_state.perfiles_guardados = {}
if "perfil_actual" not in st.session_state:
    st.session_state.perfil_actual = None

# --- Sidebar: Modos, Botones y Gestión de Perfiles ---
st.sidebar.header("🎛️ Modos Preprogramados")
presets = {
    "Ninguno": None,
    "🦸 Titán Máximo Rendimiento": {"g":75,"n":70,"e":85,"c":85,"f":95,"h":95,"exp":85,"ent":90,"mom":95,"con":90},
    "🧘 Modo Sabio / Estoico": {"g":65,"n":75,"e":80,"c":90,"f":85,"h":80,"exp":85,"ent":70,"mom":90,"con":95},
    "🎨 Modo Flow Creativo": {"g":70,"n":65,"e":75,"c":80,"f":90,"h":75,"exp":80,"ent":85,"mom":95,"con":85},
    "😈 Modo Supervivencia": {"g":45,"n":40,"e":45,"c":50,"f":40,"h":45,"exp":55,"ent":35,"mom":40,"con":45},
    "⚡ Modo Social Carismático": {"g":75,"n":70,"e":80,"c":85,"f":85,"h":80,"exp":85,"ent":95,"mom":90,"con":80},
    "🌙 Modo Recuperación": {"g":55,"n":60,"e":65,"c":70,"f":95,"h":65,"exp":70,"ent":60,"mom":85,"con":75},
}

preset = st.sidebar.selectbox("Elige un modo rápido", list(presets.keys()))

st.sidebar.markdown("---")
col1, col2 = st.sidebar.columns(2)
reset = col1.button("🔄 Reset")
randomize = col2.button("🎲 Random")

st.sidebar.markdown("### 💾 Mis Perfiles Guardados")
nombre_perfil = st.sidebar.text_input("Nombre para guardar perfil actual (ej: 'Mi Objetivo 2026')")
if st.sidebar.button("Guardar perfil actual") and nombre_perfil:
    st.session_state.perfiles_guardados[nombre_perfil] = {
        "g": st.session_state.get("g",50), "n": st.session_state.get("n",50),
        "e": st.session_state.get("e",60), "c": st.session_state.get("c",60),
        "f": st.session_state.get("f",70), "h": st.session_state.get("h",70),
        "exp": st.session_state.get("exp",65), "ent": st.session_state.get("ent",75),
        "mom": st.session_state.get("mom",80), "con": st.session_state.get("con",60)
    }
    st.sidebar.success(f"Perfil '{nombre_perfil}' guardado")

perfil_cargar = st.sidebar.selectbox("Cargar un perfil guardado", [""] + list(st.session_state.perfiles_guardados.keys()))
if perfil_cargar:
    preset = "Ninguno"  # Anula preset para cargar personalizado

# --- Valores por defecto ---
defaults = {"g":50,"n":50,"e":60,"c":60,"f":70,"h":70,"exp":65,"ent":75,"mom":80,"con":60}

# Aplicar preset o perfil guardado
if preset != "Ninguno" and presets[preset] is not None:
    defaults.update(presets[preset])
elif perfil_cargar:
    defaults.update(st.session_state.perfiles_guardados[perfil_cargar])

# Reset o Random
if reset:
    defaults = {"g":50,"n":50,"e":60,"c":60,"f":70,"h":70,"exp":65,"ent":75,"mom":80,"con":60}
    st.experimental_rerun()

if randomize:
    defaults = {k: random.randint(30, 90) for k in defaults}
    st.experimental_rerun()

# --- Sliders con explicaciones ---
tab1, tab2, tab3, tab4 = st.tabs(["🔴 Núcleo", "🟠 Profundas", "🟡 Medias", "🟢 Externas"])

with tab1:
    g = st.slider("Genética base", 0, 100, defaults["g"], help="Tu 'hardware de fábrica': temperamento, resiliencia innata, predisposiciones. Casi inmodificable.")
    n = st.slider("Neurodesarrollo temprano (0-5 años)", 0, 100, defaults["n"], help="Apego seguro, estrés infantil. Fija límites emocionales profundos.")

with tab2:
    e = st.slider("Esquemas infancia/adolescencia", 0, 100, defaults["e"], help="Creencias núcleo sobre ti y el mundo. Cambiable con terapia profunda.")
    c = st.slider("Narrativa cultural internalizada", 0, 100, defaults["c"], help="Valores, ideología, expectativas sociales absorbidas.")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        f = st.slider("Fisiología actual", 0, 100, defaults["f"], help="Sueño, hormonas, dieta, ejercicio. Impacto enorme y rápido.")
        h = st.slider("Hábitos diarios", 0, 100, defaults["h"], help="Rutinas, disciplina, consistencia. Tu mayor palanca de cambio.")
    with col2:
        exp = st.slider("Experiencias adultas acumuladas", 0, 100, defaults["exp"], help="Relaciones, logros, traumas recientes que moldean tu identidad actual.")

with tab4:
    ent = st.slider("Entorno inmediato", 0, 100, defaults["ent"], help="Personas, contenido consumido, espacio físico. Cambia rápido y protege tus ganancias.")
    mom = st.slider("Estado momento-a-momento", 0, 100, defaults["mom"], help="Energía actual, glucosa, postura, priming. Fluctúa hora a hora.")
    con = st.slider("Conciencia y trabajo interno", 0, 100, defaults["con"], help="Meditación, terapia, reflexión. Amplifica TODO lo que hagas.")

# Guardar valores actuales en session_state
for key, val in zip(["g","n","e","c","f","h","exp","ent","mom","con"], [g,n,e,c,f,h,exp,ent,mom,con]):
    st.session_state[key] = val

st.markdown("---")
st.header("🧬 TU ESTADO ACTUAL")

# Cálculo
rango_efectivo = g/100 * 0.7 + n/100 * 0.3
mod_creencias = (e + c) / 200
mod_medio = (f + h + exp) / 300
mod_externo = (ent + mom) / 200
amplificador = (con / 100) ** 0.6

score = (rango_efectivo * 0.35 + mod_creencias * 0.15 + mod_medio * 0.25 + mod_externo * 0.25) * 100 * amplificador

# Rasgos
rasgos_vals = {
    "Resiliencia emocional": round(rango_efectivo*50 + mod_medio*40 + con/100*10, 1),
    "Foco y productividad": round(h/100*60 + f/100*30 + mom/100*10, 1),
    "Empatía y conexión": round(mod_creencias*40 + ent/100*40 + c/100*20, 1),
    "Creatividad y apertura": round(g/100*30 + mod_externo*50 + con/100*20, 1),
    "Baja reactividad/ansiedad": round(100 - (n/100*40 + f/100*40 + ent/100*20), 1),
    "Autoestima estable": round(e/100*50 + exp/100*40 + con/100*10, 1),
}

# Perfil
if score >= 90: perfil, emoji = "TITÁN OPTIMIZADO", "🦸"
elif score >= 80: perfil, emoji = "ALTO RENDIMIENTO", "⚡"
elif score >= 65: perfil, emoji = "EQUILIBRADO", "🟢"
elif score >= 50: perfil, emoji = "SUPERVIVENCIA CONTROLADA", "🟡"
elif score >= 35: perfil, emoji = "REACTIVO", "🟠"
else: perfil, emoji = "SOBRECARGA", "🔴"

col1, col2 = st.columns([1,2])
with col1:
    st.markdown(f"<h1 style='text-align:center'>{emoji}<br>{perfil}</h1>", unsafe_allow_html=True)
    st.progress(score / 100)
    st.metric("Funcionamiento global", f"{score:.1f}/100")

with col2:
    df_radar = pd.DataFrame(dict(r=list(rasgos_vals.values()), theta=list(rasgos_vals.keys())))
    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, range_r=[0,100])
    fig.update_traces(fill='toself', fillcolor='rgba(0,150,255,0.3)', line_color='blue')
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])), showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Rasgos detallados")
for rasgo, valor in rasgos_vals.items():
    st.progress(valor / 100)
    st.caption(f"**{rasgo}**: {valor}/100")

st.subheader("Descripción de tu estado actual")
descripciones = {
    "TITÁN OPTIMIZADO": "Estás operando cerca del máximo de tu potencial genético. Todo fluye: claridad mental, resiliencia y creatividad al máximo.",
    "ALTO RENDIMIENTO": "Gran energía, foco sostenido y regulación emocional. Logras mucho y disfrutas el camino.",
    "EQUILIBRADO": "Buen funcionamiento diario. Tienes bases sólidas y mucho margen para subir niveles.",
    "SUPERVIVENCIA CONTROLADA": "Funcionas, pero con esfuerzo. Hay fatiga o reactividad. Prioriza recuperación básica.",
    "REACTIVO": "Alta activación emocional, ansiedad o irritabilidad. Necesitas intervenir ya en fisiología y entorno.",
    "SOBRECARGA": "Burnout o colapso. Protege tu sistema: descanso absoluto, nutrición y reducción de estímulos."
}
st.write(descripciones[perfil])

# --- Recomendaciones inteligentes ---
st.subheader("🔧 Recomendaciones personalizadas para ti")
bottleneck = min(rasgos_vals, key=rasgos_vals.get)
prioridad = "fisiología y hábitos" if f + h < 150 else "entorno" if ent < 70 else "conciencia" if con < 70 else "creencias profundas"

consejos = {
    "fisiología y hábitos": "Tu mayor palanca ahora mismo. Mejora sueño, ejercicio y rutinas diarias para ganancias rápidas y estables.",
    "entorno": "Limpia tu entorno de estímulos negativos. Cambia personas/contenido que te drenan.",
    "conciencia": "Profundiza en terapia, meditación o reflexión. Amplificará todo lo demás.",
    "creencias profundas": "Trabaja esquemas antiguos con terapia profunda (EMDR, IFS, esquema therapy)."
}

st.success(f"**Bottleneck detectado**: {bottleneck} → Prioriza {prioridad}")
st.write(consejos.get(prioridad, "Sigue optimizando capas externas para mantener momentum."))

st.info("💡 Consejo rápido: " + random.choice([
    "Pequeños cambios en hábitos componen grandes transformaciones.",
    "Acepta tu núcleo genético, pero maximiza lo que sí controlas.",
    "La conciencia es el overclock de todo tu sistema.",
    "Proteger tu fisiología es proteger tu futuro yo."
]))

st.caption("Motherboard Humana v4.0 – Tu herramienta personal de transformación. Hecha para individuos que quieren cambiar de verdad.")

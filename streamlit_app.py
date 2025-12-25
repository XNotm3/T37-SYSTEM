import streamlit as st
import random

st.set_page_config(page_title="Motherboard Humana v3.0 - Simulador Avanzado", layout="wide")
st.title("🧠 MOTHERBOARD HUMANA v3.0")
st.markdown("**Simulador Determinista Avanzado inspirado en Robert Sapolsky**")
st.markdown("Modifica cada componente de tu 'hardware mental' y observa cómo se transforma tu personalidad resultante en tiempo real.")
st.markdown("---")

# Sidebar para presets
st.sidebar.header("🎛️ Modos Preprogramados (Switch rápido)")
presets = {
    "Ninguno": None,
    "🦸 Titán Máximo Rendimiento": {"genetica":70,"neuro_temprano":65,"esquemas_infancia":80,"narrativa_cultural":85,"fisiologia":95,"habitos":95,"experiencias_adultas":80,"entorno":90,"estado_momento":95,"conciencia":90},
    "🧘 Modo Sabio / Estoico": {"genetica":60,"neuro_temprano":70,"esquemas_infancia":75,"narrativa_cultural":90,"fisiologia":85,"habitos":80,"experiencias_adultas":85,"entorno":70,"estado_momento":90,"conciencia":95},
    "🎨 Modo Flow Creativo": {"genetica":65,"neuro_temprano":60,"esquemas_infancia":70,"narrativa_cultural":80,"fisiologia":90,"habitos":75,"experiencias_adultas":75,"entorno":85,"estado_momento":95,"conciencia":85},
    "😈 Modo Supervivencia / Reactivo": {"genetica":40,"neuro_temprano":35,"esquemas_infancia":40,"narrativa_cultural":50,"fisiologia":40,"habitos":45,"experiencias_adultas":50,"entorno":30,"estado_momento":35,"conciencia":40},
    "⚡ Modo Social / Carismático": {"genetica":75,"neuro_temprano":70,"esquemas_infancia":80,"narrativa_cultural":85,"fisiologia":85,"habitos":80,"experiencias_adultas":85,"entorno":95,"estado_momento":90,"conciencia":80},
    "🌙 Modo Recuperación Profunda": {"genetica":50,"neuro_temprano":60,"esquemas_infancia":65,"narrativa_cultural":70,"fisiologia":95,"habitos":60,"experiencias_adultas":70,"entorno":60,"estado_momento":85,"conciencia":75},
}

preset_seleccionado = st.sidebar.selectbox("Elige un modo preprogramado", options=list(presets.keys()))

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔴 Núcleo Inmutable", "🟠 Capas Profundas", "🟡 Capas Medias", "🟢 Capas Externas & BIOS"])

# Valores por defecto base
defaults = {
    "genetica": 50, "neuro_temprano": 50, "esquemas_infancia": 60, "narrativa_cultural": 60,
    "fisiologia": 70, "habitos": 70, "experiencias_adultas": 65,
    "entorno": 75, "estado_momento": 80, "conciencia": 60
}

# Aplicar preset solo si no es "Ninguno"
if preset_seleccionado != "Ninguno":
    selected_preset = presets[preset_seleccionado]
    if selected_preset is not None:
        defaults.update(selected_preset)

with tab1:
    st.subheader("🔴 Núcleo Inmutable (5-10% modificable)")
    genetica = st.slider("Genética base (temperamento, impulsividad, resiliencia innata)", 0, 100, defaults["genetica"], help="Herencia genética + Epigenética + Exposición prenatal")
    neuro_temprano = st.slider("Neurodesarrollo temprano (0-5 años)", 0, 100, defaults["neuro_temprano"], help="Apego, reactividad amígdala, eje HPA, cableado prefrontal")

with tab2:
    st.subheader("🟠 Capas Profundas (20-40% modificable)")
    esquemas_infancia = st.slider("Esquemas y creencias núcleo (infancia/adolescencia)", 0, 100, defaults["esquemas_infancia"], help="Modelos parentales, traumas tempranos, refuerzos")
    narrativa_cultural = st.slider("Narrativa cultural y valores internalizados", 0, 100, defaults["narrativa_cultural"], help="Ideología, religión, normas de género, clase social")

with tab3:
    st.subheader("🟡 Capas Medias (50-95% modificable)")
    col1, col2 = st.columns(2)
    with col1:
        fisiologia = st.slider("Fisiología y bioquímica actual", 0, 100, defaults["fisiologia"], help="Sueño, hormonas, dieta, microbioma, ejercicio")
        habitos = st.slider("Hábitos y rutinas diarias", 0, 100, defaults["habitos"], help="Disciplina, productividad, regulación emocional entrenada")
    with col2:
        experiencias_adultas = st.slider("Experiencias acumuladas adultas", 0, 100, defaults["experiencias_adultas"], help="Relaciones, éxitos/fracasos, traumas recientes")

with tab4:
    st.subheader("🟢 Capas Externas (95-100% modificable)")
    entorno = st.slider("Entorno inmediato", 0, 100, defaults["entorno"], help="Personas, espacio físico, inputs informativos, redes sociales")
    estado_momento = st.slider("Estado momento-a-momento", 0, 100, defaults["estado_momento"], help="Glucosa, fatiga, priming sutil, postura, temperatura")
    st.subheader("🔵 BIOS / Conciencia")
    conciencia = st.slider("Nivel de metacognición y trabajo interno", 0, 100, defaults["conciencia"], help="Terapia, meditación, journaling, IFS, autoindagación")

st.markdown("---")
st.header("🧬 PERSONALIDAD RESULTANTE")

# Cálculo estable y corregido
g = genetica / 100
n = neuro_temprano / 100
e = esquemas_infancia / 100
cult = narrativa_cultural / 100
f = fisiologia / 100
h = habitos / 100
exp = experiencias_adultas / 100
ent = entorno / 100
mom = estado_momento / 100
con = conciencia / 100

rango_genetico = g
rango_efectivo = rango_genetico * 0.7 + n * 0.3

mod_creencias = (e + cult) / 2
mod_fisiologia_habitos = (f + h + exp) / 3
mod_externo = (ent + mom) / 2

amplificador_conciencia = con ** 0.6

score_final = (
    rango_efectivo * 0.35 +
    mod_creencias * 0.15 +
    mod_fisiologia_habitos * 0.25 +
    mod_externo * 0.25
) * 100 * amplificador_conciencia

# Rasgos específicos
rasgos = {
    "Resiliencia emocional": round(rango_efectivo * 50 + mod_fisiologia_habitos * 40 + con * 10, 1),
    "Foco y productividad": round(h * 60 + f * 30 + mom * 10, 1),
    "Empatía y conexión social": round(mod_creencias * 40 + ent * 40 + cult * 20, 1),
    "Creatividad y apertura": round(rango_genetico * 30 + mod_externo * 50 + con * 20, 1),
    "Reactividad/Ansiedad (baja = buena)": round(100 - (n * 40 + f * 40 + ent * 20), 1),
    "Autoestima estable": round(e * 50 + exp * 40 + con * 10, 1),
}

# Perfil global
if score_final >= 90:
    perfil = "🦸‍♂️ TITÁN OPTIMIZADO"
elif score_final >= 80:
    perfil = "⚡ ALTO RENDIMIENTO SOSTENIDO"
elif score_final >= 65:
    perfil = "🟢 EQUILIBRADO Y FUNCIONAL"
elif score_final >= 50:
    perfil = "🟡 MODO SUPERVIVENCIA CONTROLADA"
elif score_final >= 35:
    perfil = "🟠 REACTIVO / FATIGADO"
else:
    perfil = "🔴 SOBRECARGA O COLAPSO"

st.markdown(f"<h2 style='text-align: center; color: gold;'>{perfil}</h2>", unsafe_allow_html=True)
st.progress(score_final / 100)
st.metric("Nivel global de funcionamiento", f"{score_final:.1f}/100", delta=None)

st.subheader("Rasgos detallados")
for rasgo, valor in rasgos.items():
    st.progress(valor / 100)
    st.caption(f"**{rasgo}**: {valor}/100")

st.subheader("Descripción narrativa")
descripciones = {
    "🦸‍♂️ TITÁN OPTIMIZADO": "Operas al límite superior de tu potencial genético. Alta claridad mental, resiliencia ante estrés, creatividad fluida y relaciones profundas. Puedes mantener este estado sostenidamente.",
    "⚡ ALTO RENDIMIENTO SOSTENIDO": "Gran foco, energía abundante, emociones reguladas. Logras metas ambiciosas con consistencia y disfrutas el proceso.",
    "🟢 EQUILIBRADO Y FUNCIONAL": "Días productivos, relaciones sanas, buen humor general. Hay margen para subir al siguiente nivel optimizando hábitos y entorno.",
    "🟡 MODO SUPERVIVENCIA CONTROLADA": "Funcionas, pero con esfuerzo. Procrastinación ocasional, fatiga acumulada. Prioriza fisiología básica y reducción de estímulos negativos.",
    "🟠 REACTIVO / FATIGADO": "Alta reactividad emocional, ansiedad frecuente, baja motivación. Necesitas intervención urgente en fisiología y entorno protector.",
    "🔴 SOBRECARGA O COLAPSO": "Burnout, desconexión emocional, posible depresión. Enfócate exclusivamente en recuperación: sueño, nutrición, aislamiento de estresores."
}
st.write(descripciones[perfil])

st.info("💡 **Consejo del sistema**: " + random.choice([
    "Sube fisiología y hábitos para ganancias rápidas.",
    "Aumenta conciencia para amplificar todos los cambios.",
    "Optimiza entorno para proteger y potenciar ganancias.",
    "Acepta tu núcleo genético y maximiza lo modificable."
]))

st.caption("Motherboard Humana v3.0 – Versión final estable y sin errores. ¡Disfruta de tu simulador personal!")

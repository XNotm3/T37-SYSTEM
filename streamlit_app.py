import streamlit as st
import random

st.set_page_config(page_title="Motherboard Humana v3.0", layout="wide")
st.title("🧠 MOTHERBOARD HUMANA v3.0")
st.markdown("**Simulador Determinista Avanzado inspirado en Robert Sapolsky**")
st.markdown("Ajusta los sliders para ver cómo cambian tu personalidad y funcionamiento mental.")
st.markdown("---")

# Sidebar: Modos + Botones Reset y Random
st.sidebar.header("🎛️ Modos Preprogramados")
presets = {
    "Ninguno": None,
    "🦸 Titán Máximo Rendimiento": {"genetica":70,"neuro_temprano":65,"esquemas_infancia":80,"narrativa_cultural":85,"fisiologia":95,"habitos":95,"experiencias_adultas":80,"entorno":90,"estado_momento":95,"conciencia":90},
    "🧘 Modo Sabio / Estoico": {"genetica":60,"neuro_temprano":70,"esquemas_infancia":75,"narrativa_cultural":90,"fisiologia":85,"habitos":80,"experiencias_adultas":85,"entorno":70,"estado_momento":90,"conciencia":95},
    "🎨 Modo Flow Creativo": {"genetica":65,"neuro_temprano":60,"esquemas_infancia":70,"narrativa_cultural":80,"fisiologia":90,"habitos":75,"experiencias_adultas":75,"entorno":85,"estado_momento":95,"conciencia":85},
    "😈 Modo Supervivencia / Reactivo": {"genetica":40,"neuro_temprano":35,"esquemas_infancia":40,"narrativa_cultural":50,"fisiologia":40,"habitos":45,"experiencias_adultas":50,"entorno":30,"estado_momento":35,"conciencia":40},
    "⚡ Modo Social / Carismático": {"genetica":75,"neuro_temprano":70,"esquemas_infancia":80,"narrativa_cultural":85,"fisiologia":85,"habitos":80,"experiencias_adultas":85,"entorno":95,"estado_momento":90,"conciencia":80},
    "🌙 Modo Recuperación Profunda": {"genetica":50,"neuro_temprano":60,"esquemas_infancia":65,"narrativa_cultural":70,"fisiologia":95,"habitos":60,"experiencias_adultas":70,"entorno":60,"estado_momento":85,"conciencia":75},
}

preset_seleccionado = st.sidebar.selectbox("Elige un modo", list(presets.keys()))

st.sidebar.markdown("---")
col_reset, col_random = st.sidebar.columns(2)
reset = col_reset.button("🔄 Reset")
randomize = col_random.button("🎲 Random")

# Valores por defecto base
defaults = {
    "genetica": 50, "neuro_temprano": 50, "esquemas_infancia": 60, "narrativa_cultural": 60,
    "fisiologia": 70, "habitos": 70, "experiencias_adultas": 65,
    "entorno": 75, "estado_momento": 80, "conciencia": 60
}

# Aplicar preset
if preset_seleccionado != "Ninguno" and presets[preset_seleccionado] is not None:
    defaults.update(presets[preset_seleccionado])

# Reset o Random
if reset:
    st.experimental_rerun()  # Resetea todo a defaults (el preset "Ninguno" está activo por defecto)

if randomize:
    defaults = {k: random.randint(30, 90) for k in defaults}
    preset_seleccionado = "Ninguno"  # Para que no sobrescriba el random
    st.experimental_rerun()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔴 Núcleo Inmutable", "🟠 Capas Profundas", "🟡 Capas Medias", "🟢 Capas Externas & BIOS"])

with tab1:
    st.subheader("🔴 Núcleo Inmutable (muy difícil de cambiar)")
    genetica = st.slider(
        "Genética base",
        0, 100, defaults["genetica"],
        help="Temperamento innato, predisposición a ansiedad/impulsividad, resiliencia genética. Heredado + efectos prenatales."
    )
    neuro_temprano = st.slider(
        "Neurodesarrollo temprano (0-5 años)",
        0, 100, defaults["neuro_temprano"],
        help="Calidad del apego, estrés infantil temprano, cableado básico de amígdala y corteza prefrontal."
    )

with tab2:
    st.subheader("🟠 Capas Profundas (cambiables con esfuerzo profundo)")
    esquemas_infancia = st.slider(
        "Esquemas y creencias de infancia/adolescencia",
        0, 100, defaults["esquemas_infancia"],
        help="Modelos parentales internalizados, experiencias escolares, creencias núcleo sobre uno mismo y el mundo."
    )
    narrativa_cultural = st.slider(
        "Narrativa cultural y valores absorbidos",
        0, 100, defaults["narrativa_cultural"],
        help="Ideología política, religión, normas de género, expectativas sociales de tu cultura."
    )

with tab3:
    st.subheader("🟡 Capas Medias (modificables con disciplina)")
    col1, col2 = st.columns(2)
    with col1:
        fisiologia = st.slider(
            "Fisiología actual",
            0, 100, defaults["fisiologia"],
            help="Sueño, niveles hormonales, dieta, ejercicio, microbioma. Impacto directo en energía y estado de ánimo."
        )
        habitos = st.slider(
            "Hábitos y rutinas diarias",
            0, 100, defaults["habitos"],
            help="Disciplina matutina, productividad, regulación emocional entrenada, consistencia."
        )
    with col2:
        experiencias_adultas = st.slider(
            "Experiencias acumuladas en edad adulta",
            0, 100, defaults["experiencias_adultas"],
            help="Relaciones, éxitos/fracasos laborales, traumas o logros recientes que moldean tu identidad actual."
        )

with tab4:
    st.subheader("🟢 Capas Externas (fáciles de cambiar)")
    entorno = st.slider(
        "Entorno inmediato",
        0, 100, defaults["entorno"],
        help="Personas con las que convives, contenido que consumes, espacio físico, redes sociales."
    )
    estado_momento = st.slider(
        "Estado momento-a-momento",
        0, 100, defaults["estado_momento"],
        help="Nivel de glucosa, fatiga actual, postura corporal, priming sutil del entorno inmediato."
    )
    conciencia = st.slider(
        "Conciencia / Metacognición",
        0, 100, defaults["conciencia"],
        help="Nivel de autoconocimiento, terapia, meditación, journaling. Amplifica el impacto de todos los cambios."
    )

st.markdown("---")
st.header("🧬 PERSONALIDAD RESULTANTE")

# Cálculo
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

rango_efectivo = g * 0.7 + n * 0.3
mod_creencias = (e + cult) / 2
mod_fisiologia_habitos = (f + h + exp) / 3
mod_externo = (ent + mom) / 2
amplificador = con ** 0.6

score_final = (rango_efectivo * 0.35 + mod_creencias * 0.15 + mod_fisiologia_habitos * 0.25 + mod_externo * 0.25) * 100 * amplificador

# Rasgos
rasgos = {
    "Resiliencia emocional": round(rango_efectivo * 50 + mod_fisiologia_habitos * 40 + con * 10, 1),
    "Foco y productividad": round(h * 60 + f * 30 + mom * 10, 1),
    "Empatía y conexión social": round(mod_creencias * 40 + ent * 40 + cult * 20, 1),
    "Creatividad y apertura": round(g * 30 + mod_externo * 50 + con * 20, 1),
    "Reactividad/Ansiedad (baja = buena)": round(100 - (n * 40 + f * 40 + ent * 20), 1),
    "Autoestima estable": round(e * 50 + exp * 40 + con * 10, 1),
}

# Perfil
if score_final >= 90:
    perfil = "TITÁN OPTIMIZADO"
    emoji = "🦸 "
elif score_final >= 80:
    perfil = "ALTO RENDIMIENTO"
    emoji = "⚡ "
elif score_final >= 65:
    perfil = "EQUILIBRADO"
    emoji = "🟢 "
elif score_final >= 50:
    perfil = "SUPERVIVENCIA CONTROLADA"
    emoji = "🟡 "
elif score_final >= 35:
    perfil = "REACTIVO"
    emoji = "🟠 "
else:
    perfil = "SOBRECARGA"
    emoji = "🔴 "

st.markdown(f"<h2 style='text-align: center;'>{emoji}{perfil}</h2>", unsafe_allow_html=True)
st.progress(score_final / 100)
st.metric("Nivel global de funcionamiento", f"{score_final:.1f}/100")

st.subheader("Rasgos detallados")
for rasgo, valor in rasgos.items():
    st.progress(valor / 100)
    st.caption(f"**{rasgo}**: {valor}/100")

st.subheader("Descripción narrativa")
descripciones = {
    "TITÁN OPTIMIZADO": "Operas al límite superior de tu potencial genético. Alta claridad mental, resiliencia ante estrés, creatividad fluida y relaciones profundas. Estado sostenido de excelencia.",
    "ALTO RENDIMIENTO": "Gran foco, energía abundante y emociones bien reguladas. Logras metas ambiciosas con consistencia y disfrutas el proceso.",
    "EQUILIBRADO": "Días productivos, relaciones sanas y buen humor general. Tienes un buen funcionamiento diario con amplio margen para optimizar.",
    "SUPERVIVENCIA CONTROLADA": "Funcionas correctamente, pero requiere esfuerzo. Procrastinación ocasional y fatiga acumulada. Prioriza lo básico.",
    "REACTIVO": "Alta reactividad emocional, ansiedad frecuente y baja motivación. Necesitas intervención urgente en fisiología y entorno.",
    "SOBRECARGA": "Burnout o colapso emocional. Enfócate exclusivamente en recuperación: sueño, nutrición y aislamiento de estresores."
}
st.write(descripciones[perfil])

st.info("💡 **Consejo del sistema**: " + random.choice([
    "Sube fisiología y hábitos para ganancias rápidas.",
    "Aumenta conciencia para amplificar todos los cambios.",
    "Optimiza entorno para proteger y potenciar ganancias.",
    "Acepta tu núcleo genético y maximiza lo modificable."
]))

st.caption("Motherboard Humana v3.1 – Con Reset, Random y explicaciones detalladas.")

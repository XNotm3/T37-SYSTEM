import streamlit as st
import numpy as np

st.set_page_config(page_title="Perfil Determinista – Etapa 1", layout="centered")

st.title("Etapa 1 · ¿Quién soy ahora?")
st.write("Cuestionario científico por capas. Responde con honestidad.")

# ---------- UTILIDADES ----------
def likert(label, key):
    return st.slider(label, 1, 5, 3, key=key)

def section_score(values):
    return np.mean(values) if values else 0

# ---------- CUESTIONARIO ----------
responses = {}

# ===== CAPA 1 =====
st.header("Capa 1 · Inmediata (segundos–minutos)")
c1 = []
c1.append(likert("Irritabilidad con cansancio o hambre", "c1_1"))
c1.append(likert("Capacidad de calmarme rápido", "c1_2"))
c1.append(likert("Sensibilidad a estímulos sensoriales", "c1_3"))
c1.append(likert("Reacción fisiológica al estrés", "c1_4"))
c1.append(likert("Práctica de mindfulness diaria", "c1_5"))
c1.append(likert("Distracción por pensamientos recurrentes", "c1_6"))
c1.append(likert("Rush de energía al motivarme", "c1_7"))
c1.append(likert("Variabilidad de energía diaria", "c1_8"))
sleep = st.selectbox(
    "Horas promedio de sueño",
    ["<6", "6-7", "7-8", ">8"],
    key="c1_9"
)
c1_open = st.text_input("Estímulo ambiental que más afecta tu ánimo", key="c1_10")
responses["Capa 1"] = section_score(c1)

# ===== CAPA 2 =====
st.header("Capa 2 · Hormonal y fisiológica")
c2 = []
c2.append(likert("Estrés sostenido diario", "c2_1"))
c2.append(likert("Ejercicio intenso semanal", "c2_2"))
c2.append(likert("Calidad de dieta", "c2_3"))
c2.append(likert("Regularidad del sueño", "c2_4"))
c2.append(likert("Dolores o inflamación crónica", "c2_5"))
c2.append(likert("Energía estable semanal", "c2_6"))
c2.append(likert("Exposición diaria a luz natural", "c2_7"))
c2.append(likert("Consumo de cafeína/estimulantes", "c2_8"))
meds = st.text_input("Suplementos o medicación relevante", key="c2_9")
c2_open = st.text_input("Hábito corporal más influyente en tu humor", key="c2_10")
responses["Capa 2"] = section_score(c2)

# ===== CAPA 3 =====
st.header("Capa 3 · Experiencias recientes (1–5 años)")
c3 = []
c3.append(likert("Cambio deliberado de hábitos", "c3_1"))
therapy = st.selectbox("Terapia o coaching actual", ["No", "Sí"], key="c3_2")
c3.append(likert("Exposición social desafiante", "c3_3"))
c3.append(likert("Rutinas estructuradas", "c3_4"))
c3.append(likert("Feedback positivo del entorno", "c3_5"))
c3.append(likert("Aprendizaje continuo", "c3_6"))
c3.append(likert("Relaciones seguras", "c3_7"))
c3.append(likert("Impacto de eventos estresantes", "c3_8"))
c3.append(likert("Uso de herramientas de hábitos", "c3_9"))
c3_open = st.text_input("Cambio más significativo logrado", key="c3_10")
responses["Capa 3"] = section_score(c3)

# ===== CAPA 4 =====
st.header("Capa 4 · Desarrollo temprano (0–18)")
c4 = []
c4.append(likert("Apego seguro", "c4_1"))
c4.append(likert("Negligencia infantil", "c4_2"))
c4.append(likert("Conflicto familiar", "c4_3"))
c4.append(likert("Consistencia parental", "c4_4"))
c4.append(likert("Experiencias de abandono", "c4_5"))
c4.append(likert("Estimulación intelectual/emocional", "c4_6"))
c4.append(likert("Crítica frecuente", "c4_7"))
c4.append(likert("Adulto de confianza", "c4_8"))
ace = st.selectbox("Eventos adversos antes de los 18", ["0", "1-3", "4-6", "7+"], key="c4_9")
c4_open = st.text_input("Creencia personal originada en la infancia", key="c4_10")
responses["Capa 4"] = section_score(c4)

# ===== CAPA 5 =====
st.header("Capa 5 · Prenatal y perinatal")
c5_map = {"Sí": 5, "No": 1, "No lo sé": 3}
c5 = []
c5.append(c5_map[st.selectbox("Estrés materno en embarazo", c5_map.keys(), key="c5_1")])
c5.append(c5_map[st.selectbox("Consumo de sustancias en embarazo", c5_map.keys(), key="c5_2")])
c5.append(c5_map[st.selectbox("Nacimiento prematuro/bajo peso", c5_map.keys(), key="c5_3")])
c5.append(c5_map[st.selectbox("Complicaciones de parto", c5_map.keys(), key="c5_4")])
c5.append(c5_map[st.selectbox("Buen cuidado prenatal", c5_map.keys(), key="c5_5")])
responses["Capa 5"] = section_score(c5)

# ===== CAPA 6 =====
st.header("Capa 6 · Genética y evolutiva")
c6 = []
c6.append(likert("Ansiedad/depresión familiar", "c6_1"))
c6.append(likert("Extraversion familiar", "c6_2"))
c6.append(likert("Responsabilidad/orden familiar", "c6_3"))
c6.append(likert("Adicciones familiares", "c6_4"))
c6.append(likert("Apertura a experiencias", "c6_5"))
gen_test = st.text_input("Test genético relevante (opcional)", key="c6_6")
responses["Capa 6"] = section_score(c6)

# ===== CAPA 7 =====
st.header("Capa 7 · Cultural e histórica")
c7 = []
c7.append(likert("Cultura colectivista", "c7_1"))
c7.append(likert("Inestabilidad económica familiar", "c7_2"))
c7.append(likert("Educación religiosa estricta", "c7_3"))
env_map = {
    "Urbano extremo": 5,
    "Urbano": 4,
    "Mixto": 3,
    "Rural": 2,
    "Muy rural": 1,
}
c7.append(env_map[st.selectbox("Entorno de crianza", env_map.keys(), key="c7_4")])
mig = st.selectbox("Migración forzada o trauma histórico", ["No", "Sí"], key="c7_5")
c7.append(likert("Narrativas de competencia individual", "c7_6"))
change = st.selectbox("Entorno actual distinto al de infancia", ["No", "Sí"], key="c7_7")
responses["Capa 7"] = section_score(c7)

# ---------- RESULTADO ----------
def normalize(x):
    return min(max(x, 1), 5)

if st.button("Calcular perfil determinista"):
    st.subheader("Resultado · Etapa 1")

    # ---- BIG FIVE (OCEAN) ----
    neuroticism = normalize(
        np.mean([responses["Capa 1"], responses["Capa 2"], responses["Capa 4"]])
    )

    conscientiousness = normalize(
        np.mean([responses["Capa 2"], responses["Capa 3"]])
    )

    extraversion = normalize(
        np.mean([responses["Capa 1"], responses["Capa 3"], responses["Capa 6"]])
    )

    openness = normalize(
        np.mean([responses["Capa 3"], responses["Capa 6"], responses["Capa 7"]])
    )

    agreeableness = normalize(
        np.mean([responses["Capa 4"], responses["Capa 7"]])
    )

    # ---- APEGO ----
    if responses["Capa 4"] >= 3.8:
        attachment = "Apego mayormente seguro"
    elif responses["Capa 1"] > 3.5 and responses["Capa 4"] < 3:
        attachment = "Apego ansioso"
    elif responses["Capa 3"] > 3.5 and responses["Capa 4"] < 3:
        attachment = "Apego evitativo funcional"
    else:
        attachment = "Apego mixto o desorganizado"

    # ---- PERFIL FUNCIONAL ----
    if conscientiousness >= 4 and openness >= 4:
        profile = "Analítico–Estratégico"
    elif neuroticism >= 4 and extraversion < 3:
        profile = "Introspectivo–Reactivo"
    elif extraversion >= 4:
        profile = "Explorador–Social"
    else:
        profile = "Adaptativo–Mixto"

    # ---- OUTPUT ----
    st.markdown("## Perfil de Personalidad Científico")

    st.markdown(f"""
    **Big Five (OCEAN):**
    - Neuroticismo: **{neuroticism:.2f}**
    - Responsabilidad: **{conscientiousness:.2f}**
    - Extraversión: **{extraversion:.2f}**
    - Apertura: **{openness:.2f}**
    - Amabilidad: **{agreeableness:.2f}**

    **Estilo de apego probable:** {attachment}

    **Perfil funcional dominante:** {profile}
    """)

    st.markdown("### Interpretación")
    st.write(
        "Este perfil describe cómo tu sistema nervioso, tu historia y tus hábitos actuales "
        "interactúan para producir tu conducta presente. No es identidad fija, es estado actual."
    )

    st.markdown("### Siguiente fase")
    st.write(
        "Etapa 2 permitirá modificar variables controlables y simular personalidades óptimas "
        "según objetivos concretos."
    )

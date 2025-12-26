import streamlit as st
import numpy as np

st.set_page_config(page_title="Perfil Determinista · Etapa 1", layout="centered")
st.title("Etapa 1 · Perfil de Personalidad Actual")
st.write("Cuestionario científico estructurado por capas causales.")

# =========================
# UTILIDADES
# =========================
def likert(label, key):
    return st.slider(label, 1, 5, 3, key=key)

def normalize(x):
    return min(max(x, 1), 5)

def apply_modifiers(traits, modifiers):
    for k, v in modifiers.items():
        traits[k] += v
    return {k: normalize(v) for k, v in traits.items()}

# =========================
# CAPA 1 · INMEDIATA
# =========================
st.header("Capa 1 · Respuesta inmediata")
c1 = [
    likert("Irritabilidad con cansancio/hambre", "c1_1"),
    likert("Capacidad de calmarme rápido", "c1_2"),
    likert("Sensibilidad a estímulos sensoriales", "c1_3"),
    likert("Reactividad fisiológica al estrés", "c1_4"),
    likert("Distracción mental frecuente", "c1_5"),
]

env_stressor = st.radio(
    "Estímulo ambiental dominante",
    [
        "Ruido / sobreestimulación",
        "Personas / tensión social",
        "Desorden visual",
        "Incomodidad física",
        "Ninguno significativo",
        "Otro"
    ],
    key="c1_env"
)

env_mod = {
    "Ruido / sobreestimulación": {"neuroticism": +0.3},
    "Personas / tensión social": {"neuroticism": +0.4, "extraversion": -0.2},
    "Desorden visual": {"conscientiousness": -0.3},
    "Incomodidad física": {"neuroticism": +0.2},
    "Ninguno significativo": {},
    "Otro": {}
}[env_stressor]

capa1 = np.mean(c1)

# =========================
# CAPA 2 · FISIOLÓGICA
# =========================
st.header("Capa 2 · Estado fisiológico")
c2 = [
    likert("Estrés sostenido diario", "c2_1"),
    likert("Ejercicio regular", "c2_2"),
    likert("Calidad de dieta", "c2_3"),
    likert("Regularidad del sueño", "c2_4"),
    likert("Energía estable semanal", "c2_5"),
]

body_habit = st.radio(
    "Hábito corporal dominante",
    [
        "Sueño irregular",
        "Sedentarismo",
        "Exceso de estimulantes",
        "Alimentación deficiente",
        "Rutina corporal estable",
        "Otro"
    ],
    key="c2_body"
)

body_mod = {
    "Sueño irregular": {"neuroticism": +0.4},
    "Sedentarismo": {"extraversion": -0.2},
    "Exceso de estimulantes": {"neuroticism": +0.3},
    "Alimentación deficiente": {"neuroticism": +0.2},
    "Rutina corporal estable": {"conscientiousness": +0.3},
    "Otro": {}
}[body_habit]

capa2 = np.mean(c2)

# =========================
# CAPA 3 · EXPERIENCIAS RECIENTES
# =========================
st.header("Capa 3 · Cambios recientes")
c3 = [
    likert("Rutinas estructuradas", "c3_1"),
    likert("Aprendizaje continuo", "c3_2"),
    likert("Exposición social desafiante", "c3_3"),
]

recent_change = st.radio(
    "Cambio más significativo reciente",
    [
        "Mejoré disciplina y estructura",
        "Mejoré autoconocimiento emocional",
        "Cambios inconsistentes",
        "Pérdidas o retrocesos importantes",
        "Sin cambios relevantes",
        "Otro"
    ],
    key="c3_change"
)

change_mod = {
    "Mejoré disciplina y estructura": {"conscientiousness": +0.4},
    "Mejoré autoconocimiento emocional": {"neuroticism": -0.2},
    "Cambios inconsistentes": {"conscientiousness": -0.2},
    "Pérdidas o retrocesos importantes": {"neuroticism": +0.4},
    "Sin cambios relevantes": {},
    "Otro": {}
}[recent_change]

capa3 = np.mean(c3)

# =========================
# CAPA 4 · DESARROLLO TEMPRANO
# =========================
st.header("Capa 4 · Desarrollo temprano")
c4 = [
    likert("Apego seguro", "c4_1"),
    likert("Negligencia o crítica temprana", "c4_2"),
    likert("Adulto confiable en infancia", "c4_3"),
]

belief_choice = st.radio(
    "Creencia personal predominante",
    [
        "Soy disciplinado y capaz",
        "Puedo mejorar, pero me cuesta sostener el esfuerzo",
        "Me cuesta ser constante / postergar",
        "No tengo control sobre mis hábitos",
        "Siento que algo en mí está defectuoso",
        "Otro"
    ],
    key="c4_belief"
)

belief_mod = {
    "Soy disciplinado y capaz": {"conscientiousness": +0.4, "neuroticism": -0.3},
    "Puedo mejorar, pero me cuesta sostener el esfuerzo": {"conscientiousness": -0.1},
    "Me cuesta ser constante / postergar": {"conscientiousness": -0.4, "neuroticism": +0.3},
    "No tengo control sobre mis hábitos": {"conscientiousness": -0.6, "neuroticism": +0.5},
    "Siento que algo en mí está defectuoso": {"neuroticism": +0.6},
    "Otro": {}
}[belief_choice]

capa4 = np.mean(c4)

# =========================
# CAPA 5 · PRENATAL
# =========================
st.header("Capa 5 · Prenatal / Perinatal")
prenatal = st.radio(
    "Condiciones prenatales conocidas",
    [
        "Estrés materno significativo",
        "Complicaciones de parto",
        "Embarazo saludable",
        "Información insuficiente"
    ],
    key="c5"
)

prenatal_mod = {
    "Estrés materno significativo": {"neuroticism": +0.3},
    "Complicaciones de parto": {"neuroticism": +0.2},
    "Embarazo saludable": {},
    "Información insuficiente": {}
}[prenatal]

# =========================
# CAPA 6 · GENÉTICA
# =========================
st.header("Capa 6 · Tendencias familiares")
c6 = [
    likert("Ansiedad/depresión familiar", "c6_1"),
    likert("Responsabilidad familiar", "c6_2"),
    likert("Apertura a experiencias", "c6_3"),
]
capa6 = np.mean(c6)

# =========================
# CAPA 7 · CULTURAL
# =========================
st.header("Capa 7 · Contexto cultural")
culture = st.radio(
    "Entorno cultural dominante",
    [
        "Alta presión competitiva",
        "Colectivista/familiar",
        "Mixto",
        "Estable y predecible"
    ],
    key="c7"
)

culture_mod = {
    "Alta presión competitiva": {"neuroticism": +0.2},
    "Colectivista/familiar": {"agreeableness": +0.3},
    "Mixto": {},
    "Estable y predecible": {"neuroticism": -0.2}
}[culture]

# =========================
# RESULTADO
# =========================
st.divider()
if st.button("Calcular perfil científico"):
    traits = {
        "neuroticism": normalize(np.mean([capa1, capa2, capa4])),
        "conscientiousness": normalize(np.mean([capa2, capa3])),
        "extraversion": normalize(np.mean([capa1, capa3, capa6])),
        "openness": normalize(np.mean([capa3, capa6, capa7 := 3])),
        "agreeableness": normalize(np.mean([capa4, capa7])),
    }

    for mod in [env_mod, body_mod, change_mod, belief_mod, prenatal_mod, culture_mod]:
        traits = apply_modifiers(traits, mod)

    st.subheader("Perfil de Personalidad (Big Five)")
    for k, v in traits.items():
        st.write(f"{k.capitalize()}: **{v:.2f} / 5**")

    attachment = (
        "Seguro" if capa4 >= 3.8 else
        "Ansioso" if traits["neuroticism"] >= 4 else
        "Evitativo funcional" if traits["conscientiousness"] >= 3 else
        "Mixto"
    )

    st.markdown("### Síntesis")
    st.write(f"""
    - Estilo de apego probable: **{attachment}**
    - Rasgo dominante: **{max(traits, key=traits.get)}**
    - Rasgo vulnerable: **{min(traits, key=traits.get)}**

    Este perfil describe tu **estado actual**, no una identidad fija.
    """)

    st.markdown("### Etapa siguiente")
    st.write("Etapa 2 permitirá simular y optimizar personalidades objetivo.")

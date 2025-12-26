import streamlit as st
import numpy as np

st.set_page_config(page_title="Perfil Determinista · Etapas 1 y 2", layout="centered")
st.title("Perfil Determinista de Personalidad")
st.write("Modelo científico por capas causales + análisis de rasgos (Big Five).")

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
# RESULTADO · ETAPA 1
# =========================
st.divider()
if st.button("Calcular perfil científico"):
    traits = {
        "Neuroticism": normalize(np.mean([capa1, capa2, capa4])),
        "Conscientiousness": normalize(np.mean([capa2, capa3])),
        "Extraversion": normalize(np.mean([capa1, capa3, capa6])),
        "Openness": normalize(np.mean([capa3, capa6, 3])),
        "Agreeableness": normalize(np.mean([capa4, 3])),
    }

    for mod in [env_mod, body_mod, change_mod, belief_mod, prenatal_mod, culture_mod]:
        traits = apply_modifiers(traits, mod)

    st.subheader("Perfil de Personalidad (Big Five)")
    for k, v in traits.items():
        st.write(f"{k}: **{v:.2f} / 5**")

    # =========================
    # ETAPA 2 · INTERPRETACIÓN
    # =========================
    st.divider()
    st.header("Etapa 2 · Interpretación científica integrada")

    def explain_trait(name, value):
        if name == "Neuroticism":
            return (
                "Indica sensibilidad del sistema nervioso ante estrés y amenaza. "
                "Valores elevados implican mayor reactividad emocional, vigilancia interna "
                "y propensión a rumiación. Bien regulado, favorece conciencia; mal regulado, desgaste."
                if value >= 3.5 else
                "Estabilidad emocional funcional y menor reactividad al estrés."
            )

        if name == "Conscientiousness":
            return (
                "Refleja disciplina, autocontrol y capacidad de sostener hábitos. "
                "Valores medios indican potencial alto pero dependencia de estructura externa."
                if value < 3.5 else
                "Alta automatización conductual y persistencia."
            )

        if name == "Extraversion":
            return (
                "Orientación introspectiva. La energía se recupera en soledad; "
                "la sobreestimulación social genera fatiga."
                if value < 3.2 else
                "Alta energía social y búsqueda de estímulo externo."
            )

        if name == "Openness":
            return (
                "Cognición pragmática, orientada a utilidad y ejecución."
                if value < 3.2 else
                "Alta curiosidad intelectual y exploración conceptual."
            )

        if name == "Agreeableness":
            return (
                "Cooperación equilibrada con límites personales."
                if value >= 3 else
                "Estilo interpersonal más defensivo o competitivo."
            )

    for k, v in traits.items():
        st.markdown(f"**{k}: {v:.2f} / 5**  \n{explain_trait(k, v)}")

    st.markdown("### Síntesis integrada")
    st.write(
        "El perfil resultante describe una personalidad sensible al entorno interno, "
        "con capacidad cognitiva y potencial alto de rendimiento, cuyo principal cuello "
        "de botella no es la capacidad sino la regulación emocional y la estructura conductual. "
        "Este perfil es dinámico y puede optimizarse mediante sistemas, no fuerza de voluntad."
    )

    st.markdown("### Próximo paso")
    st.write("Etapa 3 permitirá definir personalidad objetivo y estrategias de reprogramación.")

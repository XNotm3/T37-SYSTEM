import streamlit as st
import numpy as np

# =========================
# UTILIDADES BASE
# =========================

def normalize(value, min_val=1.0, max_val=5.0):
    return max(min(value, max_val), min_val)


def apply_modifiers(traits, modifiers):
    for k, v in modifiers.items():
        key = k.capitalize()
        if key in traits:
            traits[key] += v
    return {k: normalize(v) for k, v in traits.items()}


# =========================
# MODELO CIENTÍFICO BIG FIVE
# =========================

BASE_TRAITS = {
    "Neuroticism": 3.0,
    "Conscientiousness": 3.0,
    "Extraversion": 3.0,
    "Openness": 3.0,
    "Agreeableness": 3.0
}

# =========================
# ETAPA 1 — INPUT GUIADO
# =========================

BEHAVIOR_OPTIONS = {
    "Rutina diaria": {
        "Alta disciplina": {"conscientiousness": +0.6},
        "Irregular": {"conscientiousness": -0.4},
        "Caótica": {"conscientiousness": -0.8}
    },
    "Respuesta al estrés": {
        "Calmado": {"neuroticism": -0.6},
        "Variable": {"neuroticism": +0.2},
        "Reactivo": {"neuroticism": +0.7}
    },
    "Interacción social": {
        "Reservado": {"extraversion": -0.5},
        "Balanceado": {},
        "Dominante": {"extraversion": +0.6}
    },
    "Apertura al cambio": {
        "Resistente": {"openness": -0.5},
        "Selectivo": {},
        "Explorador": {"openness": +0.6}
    },
    "Trato interpersonal": {
        "Competitivo": {"agreeableness": -0.4},
        "Neutral": {},
        "Cooperativo": {"agreeableness": +0.5}
    }
}

# =========================
# ETAPA 2 — SÍNTESIS CIENTÍFICA
# =========================

def explain_trait(name, value):
    if name == "Neuroticism":
        return (
            "Indica estabilidad emocional. "
            "Valores altos sugieren reactividad al estrés, ansiedad y volatilidad afectiva. "
            "Valores bajos reflejan control emocional, resiliencia y respuesta adaptativa."
        )
    if name == "Conscientiousness":
        return (
            "Mide autodisciplina, organización y orientación a objetivos. "
            "Valores altos correlacionan con ejecución consistente y fiabilidad conductual. "
            "Valores bajos indican impulsividad y dificultad para sostener sistemas."
        )
    if name == "Extraversion":
        return (
            "Refleja nivel de activación social y dominancia conductual. "
            "Valores altos implican asertividad y búsqueda de estímulo. "
            "Valores bajos indican introspección y preferencia por bajo estímulo."
        )
    if name == "Openness":
        return (
            "Representa flexibilidad cognitiva y exploración conceptual. "
            "Valores altos favorecen innovación y pensamiento abstracto. "
            "Valores bajos tienden a estructuras rígidas y conservadurismo cognitivo."
        )
    if name == "Agreeableness":
        return (
            "Evalúa cooperación y orientación prosocial. "
            "Valores altos indican empatía y armonización. "
            "Valores bajos reflejan competitividad y enfoque individualista."
        )


# =========================
# ETAPA 3 — PERSONALIDAD OBJETIVO
# =========================

TARGET_PROFILES = {
    "Estratega disciplinado (INTJ-like)": {
        "Neuroticism": 1.8,
        "Conscientiousness": 4.6,
        "Extraversion": 2.6,
        "Openness": 4.2,
        "Agreeableness": 2.5
    },
    "Líder dominante": {
        "Neuroticism": 2.2,
        "Conscientiousness": 4.3,
        "Extraversion": 4.5,
        "Openness": 3.4,
        "Agreeableness": 2.7
    },
    "Explorador creativo": {
        "Neuroticism": 2.8,
        "Conscientiousness": 3.2,
        "Extraversion": 3.5,
        "Openness": 4.8,
        "Agreeableness": 3.3
    }
}


def compare_profiles(current, target):
    interventions = {}
    for k in current:
        diff = round(target[k] - current[k], 2)
        if abs(diff) >= 0.3:
            interventions[k] = diff
    return interventions


# =========================
# STREAMLIT APP
# =========================

st.set_page_config(page_title="T37 Personality System", layout="centered")
st.title("Sistema Científico de Perfil de Personalidad")

traits = BASE_TRAITS.copy()
applied_modifiers = {}

st.header("Etapa 1 — Selección conductual")

for category, options in BEHAVIOR_OPTIONS.items():
    choice = st.selectbox(category, list(options.keys()))
    mods = options[choice]
    for k, v in mods.items():
        applied_modifiers[k] = applied_modifiers.get(k, 0) + v

traits = apply_modifiers(traits, applied_modifiers)

st.header("Etapa 2 — Perfil de personalidad actual")

for trait, value in traits.items():
    st.subheader(f"{trait}: {round(value,2)} / 5")
    st.write(explain_trait(trait, value))

st.header("Etapa 3 — Comparativa con personalidad objetivo")

target_name = st.selectbox("Selecciona personalidad deseada", list(TARGET_PROFILES.keys()))
target_traits = TARGET_PROFILES[target_name]

st.subheader("Comparación cuantitativa")

for trait in traits:
    st.write(
        f"{trait} → Actual: {round(traits[trait],2)} | "
        f"Deseado: {target_traits[trait]}"
    )

interventions = compare_profiles(traits, target_traits)

st.subheader("Rasgos a intervenir")

if not interventions:
    st.write("Perfil alineado. No se requieren intervenciones significativas.")
else:
    for trait, diff in interventions.items():
        direction = "Incrementar" if diff > 0 else "Reducir"
        st.write(f"{trait}: {direction} en {abs(diff)} puntos")

st.markdown("---")
st.caption("Modelo basado en el marco Big Five (Costa & McCrae).")

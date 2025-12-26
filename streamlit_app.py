import streamlit as st
import numpy as np

st.set_page_config(page_title="Perfil de Personalidad – Etapa 1", layout="centered")

st.title("Análisis de Personalidad (Big Five)")
st.markdown("""
Evaluación basada en el **Modelo de los Cinco Grandes (Big Five)**, validado empíricamente
en psicología diferencial.  
Los resultados representan **tendencias probabilísticas**, no diagnósticos clínicos.
""")

# -----------------------------
# CONFIGURACIÓN BASE
# -----------------------------
TRAITS = {
    "neuroticism": 0.0,
    "conscientiousness": 0.0,
    "extraversion": 0.0,
    "openness": 0.0,
    "agreeableness": 0.0
}

COUNT = {
    "neuroticism": 0,
    "conscientiousness": 0,
    "extraversion": 0,
    "openness": 0,
    "agreeableness": 0
}

def add(trait, value):
    TRAITS[trait] += value
    COUNT[trait] += 1

# -----------------------------
# CAPA 1 – REGULACIÓN EMOCIONAL
# -----------------------------
st.header("1. Regulación emocional")

q1 = st.radio(
    "Cuando enfrentas estrés intenso:",
    [
        "Me altera fácilmente y me cuesta soltarlo",
        "Me afecta, pero logro estabilizarme",
        "Rara vez me altera",
        "Otro"
    ]
)

if q1 == "Me altera fácilmente y me cuesta soltarlo":
    add("neuroticism", 4.5)
elif q1 == "Me afecta, pero logro estabilizarme":
    add("neuroticism", 3.5)
elif q1 == "Rara vez me altera":
    add("neuroticism", 2.0)
else:
    add("neuroticism", 3.5)

# -----------------------------
# CAPA 2 – DISCIPLINA Y HÁBITOS
# -----------------------------
st.header("2. Disciplina y hábitos")

q2 = st.radio(
    "Respecto a tus hábitos diarios:",
    [
        "Soy inconsistente, dependo del ánimo",
        "Puedo ser disciplinado con estructura externa",
        "Soy constante y autoorganizado",
        "Otro"
    ]
)

if q2 == "Soy inconsistente, dependo del ánimo":
    add("conscientiousness", 2.3)
elif q2 == "Puedo ser disciplinado con estructura externa":
    add("conscientiousness", 3.2)
elif q2 == "Soy constante y autoorganizado":
    add("conscientiousness", 4.4)
else:
    add("conscientiousness", 3.0)

# -----------------------------
# CAPA 3 – ENERGÍA SOCIAL
# -----------------------------
st.header("3. Energía social")

q3 = st.radio(
    "En contextos sociales prolongados:",
    [
        "Me drenan rápidamente",
        "Puedo manejarlo, pero necesito pausas",
        "Me energizan",
        "Otro"
    ]
)

if q3 == "Me drenan rápidamente":
    add("extraversion", 2.2)
elif q3 == "Puedo manejarlo, pero necesito pausas":
    add("extraversion", 3.0)
elif q3 == "Me energizan":
    add("extraversion", 4.5)
else:
    add("extraversion", 3.0)

# -----------------------------
# CAPA 4 – APERTURA COGNITIVA
# -----------------------------
st.header("4. Apertura cognitiva")

q4 = st.radio(
    "Cuando enfrentas ideas nuevas:",
    [
        "Prefiero lo probado y funcional",
        "Evalúo si es útil antes de adoptarlo",
        "Me atrae explorar ideas nuevas",
        "Otro"
    ]
)

if q4 == "Prefiero lo probado y funcional":
    add("openness", 2.4)
elif q4 == "Evalúo si es útil antes de adoptarlo":
    add("openness", 3.0)
elif q4 == "Me atrae explorar ideas nuevas":
    add("openness", 4.4)
else:
    add("openness", 3.0)

# -----------------------------
# CAPA 5 – COOPERACIÓN SOCIAL
# -----------------------------
st.header("5. Cooperación y límites")

q5 = st.radio(
    "En relaciones y trabajo en equipo:",
    [
        "Prioritizo mis intereses",
        "Busco equilibrio entre cooperación y límites",
        "Suelo ceder para mantener armonía",
        "Otro"
    ]
)

if q5 == "Prioritizo mis intereses":
    add("agreeableness", 2.5)
elif q5 == "Busco equilibrio entre cooperación y límites":
    add("agreeableness", 3.2)
elif q5 == "Suelo ceder para mantener armonía":
    add("agreeableness", 4.4)
else:
    add("agreeableness", 3.0)

# -----------------------------
# NORMALIZACIÓN
# -----------------------------
results = {}
for trait in TRAITS:
    if COUNT[trait] > 0:
        results[trait] = TRAITS[trait] / COUNT[trait]
    else:
        results[trait] = 3.0

# -----------------------------
# EXPLICACIONES
# -----------------------------
def explain(trait, value):
    if trait == "neuroticism":
        return (
            "Nivel elevado de reactividad emocional. El sistema nervioso responde con "
            "intensidad al estrés y a la incertidumbre. Bien regulado, aumenta conciencia "
            "y anticipación; sin regulación, puede generar rumiación y tensión sostenida."
            if value >= 3.5 else
            "Reactividad emocional moderada. Capacidad funcional de respuesta al estrés "
            "sin desbordamiento frecuente."
        )

    if trait == "conscientiousness":
        return (
            "Capacidad funcional de disciplina, pero dependiente de estructura externa. "
            "No hay déficit de capacidad, sino de automatización conductual."
            if value < 3.5 else
            "Alta autodisciplina, organización y persistencia orientada a objetivos."
        )

    if trait == "extraversion":
        return (
            "Orientación introspectiva. La energía se recupera en contextos controlados "
            "y de baja estimulación social."
            if value < 3.2 else
            "Buena tolerancia a la interacción social y estímulos externos."
        )

    if trait == "openness":
        return (
            "Preferencia por lo funcional y comprobado. La exploración ocurre solo cuando "
            "existe utilidad clara."
            if value < 3.2 else
            "Alta curiosidad intelectual y disposición a explorar ideas nuevas."
        )

    if trait == "agreeableness":
        return (
            "Cooperación equilibrada con límites personales definidos."
            if value >= 3.0 else
            "Estilo más competitivo o reservado emocionalmente."
        )

# -----------------------------
# RESULTADOS
# -----------------------------
st.header("Resultados")

for trait, value in results.items():
    st.markdown(f"""
**{trait.capitalize()}: {value:.2f} / 5**  
{explain(trait, value)}
""")

st.markdown("""
---
**Nota metodológica:**  
Este perfil describe **tendencias estadísticas de comportamiento**, no identidades fijas.
En la siguiente etapa, estos resultados pueden ser interpretados por un modelo de IA
para generar **hipótesis dinámicas, riesgos conductuales y trayectorias de optimización**.
""")

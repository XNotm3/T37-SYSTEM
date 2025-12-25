import streamlit as st
import random
import json

st.set_page_config(page_title="T37 PERSONALITY SYSTEM v7.0", layout="wide")

# Estilos CSS para tema cyberpunk minimalista
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #e0e0e0;
    }
    h1, h2, h3, h4, .monospace {
        font-family: 'Courier New', Courier, monospace;
    }
    .neon-blue {
        color: #00bfff;
        text-shadow: 0 0 10px #00bfff, 0 0 20px #00bfff;
    }
    .red-neon > div > div > div > div {
        background: #ff0000 !important;
        box-shadow: 0 0 10px #ff0000 !important;
    }
    .orange-neon > div > div > div > div {
        background: #ff8c00 !important;
        box-shadow: 0 0 10px #ff8c00 !important;
    }
    .yellow-neon > div > div > div > div {
        background: #ffff00 !important;
        box-shadow: 0 0 10px #ffff00 !important;
    }
    .green-neon > div > div > div > div {
        background: #00ff00 !important;
        box-shadow: 0 0 10px #00ff00 !important;
    }
</style>
""", unsafe_allow_html=True)

# Definición de capas
layers = {
    "🔴 NÚCLEO": {
        "mod": "5-10% modificable",
        "color_class": "red-neon",
        "components": ["Genética heredada", "Exposición prenatal", "Neurodesarrollo crítico (0-3 años)"],
        "explanations": [
            "Herencia genética que predispone rasgos temperamentales (estudios de gemelos, Sapolsky).",
            "Exposición a hormonas y estrés en útero que moldea el eje HPA (Sapolsky, estrés prenatal).",
            "Períodos críticos de desarrollo cerebral temprana con plasticidad máxima (Sapolsky, neurodesarrollo)."
        ]
    },
    "🟠 PROFUNDAS": {
        "mod": "20-40% modificable",
        "color_class": "orange-neon",
        "components": ["Estilo de apego", "Esquemas maladaptativos", "Narrativa cultural"],
        "explanations": [
            "Patrones de apego formados en infancia (Bowlby/Ainsworth, regulación emocional).",
            "Creencias núcleo maladaptativas (Beck, terapia cognitiva esquemas).",
            "Narrativas culturales internalizadas que definen identidad y valores (Sapolsky, cultura)."
        ]
    },
    "🟡 MEDIAS": {
        "mod": "60-80% modificable",
        "color_class": "yellow-neon",
        "components": ["Fisiología actual", "Hábitos ejecutivos", "Experiencias adultas reforzantes"],
        "explanations": [
            "Estado fisiológico actual (hormonas, inflamación, neuroquímica, Sapolsky).",
            "Hábitos de función ejecutiva (planificación, autocontrol prefrontal).",
            "Experiencias adultas que refuerzan vías neurales (aprendizaje hebbiano)."
        ]
    },
    "🟢 EXTERNAS": {
        "mod": "90-100% modificable",
        "color_class": "green-neon",
        "components": ["Personas cercanas", "Contenido consumido", "Espacio físico", "Estado momento-a-momento", "Conciencia interna"],
        "explanations": [
            "Influencia social de círculo cercano (mirror neurons, conformidad).",
            "Contenido mediático e informational consumido diariamente.",
            "Entorno físico y ergonomía que moldea comportamiento.",
            "Estado transitorio (sueño, hambre, estrés agudo).",
            "Nivel de mindfulness y auto-observación interna."
        ]
    }
}

# Modos predefinidos
predefined_modes = {
    "Titán Máximo": {comp: round(random.uniform(90, 100), 1) for layer in layers.values() for comp in layer["components"]},
    "Sabio Estoico": {"Genética heredada":75, "Exposición prenatal":75, "Neurodesarrollo crítico (0-3 años)":80, "Estilo de apego":95, "Esquemas maladaptativos":10, "Narrativa cultural":90, "Fisiología actual":85, "Hábitos ejecutivos":95, "Experiencias adultas reforzantes":90, "Personas cercanas":80, "Contenido consumido":95, "Espacio físico":85, "Estado momento-a-momento":90, "Conciencia interna":98},
    "Flow Creativo": {"Genética heredada":70, "Exposición prenatal":70, "Neurodesarrollo crítico (0-3 años)":75, "Estilo de apego":85, "Esquemas maladaptativos":15, "Narrativa cultural":85, "Fisiología actual":90, "Hábitos ejecutivos":75, "Experiencias adultas reforzantes":98, "Personas cercanas":80, "Contenido consumido":98, "Espacio físico":95, "Estado momento-a-momento":85, "Conciencia interna":90},
    "Supervivencia": {comp: round(random.uniform(10, 40), 1) for layer in layers.values() for comp in layer["components"]},
    "Social Carismático": {"Genética heredada":80, "Exposición prenatal":80, "Neurodesarrollo crítico (0-3 años)":80, "Estilo de apego":98, "Esquemas maladaptativos":5, "Narrativa cultural":95, "Fisiología actual":85, "Hábitos ejecutivos":70, "Experiencias adultas reforzantes":90, "Personas cercanas":98, "Contenido consumido":90, "Espacio físico":85, "Estado momento-a-momento":95, "Conciencia interna":85},
    "Recuperación Profunda": {"Genética heredada":50, "Exposición prenatal":50, "Neurodesarrollo crítico (0-3 años)":55, "Estilo de apego":70, "Esquemas maladaptativos":60, "Narrativa cultural":70, "Fisiología actual":40, "Hábitos ejecutivos":30, "Experiencias adultas reforzantes":

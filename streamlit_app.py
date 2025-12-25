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
    "Recuperación Profunda": {"Genética heredada":50, "Exposición prenatal":50, "Neurodesarrollo crítico (0-3 años)":55, "Estilo de apego":70, "Esquemas maladaptativos":60, "Narrativa cultural":70, "Fisiología actual":40, "Hábitos ejecutivos":30, "Experiencias adultas reforzantes":50, "Personas cercanas":75, "Contenido consumido":60, "Espacio físico":85, "Estado momento-a-momento":30, "Conciencia interna":95}
}

# Inicialización segura de session_state
if 'values' not in st.session_state:
    st.session_state.values = {}
    for layer in layers.values():
        for comp in layer["components"]:
            st.session_state.values[comp] = 50.0

# Funciones sidebar
def apply_mode(values_dict):
    for comp, val in values_dict.items():
        st.session_state.values[comp] = val

def reset_all():
    for comp in st.session_state.values:
        st.session_state.values[comp] = 50.0

def randomize_all():
    for comp in st.session_state.values:
        st.session_state.values[comp] = round(random.uniform(0, 100), 1)

# Sidebar
with st.sidebar:
    st.markdown("<h2 class='neon-blue'>Modos Rápidos</h2>", unsafe_allow_html=True)
    for mode_name in predefined_modes:
        if st.button(mode_name):
            apply_mode(predefined_modes[mode_name])
            st.rerun()

    col_reset, col_rand = st.columns(2)
    with col_reset:
        if st.button("RESET"):
            reset_all()
            st.rerun()
    with col_rand:
        if st.button("RANDOM"):
            randomize_all()
            st.rerun()

    st.markdown("### Guardar / Cargar Perfil")
    profile_name = st.text_input("Nombre del perfil")
    save_col, load_col = st.columns(2)
    with save_col:
        if st.button("Guardar") and profile_name:
            data = json.dumps(st.session_state.values)
            st.download_button(
                label=f"Descargar {profile_name}",
                data=data,
                file_name=f"{profile_name}.json",
                mime="application/json"
            )
    with load_col:
        uploaded_file = st.file_uploader("Subir JSON", type=["json"])
        if uploaded_file and st.button("Cargar") and profile_name:
            data = json.load(uploaded_file)
            st.session_state.values.update({k: float(v) for k, v in data.items()})
            st.rerun()

# Título principal
st.markdown("<h1 class='neon-blue'>T37 PERSONALITY SYSTEM v7.0</h1>", unsafe_allow_html=True)

# Tabs por capa
tabs = st.tabs(list(layers.keys()))

layer_averages = {}

for tab, (layer_key, layer_info) in zip(tabs, layers.items()):
    with tab:
        st.markdown(f"<strong>Modificabilidad: {layer_info['mod']}</strong>", unsafe_allow_html=True)
        
        component_values = []
        for idx, component in enumerate(layer_info["components"]):
            col_name, col_help = st.columns([5, 1])
            with col_name:
                st.write(component)
            with col_help:
                with st.expander("?"):
                    st.caption(layer_info["explanations"][idx])
            
            current_val = st.session_state.values.get(component, 50.0)
            new_val = st.slider(" ", 0.0, 100.0, current_val, key=f"{layer_key}_{component}")
            st.session_state.values[component] = new_val
            component_values.append(new_val)
        
        layer_avg = sum(component_values) / len(component_values) if component_values else 0
        layer_averages[layer_key] = layer_avg
        
        st.markdown(f"<p>Media de capa: <strong>{layer_avg:.1f}%</strong></p>", unsafe_allow_html=True)
        st.progress(layer_avg / 100)
        # Slider global disabled con neon
        st.markdown(f"<div class='{layer_info['color_class']}'>", unsafe_allow_html=True)
        st.progress(layer_avg / 100)
        st.markdown("</div>", unsafe_allow_html=True)

# Diagnóstico final
st.markdown("<h2 class='neon-blue'>DIAGNÓSTICO FINAL</h2>", unsafe_allow_html=True)

global_score = sum(layer_averages.values()) / len(layer_averages) if layer_averages else 0

# Determinación del perfil
if global_score >= 90:
    profile = "🗿 TITÁN OPTIMIZADO"
elif global_score >= 75:
    profile = "⚡ GUERRERO AVANZADO"
elif global_score >= 55:
    profile = "🌱 CRECIENTE EQUILIBRADO"
else:
    profile = "🔥 EN RECONSTRUCCIÓN"

st.markdown(f"<h3 class='neon-blue'>{profile}</h3>", unsafe_allow_html=True)
st.progress(global_score / 100)
st.markdown(f"<strong>Score Global: {global_score:.1f}%</strong>", unsafe_allow_html=True)

# Radar de rasgos (6 rasgos derivados)
traits = {
    "Resiliencia": (layer_averages.get("🔴 NÚCLEO", 0) * 0.5 + layer_averages.get("🟠 PROFUNDAS", 0) * 0.5),
    "Autocontrol": (layer_averages.get("🟡 MEDIAS", 0) * 0.7 + layer_averages.get("🟢 EXTERNAS", 0) * 0.3),
    "Adaptabilidad": layer_averages.get("🟢 EXTERNAS", 0),
    "Estabilidad Emocional": (layer_averages.get("🔴 NÚCLEO", 0) * 0.6 + layer_averages.get("🟠 PROFUNDAS", 0) * 0.4),
    "Creatividad / Flow": (layer_averages.get("🟡 MEDIAS", 0) * 0.6 + layer_averages.get("🟢 EXTERNAS", 0) * 0.4),
    "Carisma Social": (layer_averages.get("🟠 PROFUNDAS", 0) * 0.4 + layer_averages.get("🟢 EXTERNAS", 0) * 0.6)
}

st.markdown("<h4 class='neon-blue'>RADAR DE RASGOS</h4>", unsafe_allow_html=True)
for trait_name, trait_score in traits.items():
    st.progress(trait_score / 100)
    st.caption(f"{trait_name}: {trait_score:.1f}%")

# Bottleneck y consejo
if layer_averages:
    bottleneck = min(layer_averages, key=layer_averages.get)
    bottleneck_score = layer_averages[bottleneck]
    st.markdown(f"<strong>Bottleneck detectado:</strong> {bottleneck} ({bottleneck_score:.1f}%)", unsafe_allow_html=True)
    st.markdown("<strong>Consejo clave:</strong> Prioriza mejorar los componentes de esta capa para obtener gains rápidos y desbloquear tu potencial global.", unsafe_allow_html=True)

# Descripción del perfil
profile_desc = {
    "🗿 TITÁN OPTIMIZADO": "Integración máxima. Eres un titán en control total de tu personalidad. Mantén y refina.",
    "⚡ GUERRERO AVANZADO": "Alto rendimiento sostenido. Enfócate en capas medias y externas para alcanzar la cima.",
    "🌱 CRECIENTE EQUILIBRADO": "Buen progreso general. Ataca tu bottleneck para acelerar el crecimiento.",
    "🔥 EN RECONSTRUCCIÓN": "Fase de transformación poderosa. Comienza por capas externas para momentum rápido."
}
st.markdown(f"<p>{profile_desc[profile.split(' ')[1]]}</p>", unsafe_allow_html=True)

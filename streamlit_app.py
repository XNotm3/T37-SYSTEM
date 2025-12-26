import streamlit as st
import pandas as pd
import plotly.express as px

# ===================== CONFIGURACIÓN DE PÁGINA =====================
st.set_page_config(
    page_title="HACKING MY BRAIN",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== ESTILO PERSONALIZADO =====================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
    
    .main {
        background-color: #000000;
        color: #00ffff;
    }
    .stApp {
        background-color: #000000;
    }
    h1 {
        font-family: 'Orbitron', sans-serif;
        color: #00ffff;
        text-align: center;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff;
        margin-bottom: 30px;
    }
    .stMarkdown, .stText {
        color: #00ffff;
    }
    .stSlider > label {
        color: #00ffff !important;
    }
    .stSelectbox > label {
        color: #00ffff !important;
    }
    hr {
        border-color: #00ffff;
        box-shadow: 0 0 10px #00ffff;
    }
    </style>
    """, unsafe_allow_html=True)

# ===================== TÍTULO =====================
st.markdown("<h1>HACKING MY BRAIN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00ffff;'>Determinismo práctico: entiende quién eres y simula quién podrías llegar a ser.</p>", unsafe_allow_html=True)
st.markdown("---")

# ===================== SESIÓN STATE =====================
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'perfil_base' not in st.session_state:
    st.session_state.perfil_base = None

# ===================== PERSONALIDADES ÓPTIMAS CIENTÍFICAS =====================
personalidades_optimas = {
    "Arquitecto Resiliente": {
        "desc": "Alta Conscientiousness + Baja Neuroticism → Mayor longevidad, éxito profesional y salud mental (Grant Study, Dunedin)",
        "O": 60, "C": 90, "E": 65, "A": 70, "N": 20
    },
    "Explorador Empático": {
        "desc": "Alta Openness + Alta Agreeableness → Creatividad social, innovación y relaciones profundas",
        "O": 90, "C": 70, "E": 75, "A": 85, "N": 40
    },
    "Líder Equilibrado": {
        "desc": "Extraversion moderada-alta + Alta Emotional Stability → Influencia natural y resiliencia bajo presión",
        "O": 70, "C": 80, "E": 85, "A": 75, "N": 25
    },
    "Sabio Contemplativo": {
        "desc": "Alta Openness + Baja Neuroticism + Conscientiousness alta → Felicidad subjetiva máxima (meta-análisis)",
        "O": 85, "C": 80, "E": 50, "A": 80, "N": 15
    },
    "Guerrero Adaptativo": {
        "desc": "Alta resiliencia post-trauma: Conscientiousness y Emotional Stability muy altas",
        "O": 65, "C": 95, "E": 60, "A": 75, "N": 10
    }
}

# ===================== ETAPA 1: CUESTIONARIO =====================
if st.session_state.etapa == 1:
    st.header("🧠 Etapa 1: ¿Quién soy ahora?")
    st.info("Responde honestamente. Tus respuestas determinarán tu perfil base según el modelo de 7 capas de condicionamiento.")

    with st.form("cuestionario_form"):
        # Capa 1 - Inmediata
        st.subheader("1. Inmediata (momentos del día)")
        c1_1 = st.slider("Cuando estoy cansado o con hambre, me vuelvo más irritable o impulsivo", 1, 5, 3, key="c1_1")
        c1_2 = st.slider("Puedo calmarme rápidamente cuando me enojo (respiración, pausa)", 1, 5, 3, key="c1_2")
        c1_3 = st.slider("Los estímulos sensoriales (ruido, luz) me afectan mucho el humor", 1, 5, 3, key="c1_3")
        c1_4 = st.slider("Practico mindfulness o técnicas de regulación diaria", 1, 5, 2, key="c1_4")

        # Capa 2 - Hormonal/Fisiológica
        st.subheader("2. Hormonal y fisiológica")
        c2_1 = st.slider("Me siento estresado/ansioso la mayor parte del día", 1, 5, 3, key="c2_1")
        c2_2 = st.slider("Hago ejercicio intenso ≥3 veces/semana", 1, 5, 3, key="c2_2")
        c2_3 = st.slider("Mi dieta es saludable y antiinflamatoria", 1, 5, 3, key="c2_3")
        c2_4 = st.slider("Tengo rutina de sueño muy regular", 1, 5, 3, key="c2_4")

        # Capa 3 - Experiencias recientes
        st.subheader("3. Experiencias recientes (últimos años)")
        c3_1 = st.slider("He cambiado hábitos importantes con éxito recientemente", 1, 5, 3, key="c3_1")
        c3_2 = st.selectbox("¿Estás actualmente en terapia o coaching?", ["No", "Sí, TCC/ACT", "Sí, profunda (EMDR, esquemas)", "Sí, otro"], key="c3_2")
        c3_3 = st.slider("Me expongo regularmente a situaciones sociales nuevas", 1, 5, 3, key="c3_3")

        # Capa 4 - Desarrollo temprano
        st.subheader("4. Desarrollo temprano (infancia/adolescencia)")
        c4_1 = st.slider("Tuve apego seguro con al menos un cuidador", 1, 5, 3, key="c4_1")
        c4_2 = st.slider("Experimenté negligencia emocional o física", 1, 5, 2, key="c4_2")
        c4_3 = st.slider("Hubo conflictos o violencia frecuentes en casa", 1, 5, 2, key="c4_3")
        c4_4 = st.slider("Recibí mucho estímulo intelectual y emocional", 1, 5, 3, key="c4_4")

        # Capa 5, 6 y 7 - Resumen rápido
        st.subheader("5-7. Capas profundas (prenatal, genética, cultural)")
        c567 = st.slider("En general, creo que mis capas profundas (genética, infancia temprana, cultura) me limitan bastante", 1, 5, 3, key="c567")

        submitted = st.form_submit_button("Generar mi perfil determinista →")

        if submitted:
            # Cálculo simple del perfil Big Five base (aproximación educativa)
            openness = int((c1_4 + c3_1 + c4_4 + (6 - c567)) / 4 * 20)
            conscientiousness = int((c2_2 + c2_4 + c3_1 + c1_2) / 4 * 20)
            extraversion = int((c3_3 + (6 - c2_1) + (6 - c4_3)) / 3 * 20)
            agreeableness = int((c4_1 + (6 - c4_2) + c2_3) / 3 * 20)
            neuroticism = int((c2_1 + c1_1 + c4_2 + c4_3 + c567) / 5 * 20)

            st.session_state.perfil_base = {
                "Openness": max(0, min(100, openness)),
                "Conscientiousness": max(0, min(100, conscientiousness)),
                "Extraversion": max(0, min(100, extraversion)),
                "Agreeableness": max(0, min(100, agreeableness)),
                "Neuroticism": max(0, min(100, neuroticism))
            }
            st.session_state.etapa = 2
            st.rerun()

# ===================== ETAPA 2: SLIDERS Y PERSONALIDADES ÓPTIMAS =====================
if st.session_state.etapa == 2:
    st.header("⚡ Etapa 2: Simulación de cambio")
    st.success("¡Perfil base generado! Ahora puedes explorar cambios realistas a tus ~30 años.")

    base = st.session_state.perfil_base

    # Radar chart del perfil actual
    df_radar = pd.DataFrame(dict(
        r=list(base.values()),
        theta=list(base.keys())
    ))
    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, range_r=[0,100])
    fig.update_traces(fill='toself', fillcolor='rgba(0,255,255,0.2)', line_color='#00ffff')
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])),
                      paper_bgcolor='black', plot_bgcolor='black', font_color='#00ffff')
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Sliders de modificabilidad")
        st.info("Límites realistas a los 30 años (±20-40% máx por rasgo)")
        
        new_O = st.slider("Openness", 0, 100, base["Openness"], step=5, key="s_O")
        new_C = st.slider("Conscientiousness", 0, 100, base["Conscientiousness"], step=5, key="s_C")
        new_E = st.slider("Extraversion", 0, 100, base["Extraversion"], step=5, key="s_E")
        new_A = st.slider("Agreeableness", 0, 100, base["Agreeableness"], step=5, key="s_A")
        new_N = st.slider("Neuroticism (bajo = más estabilidad)", 0, 100, base["Neuroticism"], step=5, key="s_N")

    with col2:
        st.subheader("Personalidades óptimas científicas")
        seleccion = st.selectbox("Elige una para cargar sus valores objetivo", ["Ninguna"] + list(personalidades_optimas.keys()))
        
        if seleccion != "Ninguna":
            opt = personalidades_optimas[seleccion]
            st.write(f"**{seleccion}**")
            st.write(opt["desc"])
            if st.button(f"Cargar valores de {seleccion}"):
                new_O = opt["O"]
                new_C = opt["C"]
                new_E = opt["E"]
                new_A = opt["A"]
                new_N = opt["N"]
                st.rerun()

        # Simulación final
        simulacion = {"Openness": new_O, "Conscientiousness": new_C, "Extraversion": new_E,
                     "Agreeableness": new_A, "Neuroticism": new_N}
        
        distancia = sum(abs(simulacion[k] - base[k]) for k in base) / 5
        esfuerzo = "Bajo" if distancia < 20 else "Moderado" if distancia < 40 else "Alto (3-5 años intensos)"
        
        st.markdown(f"### Distancia al cambio: **{distancia:.1f}/100** → Esfuerzo estimado: **{esfuerzo}**")

        df_sim = pd.DataFrame(dict(r=list(simulacion.values()), theta=list(simulacion.keys())))
        fig_sim = px.line_polar(df_sim, r='r', theta='theta', line_close=True, range_r=[0,100])
        fig_sim.update_traces(fill='toself', fillcolor='rgba(255,0,255,0.3)', line_color='#ff00ff')
        fig_sim.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])),
                              paper_bgcolor='black', plot_bgcolor='black', font_color='#ff00ff')
        st.plotly_chart(fig_sim, use_container_width=True)

    if st.button("Volver al cuestionario"):
        st.session_state.etapa = 1
        st.session_state.perfil_base = None
        st.rerun()

st.markdown("---")
st.caption("Inspirado en Robert Sapolsky y meta-análisis de plasticidad de personalidad. No es diagnóstico clínico.")

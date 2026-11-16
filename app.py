# app_deportiva.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página en alta resolución
st.set_page_config(
    page_title="Pro Elite Sports Analytics Hub",
    page_icon="⚽🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS avanzados para una interfaz de alta gama
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #f8fafc; }
    .metric-card {
        background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        border-color: #3b82f6;
    }
    .metric-title { font-size: 13px; color: #94a3b8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; }
    .metric-value { font-size: 30px; color: #38bdf8; font-weight: 800; margin-top: 8px; }
    </style>
""", unsafe_allow_html=True)

# Base de datos ampliada con métricas avanzadas
@st.cache_data
def cargar_datos_avanzados():
    return {
        "Fútbol (Top Leagues)": {
            "Premier League": {
                "Manchester City": {
                    "Erling Haaland": {"Goles/P": 1.12, "xG (Goles Esperados)": 1.04, "Asistencias/P": 0.20, "SCA (Acc. Creación)": 2.4, "Min/Gol": 78},
                    "Kevin De Bruyne": {"Goles/P": 0.35, "xG (Goles Esperados)": 0.28, "Asistencias/P": 0.65, "SCA (Acc. Creación)": 5.8, "Min/Gol": 210},
                    "Phil Foden": {"Goles/P": 0.45, "xG (Goles Esperados)": 0.40, "Asistencias/P": 0.35, "SCA (Acc. Creación)": 4.5, "Min/Gol": 160}
                },
                "Arsenal": {
                    "Bukayo Saka": {"Goles/P": 0.52, "xG (Goles Esperados)": 0.48, "Asistencias/P": 0.45, "SCA (Acc. Creación)": 4.9, "Min/Gol": 155},
                    "Martin Ødegaard": {"Goles/P": 0.38, "xG (Goles Esperados)": 0.31, "Asistencias/P": 0.50, "SCA (Acc. Creación)": 5.5, "Min/Gol": 190}
                }
            },
            "LaLiga": {
                "Real Madrid": {
                    "Kylian Mbappé": {"Goles/P": 1.05, "xG (Goles Esperados)": 0.98, "Asistencias/P": 0.30, "SCA (Acc. Creación)": 4.2, "Min/Gol": 82},
                    "Jude Bellingham": {"Goles/P": 0.55, "xG (Goles Esperados)": 0.50, "Asistencias/P": 0.40, "SCA (Acc. Creación)": 4.6, "Min/Gol": 140},
                    "Vinicius Jr.": {"Goles/P": 0.68, "xG (Goles Esperados)": 0.62, "Asistencias/P": 0.45, "SCA (Acc. Creación)": 5.1, "Min/Gol": 115}
                }
            }
        },
        "Baloncesto (NBA)": {
            "Conferencia Oeste": {
                "Los Angeles Lakers": {
                    "LeBron James": {"Puntos/P": 25.4, "Rebotes/P": 7.3, "Asistencias/P": 8.1, "eFG% (Tiros Efectivos)": 58.4, "TS% (Real Shooting)": 62.1},
                    "Anthony Davis": {"Puntos/P": 24.8, "Rebotes/P": 12.6, "Asistencias/P": 3.5, "eFG% (Tiros Efectivos)": 56.2, "TS% (Real Shooting)": 60.5}
                },
                "Golden State Warriors": {
                    "Stephen Curry": {"Puntos/P": 27.1, "Rebotes/P": 4.5, "Asistencias/P": 6.0, "eFG% (Tiros Efectivos)": 62.8, "TS% (Real Shooting)": 65.4},
                    "Draymond Green": {"Puntos/P": 8.9, "Rebotes/P": 7.2, "Asistencias/P": 6.1, "eFG% (Tiros Efectivos)": 54.1, "TS% (Real Shooting)": 57.0}
                }
            }
        }
    }

data = cargar_datos_avanzados()

# Sidebar de Navegación de Alta Precisión
st.sidebar.title("🎛️ Panel de Control")
st.sidebar.markdown("---")

deporte = st.sidebar.selectbox("⚽🏀 Selecciona Deporte", list(data.keys()))
liga = st.sidebar.selectbox("🏆 Competición / Conferencia", list(data[deporte].keys()))
equipo = st.sidebar.selectbox("🛡️ Selecciona Equipo", list(data[deporte][liga].keys()))
jugador = st.sidebar.selectbox("⭐ Selecciona Jugador", list(data[deporte][liga][equipo].keys()))

# Cuerpo Principal
st.title("🏆 Pro Sports Analytics Hub")
st.markdown(f"### Ficha Analítica Avanzada: **{jugador}** ({equipo})")
st.markdown("---")

stats_jugador = data[deporte][liga][equipo][jugador]

# Visualización en Tarjetas con métricas detalladas
cols = st.columns(len(stats_jugador))
for i, (metrica, valor) in enumerate(stats_jugador.items()):
    with cols[i]:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">{metrica}</div>
                <div class="metric-value">{valor}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Sección de Gráficos Interactivos de Barras Agrupadas en Alta Resolución
st.subheader("📊 Comparativa de Plantilla (Gráficos de Barras)")
st.markdown("Análisis visual de rendimiento de todos los integrantes del club seleccionado.")

# Transformación de datos para Plotly
df_equipo = pd.DataFrame([
    {"Jugador": j, **s} for j, s in data[deporte][liga][equipo].items()
])

df_melted = df_equipo.melt(id_vars="Jugador", var_name="Métrica Estadística", value_name="Valor")

# Gráfico de barras de alta fidelidad con Plotly
fig = px.bar(
    df_melted, 
    x="Jugador", 
    y="Valor", 
    color="Métrica Estadística", 
    barmode="group",
    template="plotly_dark",
    height=520
)

fig.update_layout(
    font=dict(size=14, family="Inter, sans-serif"),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(
        title="<b>Métricas</b>", 
        orientation="h", 
        yanchor="bottom", 
        y=1.02, 
        xanchor="right", 
        x=1
    ),
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, use_container_width=True)

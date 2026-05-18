"""
Corre Leve Club | Chatbot de Consultoria de Corrida
Versão visual inspirada na identidade do Instagram @ocorreleve:
vermelho vinho, preto, branco, estética club e corrida urbana.

Como rodar:
python -m streamlit run corre_leve_club_chatbot.py
"""

import streamlit as st
import pandas as pd
from datetime import date, timedelta

LOGO_B64 = "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"

st.set_page_config(
    page_title="Corre Leve Club | Consultoria de Corrida",
    page_icon="🏃‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CSS DA MARCA
# ==========================================================

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800;900&display=swap');

        :root {
            --wine: #8B0000;
            --wine-dark: #5E0000;
            --wine-soft: #B11212;
            --black: #080808;
            --graphite: #151515;
            --offwhite: #F7F1EA;
            --white: #FFFFFF;
            --gray: #B8B8B8;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background:
                linear-gradient(rgba(5,5,5,0.88), rgba(5,5,5,0.92)),
                radial-gradient(circle at top right, rgba(139,0,0,0.55), transparent 28%),
                radial-gradient(circle at bottom left, rgba(139,0,0,0.35), transparent 25%),
                #080808;
            color: var(--offwhite);
        }

        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 4rem;
            max-width: 1320px;
        }

        section[data-testid="stSidebar"] {
            background: #080808;
            border-right: 1px solid rgba(255,255,255,0.10);
        }

        section[data-testid="stSidebar"] * {
            color: var(--offwhite) !important;
        }

        .brand-logo {
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 999px;
            border: 3px solid #ffffff;
            box-shadow: 0 0 0 8px #8B0000, 0 20px 50px rgba(0,0,0,0.45);
            display: block;
            margin: 0 auto 22px auto;
        }

        .hero {
            background:
                linear-gradient(90deg, rgba(8,8,8,0.94) 0%, rgba(8,8,8,0.72) 52%, rgba(139,0,0,0.78) 100%),
                repeating-linear-gradient(135deg, rgba(255,255,255,0.035) 0px, rgba(255,255,255,0.035) 1px, transparent 1px, transparent 10px);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 0px;
            padding: 46px 48px;
            box-shadow: 0 24px 70px rgba(0,0,0,0.55);
            margin-bottom: 26px;
            position: relative;
            overflow: hidden;
        }

        .hero:before {
            content: "CLUB";
            font-family: 'Anton', sans-serif;
            position: absolute;
            right: 28px;
            bottom: -36px;
            font-size: 150px;
            color: rgba(255,255,255,0.045);
            letter-spacing: 2px;
            line-height: 1;
        }

        .hero:after {
            content: "";
            position: absolute;
            width: 8px;
            height: 100%;
            background: var(--wine);
            left: 0;
            top: 0;
        }

        .kicker {
            display: inline-block;
            background: var(--wine);
            color: white;
            border: 1px solid rgba(255,255,255,0.28);
            padding: 9px 14px;
            font-weight: 900;
            font-size: 13px;
            letter-spacing: 1.3px;
            text-transform: uppercase;
            margin-bottom: 18px;
        }

        .hero h1 {
            font-family: 'Anton', sans-serif;
            font-size: 78px;
            line-height: 0.95;
            letter-spacing: 1px;
            margin: 0 0 14px 0;
            color: white;
            text-transform: uppercase;
            max-width: 790px;
        }

        .hero h1 span {
            color: var(--wine-soft);
            text-shadow: 3px 3px 0px #ffffff;
        }

        .hero p {
            max-width: 720px;
            font-size: 19px;
            color: rgba(247,241,234,0.86);
            margin: 0;
            font-weight: 500;
        }

        .section-title {
            font-family: 'Anton', sans-serif;
            color: white;
            font-size: 38px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin: 26px 0 14px 0;
        }

        h1, h2, h3, h4 {
            color: white;
        }

        .club-card {
            background: linear-gradient(180deg, rgba(22,22,22,0.98), rgba(10,10,10,0.98));
            border: 1px solid rgba(255,255,255,0.10);
            border-left: 6px solid var(--wine);
            padding: 24px;
            min-height: 155px;
            box-shadow: 0 18px 45px rgba(0,0,0,0.42);
        }

        .club-card h3 {
            font-family: 'Anton', sans-serif;
            font-size: 26px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin: 0 0 8px 0;
            color: white;
        }

        .club-card p {
            color: rgba(247,241,234,0.72);
            font-size: 15px;
            line-height: 1.55;
            margin-bottom: 0;
        }

        .notice {
            background: rgba(139,0,0,0.18);
            border: 1px solid rgba(255,255,255,0.12);
            border-left: 6px solid var(--wine);
            color: var(--offwhite);
            padding: 18px 20px;
            margin: 22px 0;
            font-size: 15px;
            box-shadow: 0 18px 45px rgba(0,0,0,0.30);
        }

        div[data-testid="stForm"] {
            background: rgba(12,12,12,0.96);
            border: 1px solid rgba(255,255,255,0.11);
            border-top: 5px solid var(--wine);
            padding: 30px;
            box-shadow: 0 18px 45px rgba(0,0,0,0.48);
        }

        label, .stMarkdown, p, span {
            color: var(--offwhite);
        }

        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea,
        div[data-baseweb="select"] > div {
            background-color: #111111 !important;
            border: 1px solid rgba(255,255,255,0.16) !important;
            color: white !important;
            border-radius: 0 !important;
        }

        .stSlider [data-baseweb="slider"] {
            filter: saturate(0.8);
        }

        .stButton > button,
        .stDownloadButton > button,
        button[kind="primaryFormSubmit"] {
            background: var(--wine) !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 0 !important;
            padding: 0.78rem 1.35rem !important;
            font-weight: 900 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.8px !important;
            box-shadow: 8px 8px 0px rgba(255,255,255,0.14) !important;
            transition: 0.18s ease !important;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover,
        button[kind="primaryFormSubmit"]:hover {
            background: #ffffff !important;
            color: var(--wine) !important;
            border-color: var(--wine) !important;
            transform: translate(-2px, -2px);
            box-shadow: 10px 10px 0px rgba(139,0,0,0.55) !important;
        }

        div[data-testid="stMetric"] {
            background: #111111;
            border: 1px solid rgba(255,255,255,0.12);
            border-left: 5px solid var(--wine);
            padding: 18px;
            box-shadow: 0 16px 40px rgba(0,0,0,0.38);
        }

        div[data-testid="stMetric"] label {
            color: rgba(247,241,234,0.66) !important;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: white !important;
            font-family: 'Anton', sans-serif;
            letter-spacing: 0.6px;
        }

        .stDataFrame {
            border: 1px solid rgba(255,255,255,0.12);
            box-shadow: 0 18px 45px rgba(0,0,0,0.42);
        }

        .result-box {
            background:
                linear-gradient(135deg, rgba(139,0,0,0.95), rgba(40,0,0,0.95));
            border: 1px solid rgba(255,255,255,0.14);
            padding: 26px;
            margin: 18px 0;
            box-shadow: 0 18px 45px rgba(0,0,0,0.42);
        }

        .result-box h3 {
            font-family: 'Anton', sans-serif;
            font-size: 30px;
            text-transform: uppercase;
            margin-top: 0;
        }

        .result-box p {
            color: rgba(255,255,255,0.84);
            font-size: 16px;
            line-height: 1.6;
        }

        .chat-box {
            background: rgba(12,12,12,0.96);
            border: 1px solid rgba(255,255,255,0.11);
            border-left: 6px solid var(--wine);
            padding: 22px;
            box-shadow: 0 18px 45px rgba(0,0,0,0.42);
            margin-bottom: 14px;
        }

        .footer {
            text-align: center;
            padding: 34px 0 10px 0;
            color: rgba(247,241,234,0.55);
            font-weight: 700;
            letter-spacing: 0.7px;
            text-transform: uppercase;
        }

        .stAlert {
            background-color: rgba(139,0,0,0.18) !important;
            color: white !important;
            border-radius: 0 !important;
        }

        @media (max-width: 900px) {
            .hero h1 {
                font-size: 50px;
            }

            .hero {
                padding: 34px 28px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# FUNÇÕES DO CHATBOT
# ==========================================================

def classificar_nivel(experiencia, minutos_correndo):
    if experiencia == "Nunca corri ou estou parada há muito tempo":
        return "Iniciante total"
    if minutos_correndo < 10:
        return "Iniciante total"
    if minutos_correndo < 25:
        return "Iniciante"
    if minutos_correndo < 45:
        return "Intermediária"
    return "Avançando"

def gerar_treino(objetivo, nivel, semanas, dias_semana, data_inicio):
    linhas = []
    sessoes = ["Treino A", "Treino B", "Treino C", "Treino D", "Treino E"][:dias_semana]

    for semana in range(1, semanas + 1):
        for i, sessao in enumerate(sessoes):
            data_treino = data_inicio + timedelta(days=(semana - 1) * 7 + i * 2)

            if objetivo == "Começar do zero":
                if semana <= 2:
                    principal = "8x: 1 min correndo leve + 2 min caminhando"
                elif semana <= 4:
                    principal = "7x: 2 min correndo leve + 2 min caminhando"
                elif semana <= 6:
                    principal = "6x: 3 min correndo leve + 2 min caminhando"
                else:
                    principal = "20 a 30 min correndo leve, com pausas se necessário"
                foco = "Adaptação à corrida"

            elif objetivo == "Correr 5 km":
                if sessao == "Treino A":
                    principal = f"{20 + semana * 2} min de corrida leve"
                    foco = "Base aeróbica"
                elif sessao == "Treino B":
                    principal = "6x: 2 min moderado + 2 min leve"
                    foco = "Controle de ritmo"
                else:
                    principal = f"{3 + min(semana, 4)} km em ritmo confortável"
                    foco = "Distância progressiva"

            elif objetivo == "Correr 10 km":
                if sessao == "Treino A":
                    principal = f"{30 + semana * 2} min de corrida leve"
                    foco = "Rodagem leve"
                elif sessao == "Treino B":
                    principal = "8x: 2 min moderado + 2 min leve"
                    foco = "Ritmo controlado"
                else:
                    principal = f"{5 + min(semana, 5)} km em ritmo confortável"
                    foco = "Longo progressivo"

            elif objetivo == "Emagrecer correndo":
                if sessao == "Treino A":
                    principal = "30 a 40 min alternando corrida leve e caminhada rápida"
                    foco = "Gasto energético sustentável"
                elif sessao == "Treino B":
                    principal = "10x: 1 min mais forte + 2 min leve"
                    foco = "Intervalado seguro"
                else:
                    principal = "35 a 55 min em ritmo confortável"
                    foco = "Constância e resistência"

            else:
                principal = "30 a 45 min de corrida leve ou caminhada rápida"
                foco = "Melhorar condicionamento"

            if sessao in ["Treino D", "Treino E"]:
                principal = "30 a 45 min de fortalecimento, mobilidade ou caminhada leve"
                foco = "Complementar e prevenção"

            linhas.append({
                "Semana": semana,
                "Data sugerida": data_treino.strftime("%d/%m/%Y"),
                "Sessão": sessao,
                "Foco": foco,
                "Aquecimento": "5 a 10 min caminhando + mobilidade leve",
                "Parte principal": principal,
                "Desaquecimento": "5 min caminhando + alongamento leve",
                "Intensidade": "Leve a moderada, esforço 4 a 7 de 10",
                "Observação": "Termine o treino sentindo que conseguiria fazer um pouco mais."
            })

    return pd.DataFrame(linhas)

def resposta_chat(pergunta):
    p = pergunta.lower()

    if any(x in p for x in ["dor", "joelho", "canela", "tornozelo", "lesão", "lesao"]):
        return "Se a dor for forte, localizada, alterar sua pisada ou piorar durante o treino, pare e procure avaliação profissional. Dor não deve ser ignorada."
    if any(x in p for x in ["ritmo", "pace", "velocidade"]):
        return "No começo, o mais importante não é pace. Corra em ritmo confortável, no qual você ainda consegue conversar."
    if any(x in p for x in ["descanso", "folga", "recuperação", "recuperacao"]):
        return "Descanso faz parte do treino. É nele que o corpo assimila o estímulo e evolui."
    if any(x in p for x in ["emagrecer", "peso", "calorias"]):
        return "A corrida pode ajudar no emagrecimento, mas o resultado depende também de alimentação, sono, treino de força e constância."
    if any(x in p for x in ["menstruação", "menstruacao", "ciclo", "tpm", "cólica", "colica"]):
        return "Em fases de maior cansaço, reduza intensidade sem culpa. A planilha deve se adaptar ao seu corpo."
    if any(x in p for x in ["tênis", "tenis"]):
        return "Use um tênis confortável, que não machuque e que você já tenha testado. Evite estrear tênis novo em treino longo ou prova."

    return "Pense sempre em três pontos: segurança, constância e progressão gradual. A evolução vem da soma de semanas bem feitas."

def club_card(titulo, texto):
    return f"""
    <div class="club-card">
        <h3>{titulo}</h3>
        <p>{texto}</p>
    </div>
    """

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    st.markdown(f'<img class="brand-logo" src="data:image/png;base64,{LOGO_B64}">', unsafe_allow_html=True)
    st.markdown("## CORRE LEVE CLUB")
    st.markdown("Consultoria de corrida para mulheres que querem começar e evoluir com constância.")
    st.markdown("---")
    st.markdown("### O QUE O BOT ENTREGA")
    st.markdown("Planilha inicial")
    st.markdown("Ajuste por objetivo")
    st.markdown("Nível estimado")
    st.markdown("Orientação de segurança")
    st.markdown("Chat de dúvidas rápidas")
    st.markdown("---")
    st.markdown("### INSTAGRAM")
    st.markdown("@ocorreleve")

# ==========================================================
# HERO
# ==========================================================

st.markdown(
    f"""
    <div class="hero">
        <span class="kicker">Corre Leve Club • Consultoria de Corrida</span>
        <h1>Corra forte.<br><span>Comece leve.</span></h1>
        <p>
            Um chatbot para montar planilhas de corrida para mulheres, com estética de club,
            orientação simples e evolução progressiva.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(club_card("01. Começo real", "Planos para quem está saindo do zero, voltando aos treinos ou buscando constância."), unsafe_allow_html=True)
with c2:
    st.markdown(club_card("02. Sem pressão", "A planilha respeita nível, rotina e descanso. O foco é fazer a corrida caber na vida."), unsafe_allow_html=True)
with c3:
    st.markdown(club_card("03. Evolução club", "Objetivos como 5 km, 10 km, condicionamento e emagrecimento com progressão gradual."), unsafe_allow_html=True)

st.markdown(
    """
    <div class="notice">
        <strong>AVISO:</strong> este chatbot não substitui avaliação médica, fisioterapêutica ou acompanhamento profissional.
        Se houver dor no peito, tontura, falta de ar anormal, lesão recente, gravidez, pós-parto recente ou condição médica,
        procure liberação profissional antes de iniciar.
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# FORMULÁRIO
# ==========================================================

st.markdown('<div class="section-title">Monte sua planilha</div>', unsafe_allow_html=True)

with st.form("formulario"):
    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome", placeholder="Exemplo: Ana")
        idade = st.number_input("Idade", min_value=12, max_value=90, value=25)
        objetivo = st.selectbox(
            "Objetivo principal",
            ["Começar do zero", "Correr 5 km", "Correr 10 km", "Emagrecer correndo", "Melhorar condicionamento"]
        )
        semanas = st.selectbox("Quantidade de semanas da planilha", [4, 6, 8, 10, 12], index=2)
        dias_semana = st.selectbox("Dias de treino por semana", [2, 3, 4, 5], index=1)
        data_inicio = st.date_input("Data de início", value=date.today())

    with col2:
        experiencia = st.selectbox(
            "Experiência atual",
            [
                "Nunca corri ou estou parada há muito tempo",
                "Caminho com frequência, mas corro pouco",
                "Já corro às vezes",
                "Corro com regularidade"
            ]
        )

        minutos_correndo = st.slider(
            "Hoje, por quantos minutos você consegue correr sem parar em ritmo leve?",
            min_value=0,
            max_value=90,
            value=5,
            step=5
        )

        dor_peito = st.radio("Sente dor no peito ao fazer esforço?", ["Não", "Sim"], horizontal=True)
        tontura = st.radio("Sente tontura ou já desmaiou durante esforço?", ["Não", "Sim"], horizontal=True)
        lesao = st.radio("Teve alguma lesão recente?", ["Não", "Sim"], horizontal=True)

    gerar = st.form_submit_button("Gerar planilha")

# ==========================================================
# RESULTADO
# ==========================================================

if gerar:
    nivel = classificar_nivel(experiencia, minutos_correndo)

    st.markdown('<div class="section-title">Resultado da consultoria</div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Nível", nivel)
    m2.metric("Objetivo", objetivo)
    m3.metric("Semanas", semanas)
    m4.metric("Treinos", f"{dias_semana}/semana")

    if dor_peito == "Sim" or tontura == "Sim" or lesao == "Sim":
        st.warning("Existe pelo menos um ponto de atenção. Use a planilha apenas como referência leve e procure liberação profissional antes de iniciar.")

    st.markdown(
        f"""
        <div class="result-box">
            <h3>{nome or "Sua planilha"}</h3>
            <p>
                Seu plano foi montado com foco em <strong>{objetivo}</strong>.
                A ideia é evoluir com constância, sem transformar todo treino em prova.
                Corra leve na maior parte dos dias e respeite os descansos.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    plano = gerar_treino(objetivo, nivel, semanas, dias_semana, data_inicio)
    st.dataframe(plano, use_container_width=True, hide_index=True)

    csv = plano.to_csv(index=False, sep=";").encode("utf-8-sig")
    st.download_button(
        "Baixar planilha em CSV",
        data=csv,
        file_name="planilha_corre_leve_club.csv",
        mime="text/csv"
    )

# ==========================================================
# CHAT RÁPIDO
# ==========================================================

st.markdown('<div class="section-title">Chat rápido Corre Leve</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="chat-box">
        Pergunte sobre dor, joelho, pace, descanso, emagrecimento, ciclo menstrual, tênis ou evolução.
    </div>
    """,
    unsafe_allow_html=True
)

pergunta = st.text_input("Digite sua dúvida")

if pergunta:
    st.success(resposta_chat(pergunta))

st.markdown('<div class="footer">Corre Leve Club • Correr com leveza também é evoluir</div>', unsafe_allow_html=True)

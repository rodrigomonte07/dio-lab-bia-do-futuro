import streamlit as st

from src.carregador_dados import carregar_dados
from agente import gerar_resposta

st.set_page_config(
    page_title="FinGuardian AI",
    page_icon="💰",
    layout="wide"
)

(
    transacoes,
    historico,
    perfil,
    produtos
) = carregar_dados()

st.title("🤖 FinGuardian AI")

sidebar = st.sidebar

sidebar.header("Cliente")

sidebar.write(
    f"Nome: {perfil['nome']}"
)

sidebar.write(
    f"Perfil: {perfil['perfil_investidor']}"
)

sidebar.write(
    f"Objetivo: {perfil['objetivo_principal']}"
)

st.subheader(
    "📊 Resumo Financeiro"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Renda Mensal",
    f"R$ {perfil['renda_mensal']:,.2f}"
)

col2.metric(
    "Patrimônio",
    f"R$ {perfil['patrimonio_total']:,.2f}"
)

col3.metric(
    "Reserva Atual",
    f"R$ {perfil['reserva_emergencia_atual']:,.2f}"
)

st.subheader(
    "💡 Insights Proativos"
)

meta = perfil["metas"][0]["valor_necessario"]

reserva = perfil[
    "reserva_emergencia_atual"
]

faltam = meta - reserva

st.info(
    f"""
Sua reserva atual é de
R$ {reserva:,.2f}

Sua meta é
R$ {meta:,.2f}

Faltam
R$ {faltam:,.2f}
para concluir a meta.
"""
)

st.subheader(
    "💬 Converse com o FinGuardian AI"
)

pergunta = st.text_input(
    "Digite sua pergunta"
)

if st.button("Enviar"):

    resposta = gerar_resposta(
        pergunta,
        perfil,
        produtos,
        transacoes,
        historico
    )

    if "quota" in resposta.lower() or "configurada" in resposta.lower():
        st.error(resposta)
    else:
        st.write(resposta)

st.divider()

st.subheader(
    "⚡ Perguntas Frequentes"
)

if st.button(
    "Qual investimento combina comigo?"
):

    resposta = gerar_resposta(
        "Qual investimento combina comigo?",
        perfil,
        produtos,
        transacoes,
        historico
    )

    if "quota" in resposta.lower() or "configurada" in resposta.lower():
        st.error(resposta)
    else:
        st.write(resposta)

if st.button(
    "Como completar minha reserva?"
):

    resposta = gerar_resposta(
        "Como completar minha reserva de emergência?",
        perfil,
        produtos,
        transacoes,
        historico
    )

    if "quota" in resposta.lower() or "configurada" in resposta.lower():
        st.error(resposta)
    else:
        st.write(resposta)

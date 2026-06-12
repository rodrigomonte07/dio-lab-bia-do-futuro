import streamlit as st

from carregador_dados import carregar_dados
from agente import gerar_resposta

st.set_page_config(
    page_title="FinGuardian AI",
    page_icon="💰"
)

st.title("🤖 FinGuardian AI")

transacoes, historico, perfil, produtos = carregar_dados()

with st.sidebar:

    st.header("Cliente")

    st.write(f"Nome: {perfil['nome']}")
    st.write(f"Perfil: {perfil['perfil_investidor']}")
    st.write(f"Renda: R$ {perfil['renda_mensal']}")
    st.write(f"Objetivo: {perfil['objetivo_principal']}")

st.subheader("Faça sua pergunta")

pergunta = st.text_input(
    "Digite uma pergunta"
)

if st.button("Enviar"):

    resposta = gerar_resposta(
        perfil,
        produtos,
        pergunta
    )

    st.markdown("### Resposta")

    st.write(resposta)

st.divider()

st.subheader("Sugestões")

if st.button("Qual investimento combina comigo?"):
    resposta = gerar_resposta(
        perfil,
        produtos,
        "Qual investimento combina comigo?"
    )
    st.write(resposta)

if st.button("Como completar minha reserva de emergência?"):
    resposta = gerar_resposta(
        perfil,
        produtos,
        "Como completar minha reserva de emergência?"
    )
    st.write(resposta)

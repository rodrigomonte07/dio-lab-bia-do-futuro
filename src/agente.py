from openai import OpenAI
from openai import RateLimitError

from src.config import OPENAI_API_KEY
from src.prompts import SYSTEM_PROMPT


def criar_cliente():
    if not OPENAI_API_KEY:
        return None

    return OpenAI(api_key=OPENAI_API_KEY)

def montar_contexto(
    perfil,
    produtos,
    transacoes,
    historico
):

    return f"""
CLIENTE

Nome: {perfil['nome']}
Idade: {perfil['idade']}
Profissão: {perfil['profissao']}
Perfil: {perfil['perfil_investidor']}
Objetivo: {perfil['objetivo_principal']}
Renda Mensal: R$ {perfil['renda_mensal']}
Patrimônio Total: R$ {perfil['patrimonio_total']}
Reserva Atual: R$ {perfil['reserva_emergencia_atual']}

METAS

{perfil['metas']}

PRODUTOS DISPONÍVEIS

{produtos}

TRANSAÇÕES

{transacoes.to_string()}

ATENDIMENTOS

{historico.to_string()}
"""

def gerar_resposta(
    pergunta,
    perfil,
    produtos,
    transacoes,
    historico
):

    contexto = montar_contexto(
        perfil,
        produtos,
        transacoes,
        historico
    )

    client = criar_cliente()

    if client is None:
        return "Chave da OpenAI não configurada. Defina OPENAI_API_KEY no arquivo .env para usar o agente."

    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content":
                        contexto +
                        "\n\nPergunta:\n" +
                        pergunta
                }
            ]
        )
    except RateLimitError:
        return "A API da OpenAI não está disponível no momento porque a quota foi excedida. Verifique seu plano e billing da conta."

    return resposta.choices[0].message.content

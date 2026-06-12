from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def gerar_resposta(perfil, produtos, pergunta):

    contexto = f"""
    Dados do Cliente:

    Nome: {perfil['nome']}
    Perfil: {perfil['perfil_investidor']}
    Objetivo: {perfil['objetivo_principal']}
    Renda: R$ {perfil['renda_mensal']}
    Patrimônio: R$ {perfil['patrimonio_total']}

    Produtos Disponíveis:

    {produtos}
    """

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content": contexto + "\n\nPergunta:\n" + pergunta
            }
        ]
    )

    return resposta.choices[0].message.content

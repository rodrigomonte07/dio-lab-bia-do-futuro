import pandas as pd
import json

def carregar_dados():
    
    transacoes = pd.read_csv("../data/transacoes.csv")

    historico = pd.read_csv("../data/historico_atendimento.csv")

    with open("../data/perfil_investidor.json", encoding="utf-8") as arquivo:
        perfil = json.load(arquivo)

    with open("../data/produtos_financeiros.json", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

    return transacoes, historico, perfil, produtos

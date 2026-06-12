import json
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def carregar_dados():

    transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")

    historico = pd.read_csv(DATA_DIR / "historico_atendimento.csv")

    with open(
        DATA_DIR / "perfil_investidor.json",
        encoding="utf-8"
    ) as arquivo:

        perfil = json.load(arquivo)

    with open(
        DATA_DIR / "produtos_financeiros.json",
        encoding="utf-8"
    ) as arquivo:

        produtos = json.load(arquivo)

    return (
        transacoes,
        historico,
        perfil,
        produtos
    )

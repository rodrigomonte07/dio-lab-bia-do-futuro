# Base de Conhecimento

## Dados Utilizados

| Arquivo                   | Formato | Utilização no Agente                             |
| ------------------------- | ------- | ------------------------------------------------ |
| historico_atendimento.csv | CSV     | Recuperar contexto de atendimentos anteriores    |
| perfil_investidor.json    | JSON    | Personalizar recomendações financeiras           |
| produtos_financeiros.json | JSON    | Identificar produtos compatíveis com o perfil    |
| transacoes.csv            | CSV     | Analisar receitas, despesas e padrões de consumo |

---

## Adaptações nos Dados

Os dados mockados foram mantidos como base principal do projeto.

Foram adicionadas regras de interpretação para:

* Classificação de gastos por categoria
* Identificação de gastos recorrentes
* Sugestões de economia com base no comportamento financeiro
* Compatibilização automática entre perfil de investidor e produtos financeiros

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos CSV e JSON são carregados no início da aplicação utilizando Python e Pandas.

Os dados permanecem disponíveis durante toda a sessão para consultas do agente.

### Como os dados são usados no prompt?

Os dados são consultados dinamicamente antes da geração da resposta.

O sistema monta um contexto contendo:

* Perfil do cliente
* Objetivos financeiros
* Histórico de transações
* Histórico de atendimentos
* Produtos financeiros disponíveis

Esse contexto é enviado junto ao prompt para que o modelo responda apenas com informações verificadas.

---

## Exemplo de Contexto Montado

Dados do Cliente:

* Nome: João Silva
* Idade: 32 anos
* Profissão: Analista de Sistemas
* Perfil: Moderado
* Renda Mensal: R$ 5.000
* Patrimônio Atual: R$ 15.000
* Objetivo Principal: Construir reserva de emergência

Metas:

* Completar reserva de emergência (R$ 15.000)
* Entrada de apartamento (R$ 50.000)

Últimas transações:

* Aluguel: R$ 1.200
* Supermercado: R$ 450
* Netflix: R$ 55,90
* Restaurante: R$ 120
* Uber: R$ 45
* Conta de Luz: R$ 180
* Academia: R$ 99
* Combustível: R$ 250

Produtos Financeiros Compatíveis:

* Tesouro Selic
* CDB Liquidez Diária
* Fundo Multimercado

Exemplo de Insight Gerado:

"Você possui perfil moderado e ainda está construindo sua reserva de emergência. Com base nisso, o Tesouro Selic e o CDB Liquidez Diária são as alternativas mais adequadas para seus objetivos atuais."


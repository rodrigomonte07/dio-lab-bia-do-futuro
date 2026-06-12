# 🤖 FinGuardian AI

FinGuardian AI é um agente financeiro inteligente desenvolvido para auxiliar clientes na organização financeira, construção de metas e escolha de investimentos compatíveis com seu perfil.

## Funcionalidades

- Consulta de perfil financeiro
- Análise de gastos
- Recomendações personalizadas
- Sugestões para metas financeiras
- Segurança contra alucinações

## Tecnologias

- Python
- Streamlit
- OpenAI API
- Pandas

## Como executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Configurar chave da API

Criar arquivo `.env`

```env
OPENAI_API_KEY=sua_chave_aqui
```

### Executar

```bash
streamlit run app.py
```

## Caso de Uso

Cliente João Silva:

- Perfil Moderado
- Renda: R$ 5.000
- Patrimônio: R$ 15.000
- Objetivo: Reserva de Emergência

O agente utiliza essas informações para gerar respostas personalizadas.

## Segurança

O sistema responde apenas com base nos dados fornecidos na base de conhecimento.

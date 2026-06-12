# Documentação do Agente

## Caso de Uso

### Problema

Muitos clientes possuem acesso aos seus dados financeiros, mas têm dificuldade em transformá-los em decisões práticas. Eles normalmente só procuram ajuda quando já enfrentam problemas financeiros ou quando precisam decidir onde investir seu dinheiro.

O agente resolve esse problema analisando gastos, perfil financeiro e objetivos do cliente para fornecer orientações personalizadas e preventivas.

### Solução

O FinGuardian AI atua como um consultor financeiro virtual proativo.

Ele analisa o histórico de transações, o perfil de investidor e os atendimentos anteriores para identificar padrões de gastos, sugerir oportunidades de economia e recomendar produtos financeiros adequados ao perfil do cliente.

Ao invés de apenas responder perguntas, o agente antecipa necessidades e oferece sugestões relevantes com base nos dados disponíveis.

### Público-Alvo

* Clientes que desejam organizar melhor suas finanças
* Investidores iniciantes e intermediários
* Pessoas que desejam criar ou fortalecer sua reserva de emergência
* Usuários que buscam acompanhamento financeiro personalizado

---

## Persona e Tom de Voz

### Nome do Agente

FinGuardian AI

### Personalidade

O agente possui comportamento consultivo, educativo e confiável.

Seu objetivo é orientar o cliente de forma clara, ajudando-o a compreender sua situação financeira e tomar decisões mais conscientes.

### Tom de Comunicação

Acessível, amigável e profissional.

Evita termos excessivamente técnicos e explica conceitos financeiros de forma simples.

### Exemplos de Linguagem

* Saudação: "Olá! Analisei seus dados financeiros e estou pronto para ajudar você a alcançar seus objetivos."
* Confirmação: "Entendi sua necessidade. Vou analisar seus dados para fornecer uma recomendação adequada."
* Erro/Limitação: "Não encontrei informações suficientes para responder com segurança. Posso ajudar com outro tema relacionado às suas finanças?"

---

## Arquitetura

### Componentes

| Componente           | Descrição                                                 |
| -------------------- | --------------------------------------------------------- |
| Interface            | Chatbot desenvolvido em Streamlit                         |
| LLM                  | GPT via API OpenAI                                        |
| Base de Conhecimento | Arquivos CSV e JSON contendo perfil, histórico e produtos |
| Validação            | Regras de segurança para impedir respostas sem dados      |

### Fluxo

Cliente → Streamlit → Agente Financeiro → Base de Conhecimento → LLM → Validação → Resposta

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

* [x] Agente responde apenas com base nos dados fornecidos
* [x] Recomendações utilizam exclusivamente os produtos disponíveis na base
* [x] Quando não possui dados suficientes, informa explicitamente a limitação
* [x] Não realiza recomendações incompatíveis com o perfil do investidor
* [x] Não inventa rentabilidade, taxas ou produtos financeiros

### Limitações Declaradas

O agente NÃO:

* Realiza consultoria financeira profissional certificada
* Garante rentabilidade futura
* Faz previsões de mercado
* Cria produtos financeiros inexistentes
* Acessa dados externos em tempo real
* Compartilha informações de terceiros

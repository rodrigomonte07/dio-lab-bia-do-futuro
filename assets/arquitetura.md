flowchart TD
    A[Cliente] -->|Pergunta| B[Streamlit]
    B --> C[FinGuardian AI]
    C --> D[Perfil Investidor]
    C --> E[Transações]
    C --> F[Produtos Financeiros]
    C --> G[Histórico Atendimento]
    D --> H[LLM]
    E --> H
    F --> H
    G --> H
    H --> I[Resposta Segura]
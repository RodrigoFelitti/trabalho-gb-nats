# Trabalho GB — NATS Core vs JetStream

Comparação empírica entre os dois modos de operação do NATS em cenário de telemetria IoT simulada. Continuação do trabalho do GA, agora com implementação e coleta de métricas.

**Grupo:** Rodrigo D'Ávila, Pedro Engel, Ramiro Manoel
**Disciplina:** Sistemas Distribuídos — UNISINOS

## Estrutura

```
.
├── app/           # Aplicação de referência (compartilhada entre Core e JetStream)
├── core/          # Pessoa 1 — ambiente e testes do NATS Core
├── jetstream/     # Pessoa 2 — ambiente e testes do NATS JetStream
├── analysis/      # Pessoa 3 — gráficos, tabelas e análise comparativa
├── artigo/        # Artigo em LaTeX (modelo SBC)
└── CONTRATO.md    # Combinados do grupo (CSV, cenários, parâmetros) — LER ANTES
```

## Divisão

| Pessoa | Responsabilidade | Pastas |
|--------|------------------|--------|
| 1 — Rodrigo? | NATS Core + resultados do Core | `core/` + partes de `app/` |
| 2 — Pedro? | NATS JetStream + resultados do JetStream | `jetstream/` + partes de `app/` |
| 3 — Ramiro? | Análise comparativa, artigo, slides | `analysis/`, `artigo/` |

*(ajustar nomes conforme combinarmos)*

## Como começar

1. Ler o `CONTRATO.md` — define o formato CSV, os cenários e os parâmetros que todos usam.
2. Cada um vai para a sua pasta, há um README lá dentro com o passo a passo.
3. Resultados vão para `core/results/` e `jetstream/results/` em formato CSV.
4. A Pessoa 3 consome os CSVs em `analysis/` e gera os gráficos em `analysis/output/`.

## Prazos

- Apresentação na aula 16, antes da prova do GB
- Parte escrita entregue até a prova do GB

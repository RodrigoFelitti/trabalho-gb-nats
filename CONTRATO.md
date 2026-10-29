# Contrato do grupo

Combinados para que as três partes do trabalho sejam compatíveis entre si. **Qualquer mudança aqui precisa de alinhamento dos três.**

## 1. Linguagem e bibliotecas

- Python 3.10+
- Cliente NATS: `nats-py`
- Análise: `pandas`, `matplotlib`

## 2. Infraestrutura

- Docker + Docker Compose
- Imagem oficial `nats:latest`
- Tudo roda localmente no notebook (sem cloud)

## 3. Aplicação de referência (telemetria IoT simulada)

- **Publishers** (sensores): publicam em `sensores.<id>.leitura` com payload JSON `{"id": "...", "valor": float, "timestamp": "..."}`
- **Subscribers**: assinam `sensores.>` e processam
- **Serviço de alerta**: assina um subject de requisição e responde via request/reply quando o valor passa de um limite

## 4. Formato CSV de saída (OBRIGATÓRIO — mesmo nos dois lados)

Nome do arquivo: `resultados_<modo>_<cenario>.csv` (ex: `resultados_core_vazao.csv`)

Colunas:

```
cenario,modo,tamanho_msg,n_publishers,n_subscribers,latencia_ms,msg_enviadas,msg_recebidas,duracao_s
```

- `cenario`: `vazao` | `escalabilidade` | `resiliencia` | `replicacao` (apenas JetStream)
- `modo`: `core` | `jetstream`
- `tamanho_msg`: tamanho do payload em bytes
- `n_publishers`: número de publishers simulados
- `n_subscribers`: número de subscribers (em queue group quando aplicável)
- `latencia_ms`: latência de uma mensagem individual (uma linha por mensagem, ou agregada — definir)
- `msg_enviadas`, `msg_recebidas`: contadores
- `duracao_s`: duração da rodada em segundos

**Uma linha por medição.** A Pessoa 3 agrega (p50, p95, p99) depois.

## 5. Cenários-base (os dois rodam exatamente os mesmos)

### Cenário 1 — Vazão e latência por tamanho de mensagem
- 1 publisher, 1 subscriber
- Taxa fixa: 1000 msg/s por 60 segundos
- Tamanhos: 100 B, 1 KB, 10 KB
- Medir: latência fim-a-fim de cada mensagem, vazão real

### Cenário 2 — Escalabilidade com queue group
- Tamanho fixo: 1 KB
- Taxa fixa por publisher: 500 msg/s por 60 segundos
- N publishers: 1, 10, 50
- 3 subscribers em queue group
- Medir: vazão agregada, latência média

### Cenário 3 — Resiliência (queda do consumidor)
- 1 publisher a 500 msg/s por 60 segundos
- 1 subscriber que é derrubado nos segundos 20–50 e retorna
- Medir: `msg_enviadas` vs `msg_recebidas` (esperado Core: perda grande; JetStream: zero)

### Cenário extra — Replicação (SÓ JetStream)
- Repetir Cenário 1 com fator de replicação R=1 e R=3
- Medir: diferença de latência

## 6. Ambiente de execução (para reportar no artigo)

Cada um reporta no seu README:
- SO e versão
- CPU e RAM
- Versão do Docker
- Qualquer coisa relevante (notebook ou desktop, carregado na tomada, etc)

Isso evita viés nos resultados por rodarem em máquinas muito diferentes.

## 7. Convenção de commits

- `feat:` nova funcionalidade
- `fix:` correção
- `docs:` documentação/artigo
- `test:` ajustes em cenários de teste
- `data:` CSVs ou outputs de resultados

Exemplo: `feat(core): adiciona cenario de resiliencia`

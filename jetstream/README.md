# NATS JetStream — Pessoa 2

Ambiente, orquestração e coleta de resultados do modo JetStream do NATS, incluindo cluster de 3 nós para teste de replicação.

## Responsabilidades

- Subir cluster de 3 nós NATS com JetStream habilitado via Docker Compose
- Configurar stream e consumer
- Executar os 3 cenários-base + cenário extra de replicação
- Exportar CSVs em `results/` no formato combinado
- Escrever as seções 4.2, 5.2 e 5.3 do artigo

## Como rodar

```bash
# 1. Subir o cluster
docker compose up -d

# 2. Verificar que os 3 nós estão no ar e formaram cluster
docker compose logs | grep -i "cluster\|routes"

# 3. Instalar dependências
pip install -r ../app/requirements.txt

# 4. Criar o stream (uma vez, antes dos testes)
python setup_streams.py

# 5. Rodar os cenários
python run_scenarios.py --cenario vazao
python run_scenarios.py --cenario escalabilidade
python run_scenarios.py --cenario resiliencia
python run_scenarios.py --cenario replicacao  # extra, só JetStream

# 6. Derrubar o cluster
docker compose down -v  # -v apaga volumes de dados
```

## Ambiente de execução

**Preencher ao final para reportar no artigo:**

- SO:
- CPU:
- RAM:
- Versão Docker:
- Observações:

## Resultados esperados

- `results/resultados_jetstream_vazao.csv`
- `results/resultados_jetstream_escalabilidade.csv`
- `results/resultados_jetstream_resiliencia.csv`
- `results/resultados_jetstream_replicacao.csv`

**No cenário de resiliência:** esperado **zero perda** de mensagens quando o consumer é derrubado (comportamento at-least-once do JetStream — contraste direto com o Core).

**No cenário de replicação:** esperado aumento de latência em R=3 vs R=1 por conta do consenso RAFT entre as réplicas.

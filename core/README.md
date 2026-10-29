# NATS Core — Pessoa 1

Ambiente, orquestração e coleta de resultados do modo Core do NATS.

## Responsabilidades

- Subir um `nats-server` single-node via Docker Compose
- Executar os 3 cenários-base definidos no `CONTRATO.md`
- Exportar CSVs em `results/` no formato combinado
- Escrever as seções 3 (compartilhada), 4.1 e 5.1 do artigo

## Como rodar

```bash
# 1. Subir o NATS
docker compose up -d

# 2. Verificar que está no ar
docker compose logs nats

# 3. Instalar dependências Python
pip install -r ../app/requirements.txt

# 4. Rodar os cenários (gera CSVs em results/)
python run_scenarios.py --cenario vazao
python run_scenarios.py --cenario escalabilidade
python run_scenarios.py --cenario resiliencia

# 5. Derrubar o NATS
docker compose down
```

## Ambiente de execução

**Preencher ao final para reportar no artigo:**

- SO:
- CPU:
- RAM:
- Versão Docker:
- Observações:

## Resultados esperados

- `results/resultados_core_vazao.csv`
- `results/resultados_core_escalabilidade.csv`
- `results/resultados_core_resiliencia.csv`

**No cenário de resiliência:** esperado perda significativa de mensagens quando o consumer é derrubado por 30s (comportamento at-most-once documentado na seção 3.5 do artigo do GA).

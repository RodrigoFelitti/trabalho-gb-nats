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

- SO: Omarchy (baseado em Arch Linux), kernel 7.2.5
- CPU: Intel Core i7-8700 @ 3.20GHz (6 núcleos / 12 threads)
- RAM: 16 GB
- Versão Docker: 29.7.2
- Observações:
  - Desktop (sem bateria, sempre na tomada)
  - NATS Server 2.15.2 (imagem `nats:latest` no momento dos testes)
  - Python 3.14.7, nats-py 2.16.0
  - Sensores e consumers rodam no mesmo processo Python (asyncio), na mesma máquina do servidor; a latência usa o mesmo relógio dos dois lados

## Resultados esperados

- `results/resultados_core_vazao.csv.gz`
- `results/resultados_core_escalabilidade.csv.gz`
- `results/resultados_core_resiliencia.csv.gz`

**No cenário de resiliência:** esperado perda significativa de mensagens quando o consumer é derrubado por 30s (comportamento at-most-once documentado na seção 3.5 do artigo do GA).

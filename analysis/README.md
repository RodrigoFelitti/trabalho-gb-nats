# Análise — Pessoa 3

Consome os CSVs gerados pelas Pessoas 1 e 2, gera gráficos comparativos e a tabela resumo. Também responsável pela escrita das seções 1, 2, 6, 7 e 8 do artigo e dos slides de abertura/fechamento.

## Responsabilidades

**Pode começar antes dos CSVs chegarem:**
- Montar o Overleaf no modelo SBC (`../artigo/`)
- Escrever Introdução, Metodologia e Limitações
- Preparar os scripts de análise (abaixo)

**Depende dos CSVs das Pessoas 1 e 2:**
- Rodar `plots.py` para gerar os gráficos comparativos
- Rodar `summary_table.py` para gerar a tabela resumo
- Escrever a Discussão Comparativa (seção 6)
- Escrever a Conclusão

## Como rodar (depois que os CSVs chegarem)

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Verificar que os CSVs estão nos lugares esperados
ls ../core/results/
ls ../jetstream/results/

# 3. Gerar gráficos (saem em output/)
python plots.py

# 4. Gerar tabela resumo (sai em output/tabela_resumo.tex)
python summary_table.py
```

## Gráficos a gerar

- `output/latencia_comparacao.png` — latência p50/p99 Core vs JetStream por tamanho de msg
- `output/vazao_comparacao.png` — vazão Core vs JetStream por nº publishers
- `output/resiliencia.png` — enviadas vs recebidas no teste de queda (barras lado a lado)
- `output/replicacao.png` — latência JetStream R=1 vs R=3

## Análise comparativa — foco

A seção de Discussão é a mais importante do artigo. Para cada afirmação qualitativa do GA, confrontar com os números medidos:

1. "Core prioriza latência" → por quanto Core é mais rápido que JetStream?
2. "JetStream cobra parte da simplicidade" → quanto a mais custa em latência? E em overhead de setup?
3. "Perda aceitável em telemetria no Core" → qual foi a taxa de perda no cenário de resiliência?
4. "Consenso RAFT tem custo" → quanto R=3 adiciona de latência sobre R=1?

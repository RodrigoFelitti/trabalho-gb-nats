# Artigo (LaTeX — modelo SBC)

Esqueleto do artigo do GB. Pode ser compilado localmente ou subido no Overleaf.

## Arquivos

- `artigo_gb.tex` — esqueleto com as 8 seções estruturadas

## Para usar no Overleaf

1. Criar novo projeto em branco no Overleaf (plano free basta)
2. Fazer upload de:
   - `artigo_gb.tex`
   - `sbc-template.sty` (reaproveitar do GA)
   - `sbc.bst` (reaproveitar do GA)
   - `references.bib` (reaproveitar do GA, adicionar novas refs conforme necessário)
3. Compilar com pdfLaTeX

## Figuras

Quando gerarem gráficos em `../analysis/output/`, copiar os `.png` para uma pasta `figures/` aqui e referenciar no `.tex` com `\includegraphics{figures/nome.png}`.

## Responsáveis por seção

| Seção | Responsável |
|-------|-------------|
| Resumo | Pessoa 3 (ao final) |
| 1. Introdução | Pessoa 3 |
| 2. Metodologia | Pessoa 3 |
| 3. Arquitetura do Protótipo | Pessoas 1 e 2 |
| 4.1 Configuração Core | Pessoa 1 |
| 4.2 Configuração JetStream | Pessoa 2 |
| 5.1 Resultados Core | Pessoa 1 |
| 5.2 Resultados JetStream | Pessoa 2 |
| 5.3 Overhead Operacional | Pessoa 2 |
| 6. Discussão Comparativa | Pessoa 3 |
| 7. Limitações | Pessoa 3 |
| 8. Conclusão | Pessoa 3 |

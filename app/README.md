# Aplicação de referência

Código Python compartilhado pelas Pessoas 1 e 2. A mesma lógica roda contra NATS Core e contra JetStream — o que muda é só a configuração da conexão e, no caso do JetStream, o uso de stream/consumer.

## Arquivos

- `sensor.py` — publisher que simula um sensor publicando leituras em `sensores.<id>.leitura`
- `consumer.py` — subscriber que assina `sensores.>` e processa as mensagens
- `alert_service.py` — serviço de alerta que responde via request/reply quando o valor passa de um limite
- `config.py` — constantes compartilhadas (nomes de subjects, limites, etc)

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

Cada script aceita argumentos de linha de comando. Ver o `--help` de cada um ou os runners nas pastas `core/` e `jetstream/`.

"""Configurações compartilhadas entre todos os componentes."""

# Subjects (ver seção 3.2 do artigo do GA)
SUBJECT_SENSOR = "sensores.{sensor_id}.leitura"
SUBJECT_SENSOR_WILDCARD = "sensores.>"
SUBJECT_ALERTA_REQUEST = "alertas.verificar"

# Nome do stream JetStream (usado só pela Pessoa 2)
STREAM_NAME = "SENSORES"
CONSUMER_NAME = "processador"

# Limites de alerta
LIMITE_ALERTA = 80.0

# Endereços
NATS_URL_LOCAL = "nats://localhost:4222"
NATS_URL_CLUSTER = "nats://localhost:4222,nats://localhost:4223,nats://localhost:4224"

import json
import time

from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

consumer = None

while consumer is None:

    try:

        consumer = KafkaConsumer(
            "support-tickets",

            bootstrap_servers="localhost:29092",

            auto_offset_reset="earliest",

            enable_auto_commit=True,

            group_id="debug-group",

            consumer_timeout_ms=1000,

            value_deserializer=lambda m:
            json.loads(m.decode("utf-8"))
        )

        print("connected to kafka..")

    except NoBrokersAvailable:

        print("kafka not ready.. retrying")

        time.sleep(5)

print("Connected To Kafka Consumer")


while True:

    for message in consumer:

        print("received ticket :")

        print(message.value)
        
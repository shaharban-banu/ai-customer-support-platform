import json
import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

def send_ticket(data):

    try:

        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",

            value_serializer=lambda value:
            json.dumps(value).encode("utf-8")
        )

        producer.send(
            "support-tickets",
            value=data
        )

        producer.flush()

        print("message send to kafka..")

    except NoBrokersAvailable:

        print("Kafka unavailable")
        time.sleep(5)


# def get_producer():

#     producer = KafkaProducer(
#         bootstrap_servers="kafka:9092",
#         value_serializer=lambda value:json.dumps(value).encode("utf-8"))

#     return producer
# #print("producer running..")

# def send_ticket(data):
#     producer=get_producer()
#     producer.send("support-tickets",value=data)
#     producer.flush()
#     print("message send to kafka..")

#import time

# producer=None
# while producer is None:
#     try:
#         producer=KafkaProducer(bootstrap_servers="kafka:9092",
#                             value_serializer=lambda v:json.dumps(v).encode('utf-8'))
#         print("connected to kafka..")
#     except Exception as e:
#         print("kafka not ready.. retrying")
#         time.sleep(5)

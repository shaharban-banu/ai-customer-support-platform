import json
from kafka import KafkaProducer

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

    except Exception as error:

        print("Kafka unavailable")

        print(error)

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

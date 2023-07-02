from kafka import KafkaConsumer
import json
import time
from pykafka import KafkaClient

time.sleep(35) 

print("Ready to consume")
client = KafkaClient(hosts="kafka:29092")
client.topics
topic = client.topics['test']
consumer = topic.get_simple_consumer(
        auto_commit_enable=False,
        auto_commit_interval_ms=100, 
        consumer_group='test_group', 
        fetch_wait_max_ms=100
        #auto_offset_reset='erliest',
        #reset_offset_on_start=False
    )
for message in consumer:
    if message is not None:
        print(message.value)

    
# consumer = KafkaConsumer('test',bootstrap_servers='kafka:29092', auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
# print("got consumer")
# consumer.subscribe(['test'])
# print("subscribing")
# for msg in consumer:
#     print("New topic:")
#     try:
#         print(msg)
#     except:
#         pass
        
    
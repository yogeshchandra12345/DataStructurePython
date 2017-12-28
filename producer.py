from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    print('before')
    producer.send('test', b'some_message_bytes')
    print('after')

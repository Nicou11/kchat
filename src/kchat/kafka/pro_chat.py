from kafka import KafkaProducer
import time
from json import dumps

p = KafkaProducer

producer = p(
        bootstrap_servers=['ec2-43-201-83-4.ap-northeast-2.compute.amazonaws.com:9092'],
        value_serializer=lambda x:dumps(x).encode('utf-8')
)

print("채팅 프로그램 - 메시지 발신자")
print("메시지를 입력하세요. (종료시 'exit' 입력)")

while True:
    msg = input("YOU: ")
    data = {"message": msg, 'time': time.ctime()}
    producer.send('chat', value=data)
    producer.flush()
    if msg.lower() == 'exit':
        break
print("채팅 종료")


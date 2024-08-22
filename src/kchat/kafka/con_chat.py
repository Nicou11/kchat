from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        'chat',
        bootstrap_servers=['ec2-43-201-83-4.ap-northeast-2.compute.amazonaws.com:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        group_id="chat-group",
        enable_auto_commit=True,
)

print("채팅 프로그램 - 메세지 수신")

print("메시지 대기 중 ...")

try:
    for m in consumer:
        data = m.value
        print(f"[FREINDS] {data['message']}, {data['time']}")

except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()

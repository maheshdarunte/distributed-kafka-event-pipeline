import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'order-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order-processing-workers',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Order Consumer Service running. Listening for events...")
for message in consumer:
    order = message.value
    print(f"[Processed] Order #{order['order_id']} for {order['customer_id']} | Total: ₹{order['amount']}")
